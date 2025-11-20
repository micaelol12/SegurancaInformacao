from AES import AES
from Crypto.Cipher import AES as CryptoAES
from Crypto.Util.Padding import pad


def test_aes_encryption():
    key = b'ABCDEFGHIJKLMNOP'
    msg = b'DESENVOLVIMENTO!'

    aes = AES(key)
    ciphertext  = aes.encrypt(msg=msg)

    cipher_lib = CryptoAES.new(key, CryptoAES.MODE_ECB)
    ciphertext_lib = cipher_lib.encrypt(pad(msg, 16))  

    assert ciphertext == ciphertext_lib
    
def test_aes_decryption():
    key = b'ABCDEFGHIJKLMNOP'
    msg = b'DESENVOLVIMENTO!'
    
    aes = AES(key)
    ciphertext  = aes.encrypt(msg=msg)
    
    d_msg = aes.decrypt(ciphertext)
    
    assert msg == d_msg
