from AES import AES
from Crypto.Cipher import AES as CryptoAES
from Crypto.Util.Padding import pad, unpad

key = b'ABCDEFGHIJKLMNOP'
msg = b'DESENVOLVIMENTO!'

aes = AES(key)
ciphertext  = aes.encrypt(msg=msg)
print(ciphertext.hex())

cipher_lib = CryptoAES.new(key, CryptoAES.MODE_ECB)
ciphertext_lib = cipher_lib.encrypt(pad(msg, 16))  

print("Custom AES:  ", ciphertext.hex())
print("Lib AES:     ", ciphertext_lib.hex())


d_msg = aes.decrypt(ciphertext_lib)
