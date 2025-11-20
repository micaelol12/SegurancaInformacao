from enum import Enum
from AES import AES
import sys


class Options(Enum):
    KEY = (1, "Definir chave", "set_key")
    ENCRYPT = (2, "Criptografar arquivo", "encrypt_file")
    DECRYPT = (3, "Descriptografar arquivo", "decrypt_file")
    OPTIONS = (4, "Mostrar Opções", "show_options")
    EXIT = (5, "Sair do programa", "exit_program")

    def __init__(self, codigo, descricao, metodo):
        self.codigo = codigo
        self.descricao = descricao
        self.metodo = metodo


class Encrypter:

    def __init__(self):
        self.aes = None

    def start(self):
        print("Bem-vindo ao cifrador AES, selecione uma opção:")
        self.show_options()

        while True:
            option = self.__get_option()
            method_name = option.metodo
            method = getattr(self, method_name, None)
            if method:
                method()
            else:
                print(f"Nenhum manipulador encontrado para {option.name}")

    def set_key(self):
        s = input("Digite a Chave:")
        try:
            key = self.__format_key(s)
            self.aes = AES(bytes(key))

            print("Chave definida com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    def encrypt_file(self):
        if not self.__check_key():
            return

        try:
            arquivo_entrada, arquivo_saida = self.__get_arquivos()
            dados = self.__read_file(arquivo_entrada)
            encrypted = self.aes.encrypt(dados)
            self.__write_file(arquivo_saida, encrypted)
            print("Cifrado com sucesso!")
        except Exception as e:
            print(e)

    def decrypt_file(self):
        if not self.__check_key():
            return

        try:
            arquivo_entrada, arquivo_saida = self.__get_arquivos()

            dados = self.__read_file(arquivo_entrada)
            decrypted = self.aes.decrypt(dados)
            self.__write_file(arquivo_saida, decrypted)
            print("Decifrado com sucesso")
        except Exception as e:
            print(e)

    def exit_program(self):
        print("Encerrando o programa...")
        sys.exit(0)

    def __format_key(self, key):
        try:
            return list(map(int, key.split(',')))
        except Exception:
            raise Exception("Ocorreu um erro ao ler a chave")

    def __get_arquivos(self):
        arquivo_entrada = input("Digite o caminho do arquivo de entrada: ")
        arquivo_saida = input("Digite o nome do arquivo de saída: ")

        return (arquivo_entrada, arquivo_saida)

    def __write_file(self, path, data):
        try:
            with open(path, "wb") as f:
                return f.write(data)
        except Exception:
            raise (f"Erro ao gravar o arquivo {path}")

    def __read_file(self, path):
        try:
            with open(path, "rb") as f:
                return f.read()
        except Exception:
            raise (f"Erro ao ler o arquivo {path}")

    def show_options(self):
        for opt in Options:
            codigo, nome, _ = opt.value
            print(f"{codigo} - {nome}")

    def __get_option(self) -> Options:
        i = input("Digite o número da opção: ")
        try:
            codigo = int(i)
        except ValueError:
            print("Por favor, digite um valor numérico.")
            return self.__get_option()

        for opt in Options:
            if opt.codigo == codigo:
                return opt

        print("Opção inválida.")
        return self.__get_option()

    def __check_key(self):
        if self.aes is None:
            print("Defina uma chave antes de criptografar ou descriptografar.")
            return False
        return True


e = Encrypter()
e.start()
