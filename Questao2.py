from collections import deque

class CercaFerroviaria():
    def __init__(self,trilhas: int):
        self.trilhas = trilhas
        

    def _cria_matriz(self,colunas:int) -> list[list[str]]:
        return [['' for _ in range(colunas)] for _ in range(self.trilhas)]
    
             
    def cifrar(self, texto:str) -> str:
        texto = texto.replace(' ','')
        matriz = self._cria_matriz(len(texto))
        cifra = ""
        
        trilho,direcao = 0,1
        for coluna,char in enumerate(texto):
            matriz[trilho][coluna] = char
            trilho += direcao
            
            if trilho == self.trilhas - 1 or trilho == 0:
                direcao *= -1
        
        for linha in matriz:
            for char in linha:
                cifra += char
                    
        return cifra
    
        
    def decifrar(self,cifra):
        l_cifra = len(cifra)
        matriz = self._cria_matriz(l_cifra)
        decifrado = ""

        trilho,direcao = 0,1
        for coluna in range(l_cifra):
            matriz[trilho][coluna] = '@'
            trilho += direcao
            
            if trilho == self.trilhas - 1 or trilho == 0:
                direcao *= -1
                
        chars = deque(cifra)
        for i in range(self.trilhas):
            for j in range(l_cifra):
                if matriz[i][j] == '@':
                    matriz[i][j] = chars.popleft()
                    
        trilho,direcao = 0,1
        for coluna in range(l_cifra):
            decifrado += matriz[trilho][coluna]
            trilho += direcao
            
            if trilho == self.trilhas - 1 or trilho == 0:
                direcao *= -1
                
        return decifrado




t = CercaFerroviaria(3)
cifrado = t.cifrar("VAMOS INVADIR O SUL AMANHA")
print(cifrado)
decifrado = t.decifrar(cifrado)
print(decifrado)

    
