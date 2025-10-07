from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad,unpad

chave = bytes([65, 66, 67, 68, 69])

# Mensagem original
def criptografa(mensagem, mode):
    if isinstance(mensagem, str):
        texto_simples = mensagem.encode('utf-8')
    elif isinstance(mensagem, bytes):
        texto_simples = mensagem
    else:
        raise TypeError("Mensagem deve ser str ou bytes")

    cipher_encrypt = Blowfish.new(chave, mode)
    texto_preenchido = pad(texto_simples, Blowfish.block_size, style='pkcs7')
    texto_cifrado = cipher_encrypt.encrypt(texto_preenchido)
    hex_string = texto_cifrado.hex()
    
    # separa em bytes (2 chars) com espaço
    bytes_hex = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
    
    # agora imprime em linhas de 8 bytes
    for i in range(0, len(bytes_hex), 8):
        linha = ' '.join(bytes_hex[i:i+8])
        print(linha.upper())
    
    print("Tamanho:", len(texto_cifrado))

    return texto_cifrado

def decifrar(msg_cifrado,mode,iv):
    cipher = Blowfish.new(chave, mode, iv)
    texto_decifrado = cipher.decrypt(msg_cifrado)
    try:
        texto_final = unpad(texto_decifrado, Blowfish.block_size, style='pkcs7')
    except ValueError as e:
        print("Erro ao remover padding:", e)
        return None
    print("Decifrado:", texto_final.decode('utf-8'))
    return texto_final


# criptografa("FURB",Blowfish.MODE_ECB)
# criptografa("COMPUTADOR",Blowfish.MODE_ECB)
# criptografa("SABONETE",Blowfish.MODE_ECB)
# criptografa(bytes([8, 8, 8, 8, 8, 8, 8, 8]),Blowfish.MODE_ECB)
# criptografa("SABONETESABONETESABONETE",Blowfish.MODE_ECB)
cifrado = criptografa("FURB",Blowfish.MODE_CBC)
decifrar(cifrado,Blowfish.MODE_CBC,None)