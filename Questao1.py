
import math

class TransposicaoColunar():
    colunas = 0
    caractere_vazio = 'X'

    def __init__(self,pcolunas):
        self.colunas = pcolunas

    def criaMatriz(self,linhas):
        return [[self.caractere_vazio for _ in range(self.colunas)] for _ in range(linhas)]

    def cifrar(self,texto):
        texto = texto.replace(' ','')
        linhas = math.ceil(len(texto) / self.colunas)
        cifrado = "" 

        matriz = self.criaMatriz(linhas)

        for i in range(linhas):
            for j in range(self.colunas):
                posicao = (self.colunas * i) + j

                if posicao >= len(texto):
                    break

                matriz[i][j] = texto[posicao]

        for j in range(self.colunas):
            for i in range(linhas):
                c = matriz[i][j]
                cifrado += c

        
        return cifrado
        
    def decifrar(self,cifra):
        decifrado = ""
        linhas = int(len(cifra)/self.colunas)
        matriz = self.criaMatriz(linhas)

        for j in range(self.colunas):
            for i in range(linhas):
                posicao = (linhas * j) + i
                matriz[i][j] = cifra[posicao]
        
        for i in range(linhas):
            for j in range(self.colunas):
                decifrado += matriz[i][j]

        return decifrado




t = TransposicaoColunar(7)
cifrado = t.cifrar("VAMOS ATACAR O SUL NO FINAL DESTA SEMANA")
print(cifrado)
decifrado = t.decifrar(cifrado)
print(decifrado)

    

    