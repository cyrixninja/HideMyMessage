import unittest
from app import encrypt_message
from cryptography.fernet import Fernet

class TestApp(unittest.TestCase):
    def test_encrypt_message(self):
        message = "Hello, World!"
        key = Fernet.generate_key().decode()
        encrypted_message = encrypt_message(message, key)
        self.assertIsNotNone(encrypted_message)

    def test_encrypt_message_empty_message(self):
        key = Fernet.generate_key().decode()
        with self.assertRaises(ValueError):
            encrypt_message("", key)

if __name__ == '__main__':
    unittest.main()