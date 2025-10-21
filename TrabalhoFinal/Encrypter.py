from enum import Enum
from AES import AES
import sys


class Options(Enum):
    KEY = 1
    ENCRYPT = 2
    DECRYPT = 3
    EXIT = 4


class Encrypter:

    def init(self):
        while True:
            option = self.__show_options()

            match option:
                case Options.KEY:
                    self.__set_key()
                case Options.ENCRYPT:
                    self.__encrypt_file()
                case Options.DECRYPT:
                    self.__decrypt_file()
                case Options.EXIT:
                    sys.exit("O programa foi encerrado.")

    def __set_key(self):
        s = input("Digite a Chave:")

        try:
            key = list(map(int, s.split(',')))
            self.aes = AES(bytes(key))
            print("Chave definida com sucesso!")
        except Exception as e:
            print(e)

    def __encrypt_file(self):
        try:
            arquivo_entrada = input("Digite o caminho do arquivo de entrada: ")
            arquivo_saida = input("Digite o nome do arquivo de saída: ")

            with open(arquivo_entrada, "rb") as f:
                dados = f.read()
                
            encrypted = self.aes.encrypt(dados)
            
            with open(arquivo_saida, "wb") as f:
                f.write(encrypted)
        except Exception as e:
            print(e) 
            
    def __decrypt_file(self):
        try:
            arquivo_entrada = input("Digite o caminho do arquivo de entrada: ")
            arquivo_saida = input("Digite o nome do arquivo de saída: ")

            with open(arquivo_entrada, "rb") as f:
                dados = f.read()
                
            decrypted = self.aes.decrypt(dados)
            
            with open(arquivo_saida, "wb") as f:
                f.write(decrypted)
                
        except Exception as e:
            print(e) 
            
    def __show_options(self) -> Options:
        print("Bem-vindo ao cifrador AES, selecione uma opção:")
        print(f'{Options.KEY.value} - Definir Chave')
        print(f'{Options.ENCRYPT.value} - Cifrar Arquivo')
        print(f'{Options.DECRYPT.value} - Decifrar arquivo')
        print(f'{Options.EXIT.value} - Sair')

        i = input("Digite o número da opção: ")

        if not i.isdigit() or int(i) not in [status.value for status in Options]:
            print("Opção inválida.")
            return self.__show_options()

        return Options(int(i))


e = Encrypter()
e.init()
