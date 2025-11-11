from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def salvar_chave(path, key):
    with open(path, "wb") as f:
        data = key.export_key()
        f.write(data)

def ler_chave(path):
    with open(path, "rb") as f:
        data = f.read()
        mykey = RSA.import_key(data)

    return mykey

def salvar_chaves():
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    salvar_chave("myprivatekey.pem",private_key)
    salvar_chave("mypublickey.pem",public_key)

def cifra_msg(data_to_encrypt:bytes,public_key):
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted = cipher_rsa.encrypt(data_to_encrypt)

    return encrypted

def decifra_msg(encrypted:bytes,private_key):
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted = cipher_rsa.decrypt(encrypted)

    return decrypted

def cifra_arquivo(r_path,w_path,public_key):
    dados = read_file(r_path)
    data = cifra_msg(dados,public_key)
    write_file(w_path,data)

def decifra_arquivo(r_path,w_path,private_key):
    dados = read_file(r_path)
    data = decifra_msg(dados,private_key)
    write_file(w_path,data)

def write_file(path, data):
        try:
            with open(path, "wb") as f:
                return f.write(data)
        except Exception:
            raise (f"Erro ao gravar o arquivo {path}")

def read_file(path):
        try:
            with open(path, "rb") as f:
                return f.read()
        except Exception:
            raise (f"Erro ao ler o arquivo {path}")