import uuid

from django.db import models
from taggit.managers import TaggableManager


class TestUserModelExists:
    def test_model_existence(self):
        """
        This Test tests if an Object User can be imported.
        :return:
        """

        from api.models import User

    def test_model_is_model(self):
        """
        Test if the User Object is a Django Model
        :return:
        """
        from api.models import User

        assert issubclass(User, models.Model)


class TestContractModelExists:
    def test_model_existence(self):
        """
        This Test tests if an Object Contract can be imported.
        :return:
        """

        from api.models import Contract

    def test_model_is_model(self):
        """
        Test if the Contract Object is a Django Model
        :return:
        """
        from api.models import Contract

        assert issubclass(Contract, models.Model)


class TestShiftModelExists:
    def test_model_existence(self):
        """
        This Test tests if an Object Shift can be imported.
        :return:
        """

        from api.models import Shift

    def test_model_is_model(self):
        """
        Test if the Shift Object is a Django Model
        :return:
        """
        from api.models import Shift

        assert issubclass(Shift, models.Model)


class TestReportModelExists:
    def test_model_existence(self):
        """
        This Test tests if an Object Report can be imported.
        :return:
        """

        from api.models import Report

    def test_model_is_model(self):
        """
        Test if the Report Object is a Django Model
        :return:
        """
        from api.models import Report

        assert issubclass(Report, models.Model)


class TestUserFields:
    """
    This Testsuit summerizes the basic field tests:
    1. Do all fields exist
    2. Do all fields have the correct format/class instance
    """

    def test_model_has_id_field(self, user_model_class):
        assert hasattr(user_model_class, "id")

    def test_model_has_email_field(self, user_model_class):
        assert hasattr(user_model_class, "email")

    def test_model_has_first_name_field(self, user_model_class):
        assert hasattr(user_model_class, "first_name")

    def test_model_has_last_name_field(self, user_model_class):
        assert hasattr(user_model_class, "last_name")

    def test_model_has_personal_number_filed(self, user_model_class):
        assert hasattr(user_model_class, "personal_number")

    def test_model_has_created_at_field(self, user_model_class):
        assert hasattr(user_model_class, "date_joined")

    def test_model_has_modified_at_field(self, user_model_class):
        assert hasattr(user_model_class, "modified_at")

    def test_field_type_id(self, user_model_class):
        assert isinstance(user_model_class._meta.get_field("id"), models.UUIDField)

    def test_field_type_email(self, user_model_class):
        assert isinstance(user_model_class._meta.get_field("email"), models.EmailField)

    def test_field_type_first_name(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("first_name"), models.CharField
        )

    def test_field_type_last_name(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("last_name"), models.CharField
        )

    def test_field_type_personal_number(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("personal_number"), models.CharField
        )

    def test_field_type_created_at(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("date_joined"), models.DateTimeField
        )

    def test_field_type_modified_at(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("modified_at"), models.DateTimeField
        )

    def test_field_conf_id(self, user_model_class):
        field = user_model_class._meta.get_field("id")
        assert field.primary_key
        assert field.default == uuid.uuid4
        assert not field.editable


class TestContractFields:
    """
    This Testsuit summerizes the basic field tests:
    1. Do all fields exist
    2. Do all fields have the correct format/class instance
    """

    def test_model_has_id(self, contract_model_class):
        assert hasattr(contract_model_class, "id")

    def test_model_has_user(self, contract_model_class):
        assert hasattr(contract_model_class, "user")

    def test_model_has_name(self, contract_model_class):
        assert hasattr(contract_model_class, "name")

    def test_model_has_hours(self, contract_model_class):
        assert hasattr(contract_model_class, "hours")

    def test_model_has_start_date(self, contract_model_class):
        assert hasattr(contract_model_class, "start_date")

    def test_model_has_end_date(self, contract_model_class):
        assert hasattr(contract_model_class, "end_date")

    def test_model_has_created_at(self, contract_model_class):
        assert hasattr(contract_model_class, "created_at")

    def test_model_has_created_by(self, contract_model_class):
        assert hasattr(contract_model_class, "created_by")

    def test_model_has_modified_at(self, contract_model_class):
        assert hasattr(contract_model_class, "modified_at")

    def test_model_has_modified_by(self, contract_model_class):
        assert hasattr(contract_model_class, "modified_by")

    def test_field_type_id(self, contract_model_class):
        assert isinstance(contract_model_class._meta.get_field("id"), models.UUIDField)

    def test_field_type_user(self, contract_model_class):
        assert isinstance(
            contract_model_class._meta.get_field("user"), models.ForeignKey
        )

    def test_field_type_name(self, contract_model_class):
        assert isinstance(
            contract_model_class._meta.get_field("name"), models.CharField
        )

    def test_field_type_hours(self, contract_model_class):
        assert isinstance(
            contract_model_class._meta.get_field("hours"), models.FloatField
        )

    def test_field_type_start_date(self, contract_model_class):
        assert isinstance(
            contract_model_class._meta.get_field("start_date"), models.DateField
        )

    def test_field_type_end_date(self, contract_model_class):
        assert isinstance(
            contract_model_class._meta.get_field("end_date"), models.DateField
        )

    def test_field_type_created_at(self, contract_model_class):
        assert isinstance(
            contract_model_class._meta.get_field("created_at"), models.DateTimeField
        )

    def test_field_type_created_by(self, contract_model_class):
        assert isinstance(
            contract_model_class._meta.get_field("created_by"), models.ForeignKey
        )

    def test_field_type_modified_at(self, contract_model_class):
        assert isinstance(
            contract_model_class._meta.get_field("modified_at"), models.DateTimeField
        )

    def test_field_type_modified_by(self, contract_model_class):
        assert isinstance(
            contract_model_class._meta.get_field("modified_by"), models.ForeignKey
        )

    def test_field_conf_id(self, contract_model_class):
        field = contract_model_class._meta.get_field("id")
        assert field.primary_key
        assert field.default == uuid.uuid4
        assert not field.editable


class TestShiftields:
    """
    This Testsuit summerizes the basic field tests:
    1. Do all fields exist
    2. Do all fields have the correct format/class instance
    """

    def test_model_has_id(self, shift_model_class):
        assert hasattr(shift_model_class, "id")

    def test_model_has_user(self, shift_model_class):
        assert hasattr(shift_model_class, "user")

    def test_model_has_started(self, shift_model_class):
        assert hasattr(shift_model_class, "started")

    def test_model_has_stopped(self, shift_model_class):
        assert hasattr(shift_model_class, "stopped")

    def test_model_has_contract(self, shift_model_class):
        assert hasattr(shift_model_class, "contract")

    def test_model_has_type(self, shift_model_class):
        assert hasattr(shift_model_class, "type")

    def test_model_has_note(self, shift_model_class):
        assert hasattr(shift_model_class, "note")

    def test_model_has_tags(self, shift_model_class):
        assert hasattr(shift_model_class, "tags")

    def test_model_has_was_reviewed(self, shift_model_class):
        assert hasattr(shift_model_class, "was_reviewed")

    def test_model_has_was_exported(self, shift_model_class):
        assert hasattr(shift_model_class, "was_exported")

    def test_model_has_created_at(self, shift_model_class):
        assert hasattr(shift_model_class, "created_at")

    def test_model_has_created_by(self, shift_model_class):
        assert hasattr(shift_model_class, "created_by")

    def test_model_has_modified_at(self, shift_model_class):
        assert hasattr(shift_model_class, "modified_at")

    def test_model_has_modified_by(self, shift_model_class):
        assert hasattr(shift_model_class, "modified_by")

    def test_field_type_id(self, shift_model_class):
        assert isinstance(shift_model_class._meta.get_field("id"), models.UUIDField)

    def test_field_type_user(self, shift_model_class):
        assert isinstance(shift_model_class._meta.get_field("user"), models.ForeignKey)

    def test_field_type_started(self, shift_model_class):
        assert isinstance(
            shift_model_class._meta.get_field("started"), models.DateTimeField
        )

    def test_field_type_stopped(self, shift_model_class):
        assert isinstance(
            shift_model_class._meta.get_field("stopped"), models.DateTimeField
        )

    def test_field_type_contract(self, shift_model_class):
        assert isinstance(
            shift_model_class._meta.get_field("contract"), models.ForeignKey
        )

    def test_field_type_type(self, shift_model_class):
        assert isinstance(shift_model_class._meta.get_field("type"), models.CharField)

    def test_field_type_note(self, shift_model_class):
        assert isinstance(shift_model_class._meta.get_field("note"), models.TextField)

    def test_field_type_tags(self, shift_model_class):
        assert isinstance(shift_model_class._meta.get_field("tags"), TaggableManager)

    def test_field_type_was_reviewed(self, shift_model_class):
        assert isinstance(
            shift_model_class._meta.get_field("was_reviewed"), models.BooleanField
        )

    def test_field_typ_was_exported(self, shift_model_class):
        assert isinstance(
            shift_model_class._meta.get_field("was_exported"), models.BooleanField
        )

    def test_field_type_created_at(self, shift_model_class):
        assert isinstance(
            shift_model_class._meta.get_field("created_at"), models.DateTimeField
        )

    def test_field_type_created_by(self, shift_model_class):
        assert isinstance(
            shift_model_class._meta.get_field("created_by"), models.ForeignKey
        )

    def test_field_type_modified_at(self, shift_model_class):
        assert isinstance(
            shift_model_class._meta.get_field("modified_at"), models.DateTimeField
        )

    def test_field_type_modified_by(self, shift_model_class):
        assert isinstance(
            shift_model_class._meta.get_field("modified_by"), models.ForeignKey
        )

    def test_field_conf_id(self, shift_model_class):
        field = shift_model_class._meta.get_field("id")
        assert field.primary_key
        assert field.default == uuid.uuid4
        assert not field.editable

    def test_field_conf_user(self, shift_model_class, user_model_class):
        field = shift_model_class._meta.get_field("user")
        assert issubclass(field.remote_field.model, user_model_class)

    def test_field_conf_contract(self, shift_model_class, contract_model_class):
        field = shift_model_class._meta.get_field("contract")
        assert issubclass(field.remote_field.model, contract_model_class)

    def test_field_conf_type(self, shift_model_class):
        choices = (("st", "Shift"), ("sk", "Sick"), ("vn", "Vacation"))
        field = shift_model_class._meta.get_field("type")
        assert field.choices == choices

    def test_field_conf_was_reviewed(self, shift_model_class):
        field = shift_model_class._meta.get_field("was_reviewed")
        assert (
            field.default == True
        )  # if no default is provided django returns an object which would be allways True

    def test_field_conf_was_exported(self, shift_model_class):
        field = shift_model_class._meta.get_field("was_exported")
        assert not field.default

    def test_field_conf_created_at(self, shift_model_class):
        field = shift_model_class._meta.get_field("created_at")
        assert field.auto_now_add

    def test_field_conf_created_by(self, shift_model_class, user_model_class):
        field = shift_model_class._meta.get_field("created_by")
        assert issubclass(field.remote_field.model, user_model_class)

    def test_field_conf_modified_at(self, shift_model_class):
        field = shift_model_class._meta.get_field("modified_at")
        assert field.auto_now

    def test_field_conf_modified_by(self, shift_model_class, user_model_class):
        field = shift_model_class._meta.get_field("modified_by")
        assert issubclass(field.remote_field.model, user_model_class)


class TestReportFields:
    """
    This Testsuit summerizes the basic field tests:
    1. Do all fields exist
    2. Do all fields have the correct format/class instance
    """

    def test_model_has_id(self, report_model_class):
        assert hasattr(report_model_class, "id")

    def test_model_has_user(self, report_model_class):
        assert hasattr(report_model_class, "user")

    def test_model_has_month_year(self, report_model_class):
        assert hasattr(report_model_class, "month_year")

    def test_model_has_hours(self, report_model_class):
        assert hasattr(report_model_class, "hours")

    def test_model_has_contract(self, report_model_class):
        assert hasattr(report_model_class, "contract")

    def test_model_has_created_at(self, report_model_class):
        assert hasattr(report_model_class, "created_at")

    def test_model_has_created_by(self, report_model_class):
        assert hasattr(report_model_class, "created_by")

    def test_model_has_modified_at(self, report_model_class):
        assert hasattr(report_model_class, "modified_at")

    def test_model_has_modified_by(self, report_model_class):
        assert hasattr(report_model_class, "modified_by")

    def test_field_type_id(self, report_model_class):
        assert isinstance(report_model_class._meta.get_field("id"), models.UUIDField)

    def test_field_type_user(self, report_model_class):
        assert isinstance(report_model_class._meta.get_field("user"), models.ForeignKey)

    def test_field_type_month_year(self, report_model_class):
        assert isinstance(
            report_model_class._meta.get_field("month_year"), models.DateField
        )

    def test_field_type_hours(self, report_model_class):
        assert isinstance(
            report_model_class._meta.get_field("hours"), models.DurationField
        )

    def test_field_type_contract(self, report_model_class):
        assert isinstance(
            report_model_class._meta.get_field("contract"), models.ForeignKey
        )

    def test_field_type_created_at(self, report_model_class):
        assert isinstance(
            report_model_class._meta.get_field("created_at"), models.DateTimeField
        )

    def test_field_type_created_by(self, report_model_class):
        assert isinstance(
            report_model_class._meta.get_field("created_by"), models.ForeignKey
        )

    def test_field_type_modified_at(self, report_model_class):
        assert isinstance(
            report_model_class._meta.get_field("modified_at"), models.DateTimeField
        )

    def test_field_type_modified_by(self, report_model_class):
        assert isinstance(
            report_model_class._meta.get_field("modified_by"), models.ForeignKey
        )

    def test_field_conf_id(self, report_model_class):
        field = report_model_class._meta.get_field("id")
        assert field.primary_key
        assert field.default == uuid.uuid4
        assert not field.editable

    def test_field_conf_user(self, report_model_class, user_model_class):
        field = report_model_class._meta.get_field("user")
        assert issubclass(field.remote_field.model, user_model_class)

    def test_field_conf_contract(self, report_model_class, contract_model_class):
        field = report_model_class._meta.get_field("contract")
        assert issubclass(field.remote_field.model, contract_model_class)

    def test_field_conf_created_at(self, report_model_class):
        field = report_model_class._meta.get_field("created_at")
        assert field.auto_now_add

    def test_field_conf_created_by(self, report_model_class, user_model_class):
        field = report_model_class._meta.get_field("created_by")
        assert issubclass(field.remote_field.model, user_model_class)

    def test_field_conf_modified_at(self, report_model_class):
        field = report_model_class._meta.get_field("modified_at")
        assert field.auto_now

    def test_field_conf_modified_by(self, report_model_class, user_model_class):
        field = report_model_class._meta.get_field("modified_by")
        assert issubclass(field.remote_field.model, user_model_class)
