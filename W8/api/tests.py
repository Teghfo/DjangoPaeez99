from django.test import TestCase
from rest_framework.test import APIRequestFactory


from .views import AuthorViewSet


class AuthorViewSetTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = AuthorViewSet.as_view({'get': 'list'})
        print('in setup')

    def test_get_functionality(self):
        request = self.factory.get('author_list/', format='json')
        response = self.view(request)

        self.assertEqual(response.status_code, 200)
