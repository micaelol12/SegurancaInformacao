from rsa import ler_chave,cifra_arquivo,salvar_chaves

salvar_chaves()

public_key = ler_chave("chave_publica_selmo.pem")
private_key = ler_chave("myprivatekey.pem")

cifra_arquivo(r_path="msg_selmo.txt",w_path="msg_selmo.bin",public_key=public_key)

# decifra_arquivo(r_path="chave_aes.bin",w_path="chave_aes_d.txt",private_key=private_key)

# cifra_arquivo(r_path="L08 - Chave assimétrica (novo).pdf",w_path="L08 - Chave assimétrica (novo).bin",public_key=public_key)
# decifra_arquivo(r_path="L08 - Chave assimétrica (novo).bin",w_path="L08 - Chave assimétrica2.pdf",private_key=private_key)


