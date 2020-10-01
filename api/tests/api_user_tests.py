from unittest import TestCase
# Under development
# settings.configure()
import pytest
from rest_framework.test import RequestsClient


@pytest.mark.django_db
class UserTest(TestCase):
    """ Test module for Puppy model """

    # def setUp(self):
    #     User.objects.create(
    #         username='Casper', email='asad@sdad.coza', is_staff=True).save()

    def test_API_user(self):
        # client = RequestsClient()
        #
        # # Obtain a CSRF token.
        # response = client.get('http://127.0.0.1:9090/api-auth/login/')
        # assert response.status_code == 200
        # csrftoken = response.cookies['csrftoken']
        #
        # # Interact with the API.
        # response = client.post('http://127.0.0.1:9090/api-auth/login/', json={
        #     'username': 'MegaCorp',
        #     'password': 'active'
        # }, headers={'X-CSRFToken': csrftoken})
        # assert response.status_code == 200

        from requests.auth import HTTPBasicAuth

        # Include an appropriate `Authorization:` header on all requests.
        # token = Token.objects.get(user__username='lauren')
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        client = RequestsClient()
        client.auth = HTTPBasicAuth('jody', 'rekless')
        # client.headers.update({'x-test': 'true'})
        test = client.login()

        response = client.post('http://127.0.0.1:9090/api-auth/login/')
        assert response.status_code == 200
