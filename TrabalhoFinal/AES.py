from utils import AES_SBOX

KEY_SIZE = 128
BLOCK_SIZE = 128

Word = list[int]  # 4 bytes como inteiros
Key = list[Word]  # 4 palavras por round key

class AES():
    def __init__(self):
        self.key = b'ABCDEFGHIJKLMNOP'
        self.get_original_key()

    def get_state_matrix(self) -> list[list[int]]:
        matrix = [[self.key[i + j*4] for j in range(4)] for i in range(4)]
        return matrix

    def get_original_key(self) -> Key:
        state_matrix = self.get_state_matrix()
        original_key = []

        for c in range(4):
            word = [state_matrix[i][c] for i in range(4)]
            original_key.append(word)

        return original_key

    def expand_keys(self) -> list[Key]:
        original_key = self.get_original_key()
        key_schedule: list[Key] = []

        key_schedule.append(original_key)

        for i in range(1, 11):
            round_key = self.create_round_key(last_round_key=key_schedule[i-1], number=i)
            key_schedule.append(round_key)

        return key_schedule

    def create_round_key(self, last_round_key: Key, number: int) -> Key:
        round_key = []

        first_word = self.get_round_key_first_word(last_round_key, number)
        round_key.append(first_word)

        for i in range(1, 4):
            prev_word = round_key[i-1]
            last_word = last_round_key[i]
            word = [prev_word[j] ^ last_word[j] for j in range(4)]
            round_key.append(word)

        return round_key

    def get_round_key_first_word(self, last_round_key: Key, number: int) -> Word:
        last_word = last_round_key[-1]
        first_word = last_round_key[0]
        rotated_word = self.round_bytes(last_word)
        replaced_word = self.word_replacement(rotated_word)
        round_constant = self.get_round_constant(number)
        xor_word = [replaced_word[i] ^ round_constant[i] for i in range(4)]
        final_word = [first_word[i] ^ xor_word[i] for i in range(4)]
        
        return final_word

    def word_replacement(self, word: Word) -> Word:
        return [AES_SBOX[b] for b in word]

    def xtime(self, x: int) -> int:
        return ((x << 1) ^ 0x1B) & 0xFF if x & 0x80 else (x << 1)

    def round_bytes(self, bytes: Word) -> Word:
        return bytes[1:] + bytes[:1]

    def get_round_constant(self, number: int) -> Word:
        rcon = 1
        for _ in range(1, number):
            rcon = self.xtime(rcon)
        return [rcon, 0x00, 0x00, 0x00]

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


aes = AES()
