class CifraVegenere():
    ALPHABET_SIZE = 26
    ASCII_POSITION = 65

    def __init__(self,chave:str):
        self.chave = chave
        self.chave_s = len(chave)


    def get_char_position_in_realation_to_A(self,c: str) -> int:
        return ord(c) - self.ASCII_POSITION
    

    def get_char(self,c,chave_shift) -> str:
            if c == ' ':
                return c
            else:
                posicao = (self.get_char_position_in_realation_to_A(c) + chave_shift) % self.ALPHABET_SIZE
                return chr(posicao + self.ASCII_POSITION)
            

    def change_chars(self,msg,direction) -> str:
        new_msg = ""

        for i,c in enumerate(msg):
            posicao = i % self.chave_s
            chave_shift = self.get_char_position_in_realation_to_A(self.chave[posicao])
            new_msg += self.get_char(c,chave_shift * direction)

        return new_msg
    
    
    def criptografa(self,msg) -> str:
        return self.change_chars(msg,1)
    

    def descriptograva(self, msg:str)->str:
        return self.change_chars(msg,-1)




t = CifraVegenere("DUH")
cifrado = t.criptografa("THEY DRINK THE TEA")
print(cifrado)
decifrado = t.descriptograva(cifrado)
print(decifrado)