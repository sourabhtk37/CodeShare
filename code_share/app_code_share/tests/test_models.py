from test_plus.test import TestCase
from app_code_share.models import CodeShare
import random


class TestCodeShare(TestCase):

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

    def test_string_representation(self):
        code_share_object = CodeShare(file_name=self.file_name)
        self.assertEqual(str(code_share_object), code_share_object.file_name)

    def test_verbose_name(self):
        self.assertEqual(str(CodeShare._meta.verbose_name), "CodeShare")
