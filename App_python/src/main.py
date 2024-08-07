import src.FrontEnd.main_gui as frontend
import src.BackEnd.Shrek as Funny
import src.BackEnd.cipher_utils as Cipher

if __name__ == '__main__':
    Funny.youGotShreked()
    print("--- RyuGUI main caller ---")
    # # cipher testing:
    ip_pool = ["10.56.62.101", "173.123.123.255"]

    # Initialize empty lists to store encrypted and decrypted IPs
    encrypted_pool = []
    decrypted_pool = []
    cipher_instance = Cipher.AES_cipher()

    # Encrypt each IP address
    for ip in ip_pool:
        encrypted_ip = cipher_instance.encrypt(ip)
        encrypted_pool.append(cipher_instance.encrypt(ip))
        print(f"Encrypted text: {encrypted_ip['cipher_text'].decode('utf-8')}")

    # Decrypt each encrypted IP address
    for encrypted_data in encrypted_pool:
        decrypted_ip = cipher_instance.decrypt(encrypted_data)
        decrypted_pool.append(decrypted_ip)
        print(f"Decrypted secret message: {decrypted_ip}")

    # #Frontend launcher# #
    #frontend.run()
