from django.core.urlresolvers import reverse, resolve
from test_plus.test import TestCase
from app_code_share.models import CodeShare
import random


class TestUserURLs(TestCase):
    """TEST URL PATTER FOR BLOG APP"""

    def setUp(self):
        self.code_share = 'testcode'
        self.a = random.randrange(0, 6)
        self.hash_value = str(hash(self.code_share))[self.a:self.a + 8]
        self.file_name = 'testfilename'

        CodeShare.objects.create(
            code=self.code_share,
            hash_value=self.hash_value,
            file_name=self.file_name
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
