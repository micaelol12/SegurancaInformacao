class CercaFerroviaria():
    trilhas = 0
    caractere_vazio = ''

    def __init__(self,ptrilhas):
        self.trilhas = ptrilhas

    def criaMatriz(self,colunas):
        return [[self.caractere_vazio for _ in range(colunas)] for _ in range(self.trilhas)]

    def cifrar(self,texto):
        texto = texto.replace(' ','')
        l_texto = len(texto)
        cifra = ""
        matriz = self.criaMatriz(l_texto)
        i = 0
        j = 0
        a = 1

        while i < l_texto:
            matriz[j][i] = texto[i]
            i+=1
            j += a
            
            if j == self.trilhas -1:
                a = -1
            if j == 0:
                a = 1
        
        for i in range(self.trilhas):
            for j in range(l_texto):
                if matriz[i][j] != '':
                    cifra += matriz[i][j]
                    
        return cifra
        
    def decifrar(self,cifra):
        l_texto = len(cifra)
        matriz = self.criaMatriz(l_texto)
        decifrado = ""
        i = 0
        j = 0
        a = 1

        while i < l_texto:
            matriz[j][i] = '@'
            i+=1
            j += a
            
            if j == self.trilhas -1:
                a = -1
            if j == 0:
                a = 1
         
        for i in range(self.trilhas):
            for j in range(l_texto):
                if matriz[i][j] == '@':
                    matriz[i][j] = cifra[0]
                    cifra = cifra[1:]
                
        i = 0
        j = 0
        a = 1
        
        while i < l_texto:
            if matriz[j][i] != '':
                decifrado += matriz[j][i]
                
            i+=1
            j += a
            
            if j == self.trilhas -1:
                a = -1
            if j == 0:
                a = 1
                
        return decifrado




t = CercaFerroviaria(3)
cifrado = t.cifrar("VAMOS INVADIR O SUL AMANHA")
print(cifrado)
decifrado = t.decifrar(cifrado)
print(decifrado)

    
