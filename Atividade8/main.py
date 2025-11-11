from rsa import ler_chave,cifra_arquivo,decifra_arquivo,salvar_chaves

salvar_chaves()

public_key = ler_chave("mypublickey.pem")
private_key = ler_chave("myprivatekey.pem")

cifra_arquivo(r_path="chave_aes.txt",w_path="chave_aes.bin",public_key=public_key)

decifra_arquivo(r_path="chave_aes.bin",w_path="chave_aes_d.txt",private_key=private_key)

cifra_arquivo(r_path="L08 - Chave assimétrica (novo).pdf",w_path="L08 - Chave assimétrica (novo).bin",public_key=public_key)
decifra_arquivo(r_path="L08 - Chave assimétrica (novo).bin",w_path="L08 - Chave assimétrica2.pdf",private_key=private_key)