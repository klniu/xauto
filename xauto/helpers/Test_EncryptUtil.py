from unittest import TestCase

from xauto.helpers.EncryptUtil import aes_encrypt, aes_decrypt


class Test_EncryptUtil(TestCase):
    def test_aes_encrypt(self):
        encrypt = aes_encrypt("keyaaaa", "asdfasdf")
        self.assertEqual(encrypt, "kQyhxU34SR9ryIUgG39EjQ==")
        decrypt = aes_decrypt("keyaaaa", encrypt)
        self.assertEqual(decrypt, "asdfasdf")
