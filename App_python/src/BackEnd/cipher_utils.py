from Crypto.Cipher import AES
from Crypto import Random
import base64
import hashlib
import os


class AES_cipher():
    def __init__(self):
        self.password = "$%Tak jim řekni Roboti$%mumlAl_malíř66se_št6tc6m/_|ústech%B87&^maloval%dál"  # FOR TESTING ONLY!!!

    # pad with spaces at the end of the text
    # beacuse AES needs 16 byte blocks
    @staticmethod
    def pad(s):
        block_size = 16
        remainder = len(s) % block_size
        padding_needed = block_size - remainder
        # Return the bytes with padding
        return s + padding_needed * b' '  # Use bytes for padding

    # remove the extra spaces at the end
    def unpad(self, s):
        return s.rstrip()

    def encrypt(self, plain_text):
        # Convert the plain text to bytes
        plain_text_bytes = plain_text.encode('utf-8')

        # Generate a random salt
        salt = os.urandom(AES.block_size)

        # Generate a random IV (initialization vector)
        iv = Random.new().read(AES.block_size)

        # Use the Scrypt KDF to get a private key from the password
        private_key = hashlib.scrypt(self.password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

        # Pad text with spaces to be valid for AES CBC mode
        padded_text = self.pad(plain_text_bytes)

        # Create cipher config
        cipher_config = AES.new(private_key, AES.MODE_CBC, iv)

        # Return a dictionary with the encrypted text
        return {
            'cipher_text': base64.b64encode(cipher_config.encrypt(padded_text)),
            'salt': base64.b64encode(salt),
            'iv': base64.b64encode(iv)
        }

    def decrypt(self, enc_dict):
        # Decode the dictionary entries from base64
        salt = base64.b64decode(enc_dict['salt'])
        enc = base64.b64decode(enc_dict['cipher_text'])
        iv = base64.b64decode(enc_dict['iv'])

        # Generate the private key from the password and salt
        private_key = hashlib.scrypt(self.password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

        # Create the cipher config
        cipher = AES.new(private_key, AES.MODE_CBC, iv)

        # Decrypt the cipher text
        decrypted = cipher.decrypt(enc)

        # Unpad the text to remove the added spaces
        original = self.unpad(decrypted)

        # Return the original text as a string
        return original.decode('utf-8')
