from utils import AES_SBOX, ROUND_CONSTANT
from Class import Key,Word
 
class KeyManager():
    def __init__(self,key:list[bytes]):
        self.key = key
        
        
    def expand_keys(self) -> list[Key]:
        original_key = self.__get_original_key()
        key_schedule: list[Key] = []

        key_schedule.append(original_key)

        for i in range(1, 11):
            round_key = self.__create_round_key(
                last_round_key=key_schedule[i-1], number=i)
            key_schedule.append(round_key)

        return key_schedule


    def __get_state_matrix(self) -> list[list[int]]:
        matrix = [[self.key[i + j*4] for j in range(4)] for i in range(4)]
        return matrix


    def __get_original_key(self) -> Key:
        state_matrix = self.__get_state_matrix()
        original_key = []

        for c in range(4):
            word = [state_matrix[i][c] for i in range(4)]
            original_key.append(word)

        return original_key


    def __create_round_key(self, last_round_key: Key, number: int) -> Key:
        round_key = []

        first_word = self.__get_round_key_first_word(last_round_key, number)
        round_key.append(first_word)

        for i in range(1, 4):
            prev_word = round_key[i-1]
            last_word = last_round_key[i]
            word = [prev_word[j] ^ last_word[j] for j in range(4)]
            round_key.append(word)

        return round_key


    def __get_round_key_first_word(self, last_round_key: Key, number: int) -> Word:
        last_word = last_round_key[-1]
        first_word = last_round_key[0]
        rotated_word = self.__round_bytes(last_word)
        replaced_word = self.__word_replacement(rotated_word)
        round_constant = self.__get_round_constant(number)
        xor_word = [replaced_word[i] ^ round_constant[i] for i in range(4)]
        final_word = [first_word[i] ^ xor_word[i] for i in range(4)]

        return final_word


    def __word_replacement(self, word: Word) -> Word:
        return [AES_SBOX[b] for b in word]
    
    
    def __round_bytes(self, bytes: Word) -> Word:
        return bytes[1:] + bytes[:1]


    def __get_round_constant(self, number: int) -> Word:
        return [ROUND_CONSTANT[number-1], 0x00, 0x00, 0x00]