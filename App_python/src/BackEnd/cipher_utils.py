import os
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class AES_cipher:
    def __init__(self):
        self.password = "$%Tak jim řekni Roboti$%mumlAl_malíř66se_št6tc6m/_|ústech%B87&^maloval%dál"  # FOR TESTING ONLY!!!
        self.encrypted_pool = []
        self.decrypted_pool = []

    def __pad(self, s):
        """Pad input text using PKCS7 padding to match the block size."""
        block_size_num = self.set_block_size(s)
        padding_len = block_size_num - len(s) % block_size_num
        padding = chr(padding_len) * padding_len
        return s + padding

    @staticmethod
    def __unpad(s):
        """Remove PKCS7 padding after decryption."""
        padding_len = ord(s[-1])
        return s[:-padding_len]

    @staticmethod
    def set_block_size(secret):
        secret_val = len(secret)  # count lengh only once :)
        if secret_val <= 32:
            print("## block size: 32")
            return 32
        else:
            return_val = ((secret_val - 1) // 32 + 1) * 32  # -1 pro zaokrouhleni
            print("## block size val:", return_val)
            return return_val

    def __encrypt(self, plain_text):
        # Pad the input text to the block size
        padded_text = self.__pad(plain_text)
        plain_text_bytes = padded_text.encode('utf-8')

        # Generating salt for entropy
        salt = os.urandom(16)

        # Use the Scrypt KDF to derive a private key from the password
        private_key = hashlib.scrypt(self.password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

        # Generating Nonce for AES EAX
        nonce = get_random_bytes(16)

        # Set AES cipher mode to EAX, add key and nonce
        cipher = AES.new(private_key, AES.MODE_EAX, nonce=nonce)

        # Encrypting provided text and doing integrity check (tag)
        cipher_text, tag = cipher.encrypt_and_digest(plain_text_bytes)

        # Return: encrypted text, salt, nonce, and tag
        return {
            'cipher_text': base64.b64encode(cipher_text).decode('utf-8'),
            'salt': base64.b64encode(salt).decode('utf-8'),
            'nonce': base64.b64encode(nonce).decode('utf-8'),
            'tag': base64.b64encode(tag).decode('utf-8')
        }

    def __decrypt(self, enc_dict):
        # Decode the dictionary entries from base64
        salt = base64.b64decode(enc_dict['salt'])
        cipher_text = base64.b64decode(enc_dict['cipher_text'])
        nonce = base64.b64decode(enc_dict['nonce'])
        tag = base64.b64decode(enc_dict['tag'])

        # Generate the private key from the password and salt
        private_key = hashlib.scrypt(self.password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

        # Create the cipher object using EAX mode
        cipher = AES.new(private_key, AES.MODE_EAX, nonce=nonce)

        # Decrypt the cipher text and verify the tag for integrity check
        try:
            decrypted_bytes = cipher.decrypt_and_verify(cipher_text, tag)
            decrypted_text = decrypted_bytes.decode('utf-8')
            return self.__unpad(decrypted_text)  # Remove padding after decryption
        except ValueError:
            return "Decryption failed or data was tampered with."

    def setter(self, ip_pool):
        print("\n\t\t--- ENCRYPTER ---")
        for ip in ip_pool:
            encrypted_ip = self.__encrypt(ip)
            self.encrypted_pool.append(encrypted_ip)
            print(f"Encrypted text: {encrypted_ip['cipher_text']}")

    def getter(self):
        print("\n\t\t--- DECRYPTER ---")
        for encrypted_data in self.encrypted_pool:
            decrypted_ip = self.__decrypt(encrypted_data)
            self.decrypted_pool.append(decrypted_ip)
            print(f"Decrypted secret message: {decrypted_ip}")

