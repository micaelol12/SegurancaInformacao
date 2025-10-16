from AES import AES
from Crypto.Cipher import AES as CryptoAES
from Crypto.Util.Padding import pad, unpad


def test_aes_encryption():
    key = b'ABCDEFGHIJKLMNOP'
    msg = b'DESENVOLVIMENTO!'

    aes = AES(key)
    ciphertext  = aes.encrypt(msg=msg)

    cipher_lib = CryptoAES.new(key, CryptoAES.MODE_ECB)
    ciphertext_lib = cipher_lib.encrypt(pad(msg, 16))  

    assert ciphertext == ciphertext_lib, "Custom AES encryption does not match library AES encryption"