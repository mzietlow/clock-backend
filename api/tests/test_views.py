# View tests come here

import pytest
import json

from django.urls import reverse
from rest_framework import status
from datetime import datetime


from api.models import Contract, Shift


class TestContractApiEndpoint:
    """
    This TestCase includes:
       - tests which try accesing an Endpoint without a provided JWT
           --> These tests will not be repeated for other Endpoints since in V1 every endpoint shares the same
               permission_class and authentication_class
       - tests which try to change the values fro user, created_by and modified by
           --> These tests will not be repeated for other Endpoints since in V1 every endpoint shares the same base
               serializer which provides this provides this Functionality
       - tests which try to create a Contract for a different user than who is issueing the request
           --> These tests will not be repeated for other Endpoints since in V1 every endpoint shares the same base
               serializer which provides this provides this Functionality
    """

    @pytest.mark.django_db
    def test_get_only_own_contract(
        self, client, user_object_jwt, diff_user_contract_object
    ):
        """
        Test that attempting to retrieve a contract, which does not belong to the User requesting it,
        gives a 404 response.
        :param client:
        :param user_object_jwt:
        :param diff_user_contract_object:
        :return:
        """
        client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt))
        response = client.get(
            path=reverse("api:contracts-detail", args=[diff_user_contract_object.id])
        )
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_forbidden_without_jwt(self, client, contract_object):
        """
        Test the detail Endpoint returns a 401 if no JWT is present.
        :param client:
        :param contract_object:
        :param user_object:
        :return:
        """
        response = client.get(path=r"/api/contracts/", args=[contract_object.id])
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_list_forbidden_without_jwt(self, client):
        """
        Test the list endpoint returns a 401 if no JWT is present.
        :param client:
        :return:
        """
        response = client.get(path="http://localhost:8000/api/contracts/")
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_create_forbidden_without_jwt(self, client, valid_contract_json):
        """
        Test the create endpoint returns a 401 if no JWT is present
        :param client:
        :param valid_contract_json:
        :return:
        """
        response = client.post(
            path="http://localhost:8000/api/contracts/", data=valid_contract_json
        )
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_put_forbidden_without_jwt(self, client, valid_contract_json):

        response = client.put(
            path="http://localhost:8000/api/contracts/", data=valid_contract_json
        )
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_list_objects_of_request_user(
        self, client, user_object, user_object_jwt, db_creation_contracts_list_endpoint
    ):
        """
        Test that the list-endpoint only retrieves the Contracts of the User who issues the request.
        :param client:
        :param user_object:
        :param user_object_jwt:
        :param create_n_user_objects:
        :param create_n_contract_objects:
        :return:
        """

        client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt))
        response = client.get(path="http://localhost:8000/api/contracts/")
        data = json.loads(response.content)
        assert response.status_code == 200
        assert all(
            Contract.objects.get(id=contract["id"]).user.id == user_object.id
            for contract in data
        )

    @pytest.mark.django_db
    def test_create_with_correct_user(
        self, client, invalid_uuid_contract_json, user_object, user_object_jwt
    ):
        """
        Test that 'user', 'created_by' and 'modified_by' (incorrectly set invalid_uuid_contract_json)
        are set to the user_id from the JWT of the request.
        :param invalid_uuid_contract_json:
        :param user_object:
        :return:
        """

        client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt))
        response = client.post(path="/api/contracts/", data=invalid_uuid_contract_json)

        content = json.loads(response.content)

        assert response.status_code == status.HTTP_201_CREATED
        new_contract = Contract.objects.get(id=content["id"])

        assert new_contract.user.id == user_object.id
        assert new_contract.created_by.id == user_object.id
        assert new_contract.created_by.id == user_object.id

    @pytest.mark.django_db
    def test_update_uuid_contract(
        self,
        client,
        invalid_uuid_contract_put_endpoint,
        contract_object,
        user_object,
        user_object_jwt,
    ):
        """
        Test that updating 'user', 'created_by' and 'modified_by' does not work.
        This is tested via 'invalid_uuid_contract_json' which has non-existent uuid's in these fields.
        By testing with this fixture it is also covered that even if the uuid corresponds to a existent user
        it is not possible to switch/modify the contracts owner.

        :param client:
        :param invalid_uuid_contract_json:
        :param contract_object:
        :return:
        """

        client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt))
        response = client.put(
            path=reverse("api:contracts-detail", args=[contract_object.id]),
            data=invalid_uuid_contract_put_endpoint,
        )
        content = json.loads(response.content)

        assert response.status_code == 200
        # Check that neither "user", "created_by" nor "modified_by" changed from the originial/issuing user
        user_id = user_object.id
        contract = Contract.objects.get(id=contract_object.id)
        assert contract.user.id == user_id
        assert contract.created_by.id == user_id
        assert contract.modified_by.id == user_id
        #      New Datetime           Old Datetime  --> Result should be positive
        assert contract.modified_at > contract_object.modified_at

    @pytest.mark.django_db
    def test_patch_uuid_contract(
        self,
        client,
        invalid_uuid_contract_patch_endpoint,
        contract_object,
        user_object,
        user_object_jwt,
    ):
        """
        Test that trying to patch 'user, 'created_by' and 'mdofied_by' does not work.
        Updating other values do not need to be tested here.
        :param client:
        :param invalid_uuid_contract_patch_endpoint:
        :param contract_object:
        :param user_object:
        :param user_obejct_jwt:
        :return:
        """
        client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt))
        response = client.patch(
            path=reverse("api:contracts-detail", args=[contract_object.id]),
            data=invalid_uuid_contract_patch_endpoint,
        )
        contract = Contract.objects.get(id=contract_object.id)
        user_id = user_object.id
        assert response.status_code == 200

        assert contract.user.id == user_id
        assert contract.created_by.id == user_id
        assert contract.modified_by.id == user_id
        #      New Datetime           Old Datetime  --> Result should be positive
        assert contract.modified_at > contract_object.modified_at


class TestShiftApiEndpoint:
    @pytest.mark.django_db
    def test_list_objects_of_request_user(
        self, client, user_object, user_object_jwt, db_creation_shifts_list_endpoint
    ):

        client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt))
        response = client.get(path="http://localhost:8000/api/shifts/")

        data = json.loads(response.content)
        assert response.status_code == 200
        assert all(
            Shift.objects.get(id=shift["id"]).user.id == user_object.id
            for shift in data
        )

    @pytest.mark.django_db
    def test_create(self, client, user_object, user_object_jwt, valid_shift_json):
        client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt))
        response = client.post(
            path="http://localhost:8000/api/shifts/", data=valid_shift_json
        )
        data = json.loads(response.content)

        assert response.status_code == 201
        shift_object = Shift.objects.get(pk=data["id"])
        initial_tags = json.loads(valid_shift_json["tags"])

        assert shift_object
        assert shift_object.tags.all().count() == len(initial_tags)

        assert all(
            shift_tag.name in initial_tags for shift_tag in shift_object.tags.all()
        )

    @pytest.mark.django_db
    def test_put_new_tags(self, client, user_object_jwt, put_new_tags_json):
        client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt))
        response = client.put(
            path=reverse("api:shifts-detail", args=[put_new_tags_json["id"]]),
            data=put_new_tags_json,
        )

        data = json.loads(response.content)
        initial_tags = json.loads(put_new_tags_json["tags"])

        assert response.status_code == 200
        shift_object = Shift.objects.get(pk=put_new_tags_json["id"])
        assert shift_object.tags.all().count() == len(initial_tags)
        assert all(
            shift_tag.name in initial_tags for shift_tag in shift_object.tags.all()
        )

    @pytest.mark.django_db
    def test_patch_new_tags(self, client, user_object_jwt, patch_new_tags_json):
        client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt))
        response = client.patch(
            path=reverse("api:shifts-detail", args=[patch_new_tags_json["id"]]),
            data=patch_new_tags_json,
        )

        initial_tags = json.loads(patch_new_tags_json["tags"])

        assert response.status_code == 200
        shift_object = Shift.objects.get(pk=patch_new_tags_json["id"])

        assert shift_object.tags.all().count() == len(initial_tags)
        assert all(
            shift_tag.name in initial_tags for shift_tag in shift_object.tags.all()
        )

    @pytest.mark.django_db
    def test_list_month_year_endpoint(
        self, client, user_object_jwt, db_creation_list_month_year_endpoint
    ):
        client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt))
        response = client.get(path=reverse("api:list-shifts", args=[1, 2019]))

        data = json.loads(response.content)
        print(data)
        assert response.status_code == 200
        assert len(data) == 2
        assert all(
            datetime.strptime(i["started"], "%Y-%m-%dT%H:%M:%SZ").month == 1
            and datetime.strptime(i["started"], "%Y-%m-%dT%H:%M:%SZ").year == 2019
            for i in data
        )
