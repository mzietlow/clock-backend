import json
from datetime import datetime

import pytest
import time
from django.urls import reverse
from freezegun import freeze_time
from rest_framework import status
from pytz import datetime, utc
from api.models import Contract, Shift, Report
from api.utilities import relativedelta_to_string


def test_relativedelta_to_string_positive_delta(positive_relativedelta_object):
    result_string = relativedelta_to_string(positive_relativedelta_object)
    assert result_string == "148:23:15"


def test_relativedelta_to_string_negative_delta(negative_relativedelta_object):
    result_string = relativedelta_to_string(negative_relativedelta_object)
    assert result_string == "-148:23:15"


class TestUpdateSignals:
    @pytest.mark.django_db
    def test_signal_updates_with_prev_month_carry_over(
        self, report_update_user, report_update_contract, report_update_february_report
    ):
        """
        Test that on an update the Report Update signal takes the previous months hours - Contrac.hours as carry over.
        :param report_update_user:
        :param report_update_contract:
        :param report_update_february_report:
        :return:
        """
        shift = Shift.objects.create(
            started=datetime.datetime(2019, 2, 11, 14, tzinfo=utc),
            stopped=datetime.datetime(2019, 2, 11, 16, tzinfo=utc),
            created_at=datetime.datetime(2019, 2, 11, 16, tzinfo=utc).isoformat(),
            modified_at=datetime.datetime(2019, 2, 11, 16, tzinfo=utc).isoformat(),
            type="st",
            note="smth",
            user=report_update_user,
            created_by=report_update_user,
            modified_by=report_update_user,
            contract=report_update_contract,
        )

        shift.stopped = datetime.datetime(2019, 2, 11, 18, tzinfo=utc)
        shift.save()

        assert Report.objects.get(
            contract=report_update_contract, month_year=datetime.date(2019, 2, 1)
        ).hours == datetime.timedelta(hours=-16)

    @pytest.mark.django_db
    def test_signal_updates_shifts_report(
        self, report_object, contract_object, user_object
    ):
        """
        Test if the Report Object belonging to a Shift gets updated on save.
        :param report_object:
        :param contract_object:
        :param user_object:
        :return:
        """
        # Creeate shift for 29.01. which is 2 hours long
        Shift.objects.create(
            started=datetime.datetime(2019, 1, 29, 14, tzinfo=utc),
            stopped=datetime.datetime(2019, 1, 29, 16, tzinfo=utc),
            created_at=datetime.datetime(2019, 1, 29, 16, tzinfo=utc).isoformat(),
            modified_at=datetime.datetime(2019, 1, 29, 16, tzinfo=utc).isoformat(),
            type="st",
            note="smth",
            user=user_object,
            created_by=user_object,
            modified_by=user_object,
            contract=contract_object,
        )

        assert Report.objects.get(
            contract=contract_object, month_year=datetime.date(2019, 1, 1)
        ).hours == datetime.timedelta(hours=2)

    @pytest.mark.django_db
    def test_signal_updates_next_months_report(
        self,
        report_object,
        february_report_object,
        contract_ending_in_february,
        user_object,
    ):

        # Create shift for 29.01. which is 2 hours long
        Shift.objects.create(
            started=datetime.datetime(2019, 1, 29, 14, tzinfo=utc),
            stopped=datetime.datetime(2019, 1, 29, 16, tzinfo=utc),
            created_at=datetime.datetime(2019, 1, 29, 16, tzinfo=utc).isoformat(),
            modified_at=datetime.datetime(2019, 1, 29, 16, tzinfo=utc).isoformat(),
            type="st",
            note="smth",
            user=user_object,
            created_by=user_object,
            modified_by=user_object,
            contract=contract_ending_in_february,
        )

        assert Report.objects.get(
            contract=contract_ending_in_february, month_year=datetime.date(2019, 2, 1)
        ).hours == datetime.timedelta(hours=-18)

    @pytest.mark.django_db
    def test_signal_only_updates_reviewed_shifts(
        self, report_object, contract_object, user_object
    ):
        Shift.objects.create(
            started=datetime.datetime(2019, 1, 29, 14, tzinfo=utc),
            stopped=datetime.datetime(2019, 1, 29, 16, tzinfo=utc),
            created_at=datetime.datetime(2019, 1, 29, 16, tzinfo=utc).isoformat(),
            modified_at=datetime.datetime(2019, 1, 29, 16, tzinfo=utc).isoformat(),
            type="st",
            note="smth",
            user=user_object,
            created_by=user_object,
            modified_by=user_object,
            contract=contract_object,
            was_reviewed=False,
        )
        assert Report.objects.get(
            contract=contract_object, month_year=datetime.date(2019, 1, 1)
        ).hours == datetime.timedelta(0)
