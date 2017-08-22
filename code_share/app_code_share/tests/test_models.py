from test_plus.test import TestCase
from app_code_share.models import CodeShare
from django.utils.crypto import get_random_string



class TestCodeShare(TestCase):

    def setUp(self):
        self.code_share = 'testcode'
        self.chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        self.hash_value = get_random_string(8, self.chars)
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
