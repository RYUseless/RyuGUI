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

    def __encrypt(self, plain_text):
        # plain text → bytes convertion
        plain_text_bytes = plain_text.encode('utf-8')

        # Generating salt for entropy
        salt = os.urandom(16)  # 16 bytes for salt

        # Use the Scrypt KDF to derive a private key from the password
        private_key = hashlib.scrypt(self.password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

        # Generating Nonce for AES EAX
        nonce = get_random_bytes(16)  # 16 bytes for nonce

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
            return decrypted_bytes.decode('utf-8')
        except ValueError:
            return "Decryption failed or data was tampered with."

    def setter(self, ip_pool):  # will think of a better name soon
        print("\n\t\t--- encripter ---")
        for ip in ip_pool:
            encrypted_ip = self.__encrypt(ip)
            self.encrypted_pool.append(encrypted_ip)
            print(f"Encrypted text: {encrypted_ip['cipher_text']}")

    def getter(self):  # will think of a better name soon
        print("\n\t\t--- decrypter ---")
        for encrypted_data in self.encrypted_pool:
            decrypted_ip = self.__decrypt(encrypted_data)
            self.decrypted_pool.append(decrypted_ip)
            print(f"Decrypted secret message: {decrypted_ip}")
