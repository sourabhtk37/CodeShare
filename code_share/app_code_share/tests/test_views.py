from test_plus.test import TestCase
from app_code_share.models import CodeShare
from django.utils.crypto import get_random_string


class TestCodeShare(TestCase):

    def setUp(self):
        self.code_share = 'testcode'
        self.chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        self.hash_value = get_random_string(8, self.chars)
        self.random_string = get_random_string(8, self.chars)
        self.file_name = 'testfilename'
        self.language = 'c-like'

        CodeShare.objects.create(
            code=self.code_share,
            hash_value=self.hash_value,
            file_name=self.file_name,
            language=self.language
        )

    def test_post_list(self):
        response = self.client.get('/app/' + self.hash_value + '/')
        self.assertEqual(response.status_code, 200)
