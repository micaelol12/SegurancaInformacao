KEY_SIZE = 128
BLOCK_SIZE = 128


Word = list[bytes]
Key = list[Word]

class AES():
    def __init__(self):
        self.key = b'ABCDEFGHIJKLMNOP'
        self.get_original_key()


    def get_state_matrix(self) -> list[list[bytes]]:
        matrix = [[self.key[i + j*4] for j in range(4)]for i in range(4)]
        return matrix
    

    def get_original_key(self) -> Key:
        state_matrix = self.get_state_matrix()
        original_key = []

        for c in range(4):
            word = [state_matrix[i][c] for i in range(4)]
            original_key.append(word)

        return original_key


    def expand_keys(self):
        original_key = self.get_original_key()
        key_schedule = []

        key_schedule.append(original_key)

        for i in range(1,11):
            round_key = self.create_round_key(last_round_key=key_schedule[i-1])
            key_schedule.append(round_key)
    

    def create_round_key(self,last_round_key:Key) -> Key:
        round_key = []

        first_word = self.get_round_key_first_word()
        round_key.append(first_word)

        for i in range(1,4):
            word = self.get_round_key_other_words(i)
            round_key.append(word)

        return round_key

    def get_round_key_first_word(self):
        pass

    def get_round_key_other_words(self,i):
        pass

    def divide_by_blocks(self):
        pass

    def fill_block(self):
        pass

    def unfill_block(self):
        pass

    def encrypt_block(self):
        pass

    def decrypt_block(self):
        pass


aes  = AES()