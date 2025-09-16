
import math

class TransposicaoColunar():
    def __init__(self,colunas:int):
        self.colunas = colunas

    def _cria_matriz(self,linhas):
        return [['X' for _ in range(self.colunas)] for _ in range(linhas)]
    

    def cifrar(self,texto:str) -> str:
        texto = texto.replace(' ','')
        linhas = math.ceil(len(texto) / self.colunas)
        matriz = self._cria_matriz(linhas)
        cifrado = "" 

        idx = 0
        for i in range(linhas):
            for j in range(self.colunas):
                if idx < len(texto):
                    matriz[i][j] = texto[idx]
                    idx += 1
                
        for j in range(self.colunas):
            for i in range(linhas):
                cifrado += matriz[i][j]

        return cifrado
    
        
    def decifrar(self,cifra:str) -> str:
        linhas = len(cifra) // self.colunas
        matriz = self._cria_matriz(linhas)
        decifrado = ""

        idx = 0
        for j in range(self.colunas):
            for i in range(linhas):
                matriz[i][j] = cifra[idx]
                idx +=1 
                
        for linha in matriz:
            for char in linha:
                decifrado += char

        return decifrado


t = TransposicaoColunar(7)
cifrado = t.cifrar("VAMOS ATACAR O SUL NO FINAL DESTA SEMANA")
print(cifrado)
decifrado = t.decifrar(cifrado)
print(decifrado)

    

    