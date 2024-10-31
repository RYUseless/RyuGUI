import src.FrontEnd.root as FrontEnd_Root
import src.BackEnd.shrek as Funny
import src.BackEnd.cipher_utils as Cipher


if __name__ == '__main__':
    print("\t--- RyuGUI main caller ---")

    ip_pool = ["211.104.144.202", "10.80.48.14", "69.69.69.69"]
    cipher_instance = Cipher.AES_cipher()
    cipher_instance.setter(ip_pool=ip_pool)  # Nastavení IP adres
    cipher_instance.getter()  # Získání zašifrovaných dat

    Funny.Shrek.youGotShreked()

    # APPLICATION LAUNCHER:
    FrontEnd_Root.run()


