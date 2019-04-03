import pytest
from pytz import datetime

from api.models import Report

# This conftest file provides all necessary test data concerning the Report Model.
# It will be imported by the conftest.py in the parent directory.


@pytest.fixture
def create_n_report_objects():
    """
    This fixture resembles a report object factory.
    Shifts are distinguised by id, there is no specific need for the start_stop mechanism.
    Nonetheless in terms of consistency this mechanism is kept as in the user_conftest.py.
    :return: Function
    """
    month_year = datetime.date(2019, 1, 1)
    hours = datetime.timedelta(0)
    created_at = datetime.datetime(2019, 1, 1, 16).isoformat()
    modified_at = created_at

    def create_reports(start_stop, user, contract, month_year=month_year):
        lst = []
        for i in range(*start_stop):
            report = Report.objects.create(
                month_year=month_year,
                hours=hours,
                contract=contract,
                user=user,
                created_by=user,
                modified_by=user,
                created_at=created_at,
                modified_at=modified_at,
            )
            lst.append(report)

        return lst

    return create_reports


@pytest.fixture
def report_object(create_n_report_objects, user_object, contract_object):
    """
    This fixture creates one report object.
    :param create_n_report_objects:
    :param user_object:
    :param contract_object:
    :return:
    """
    return create_n_report_objects((1,), user_object, contract_object)[0]


@pytest.fixture
def db_get_current_endpoint(
    create_n_report_objects, user_object, contract_object, report_object
):
    """
    This fixture creates two reports for February and March 2019.
    :param create_n_report_objects:
    :param user_object:
    :param contract_object:
    :param report_object:
    :return:
    """
    # create 2 more Reports for February and March
    create_n_report_objects(
        (1,), user_object, contract_object, month_year=datetime.date(2019, 2, 1)
    )
    create_n_report_objects(
        (1,), user_object, contract_object, month_year=datetime.date(2019, 3, 1)
    )