from django.core.urlresolvers import reverse, resolve
from test_plus.test import TestCase
from app_code_share.models import CodeShare
from django.utils.crypto import get_random_string



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
