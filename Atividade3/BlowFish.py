from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad,unpad
import os

chave = bytes([65, 66, 67, 68, 69])

# Mensagem original
def criptografa(mensagem, mode,iv = None):
    
    if isinstance(mensagem, str):
        texto_simples = mensagem.encode('utf-8')
    elif isinstance(mensagem, bytes):
        texto_simples = mensagem
    else:
        raise TypeError("Mensagem deve ser str ou bytes")

    if iv is None:
        cipher_encrypt = Blowfish.new(chave, mode)
    else:
        cipher_encrypt = Blowfish.new(chave, mode, iv)

    texto_preenchido = pad(texto_simples, Blowfish.block_size, style='pkcs7')
    texto_cifrado = cipher_encrypt.encrypt(texto_preenchido)
    hex_string = texto_cifrado.hex()
    
    bytes_hex = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
    
    for i in range(0, len(bytes_hex), 8):
        linha = ' '.join(bytes_hex[i:i+8])
        print(linha.upper())
    
    print("Tamanho:", len(texto_cifrado))

    return texto_cifrado

def decifrar(msg_cifrado,mode,iv = None):
    if iv is None:
        cipher = Blowfish.new(chave, mode)
    else:
        cipher = Blowfish.new(chave, mode, iv)
        
    texto_decifrado = cipher.decrypt(msg_cifrado)
    try:
        texto_final = unpad(texto_decifrado, Blowfish.block_size, style='pkcs7')
    except ValueError as e:
        print("Erro ao remover padding:", e)
        return None
    
    print("Decifrado:", texto_decifrado.decode('utf-8'))
    return texto_final

def criptografar_arquivo():
    arquivo_entrada = "Atividade3\entrada.pdf"  # coloque aqui o nome exato do PDF original
    arquivo_saida = "Atividade3\saida.bin"

    with open(arquivo_entrada, "rb") as f:
        dados = f.read()
        
    cipher = Blowfish.new(chave, Blowfish.MODE_ECB)
    dados_preenchidos = pad(dados, Blowfish.block_size)
    dados_cifrados = cipher.encrypt(dados_preenchidos)
    
    with open(arquivo_saida, "wb") as f:
        f.write(dados_cifrados)

    tamanho_original = os.path.getsize(arquivo_entrada)
    tamanho_cifrado = os.path.getsize(arquivo_saida)
    
    print("Tamanho do arquivo original:", tamanho_original, "bytes")
    print("Tamanho do arquivo criptografado:", tamanho_cifrado, "bytes")
    
def descriptografar_arquivo():
    arquivo_entrada = "Atividade3/saida.bin"
    arquivo_saida = "Atividade3/descriptografado.pdf"

    with open(arquivo_entrada, "rb") as f:
        dados_cifrados = f.read()

    cipher = Blowfish.new(chave, Blowfish.MODE_ECB)
    dados_decifrados = cipher.decrypt(dados_cifrados)
    dados_sem_padding = unpad(dados_decifrados, Blowfish.block_size)
    with open(arquivo_saida, "wb") as f:
        f.write(dados_sem_padding)

    print("Arquivo descriptografado salvo como", arquivo_saida)

criptografa("FURB",Blowfish.MODE_ECB) # 1
criptografa("COMPUTADOR",Blowfish.MODE_ECB) #2
criptografa("SABONETE",Blowfish.MODE_ECB) #3
criptografa(bytes([8, 8, 8, 8, 8, 8, 8, 8]),Blowfish.MODE_ECB) #4
criptografa("SABONETESABONETESABONETE",Blowfish.MODE_ECB) #5

cifrado = criptografa("FURB",Blowfish.MODE_CBC) #6
decifrar(cifrado,Blowfish.MODE_CBC,None)

iv = bytes([1, 1, 2, 2, 3, 3, 4, 4])#7
cifrado = criptografa("FURB",Blowfish.MODE_CBC,iv) 
decifrar(cifrado,Blowfish.MODE_CBC,iv)

iv = bytes([1, 1, 2, 2, 3, 3, 4, 4])#8
cifrado = criptografa("SABONETESABONETESABONETE",Blowfish.MODE_CBC,iv) 
decifrar(cifrado,Blowfish.MODE_CBC,iv)

iv = bytes([10,20,30,40,50,60,70,80])#9
cifrado = criptografa("SABONETESABONETESABONETE",Blowfish.MODE_CBC,iv)
iv = bytes([1, 1, 2, 2, 3, 3, 4, 4])
decifrar(cifrado,Blowfish.MODE_CBC,iv)

cifrado = criptografa("SABONETESABONETESABONETE",Blowfish.MODE_ECB) #10
chave = b'11111'
decifrar(cifrado,Blowfish.MODE_ECB)

chave = b'ABCDE'
criptografar_arquivo() #11

descriptografar_arquivo() #12