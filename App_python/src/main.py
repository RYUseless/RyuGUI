import src.FrontEnd.main_gui as frontend
import src.BackEnd.Shrek as Funny
import src.BackEnd.cipher_utils as Cipher

if __name__ == '__main__':
    # Funny.youGotShreked()
    print("\t--- RyuGUI main caller ---")
    # # cipher testing:
    ip_pool = ["10.56.62.101", "173.123.123.255"]
    # Initialize empty lists to store encrypted and decrypted IPs
    cipher_instance = Cipher.AES_cipher()
    # Encrypt each IP address
    cipher_instance.setter(ip_pool=ip_pool)
    cipher_instance.getter()


    # #Frontend launcher# #
    #frontend.run()
