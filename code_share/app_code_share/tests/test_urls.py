from django.core.urlresolvers import reverse, resolve
from test_plus.test import TestCase
from app_code_share.models import CodeShare
from django.utils.crypto import get_random_string
from django.test.client import RequestFactory

from code_share.views import (
    page_not_found_view,
    my_custom_error_view,
    permission_denied_view,
    bad_request_view,
)



class TestCodeShare(TestCase):

    def setUp(self):
        self.code_share = 'testcode'
        self.chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        self.hash_value = get_random_string(8, self.chars)
        self.file_name = 'testfilename'
        self.language = 'javascript'

        CodeShare.objects.create(
            code=self.code_share,
            hash_value=self.hash_value,
            file_name=self.file_name,
            language=self.language
        )

    def test_detail_reverse(self):
        """users:detail should reverse to /users/testuser/."""
        self.assertEqual(
            reverse('code_share:view_by_hash',
                    kwargs={'hash_id': self.hash_value}
                    ),
            '/app/' + self.hash_value + '/'
        )

    def test_detail_resolve(self):
        self.assertEqual(
            resolve('/app/' + self.hash_value + '/').view_name,
            'code_share:view_by_hash'
        )


class TestMyErrorPages(TestCase):

    def test_400_error(self):
        factory = RequestFactory()
        request = factory.get('/400')
        response = bad_request_view(request)
        self.assertEqual(response.status_code, 400)

    def test_403_error(self):
        factory = RequestFactory()
        request = factory.get('/403')
        response = permission_denied_view(request)
        self.assertEqual(response.status_code, 403)

    def test_404_error(self):
        factory = RequestFactory()
        request = factory.get('/404')
        response = page_not_found_view(request)
        self.assertEqual(response.status_code, 404)

    def test_500_error(self):
        factory = RequestFactory()
        request = factory.get('/500')
        response = my_custom_error_view(request)
        self.assertEqual(response.status_code, 500)

