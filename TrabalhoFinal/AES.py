from KeyManager import KeyManager
from BlockManager import BlockManager
from Class import Key, Matrix
from utils import get_state_matrix, AES_SBOX, AES_INV_SBOX, MULTIPLICATION_MATRIX, MULTIPLICATION_INV_MATRIX


class AES():
    def __init__(self, key: list[bytes]):
        self.key = key
        self.key_manager = KeyManager(self.key)
        self.block_manager = BlockManager()

    def encrypt(self, msg: bytes):
        key_schedule = self.key_manager.expand_keys()
        padded = self.block_manager.fill_block(msg)
        blocks = self.block_manager.divide_by_blocks(padded)
        encrypted_data = b''

        for block in blocks:
            eb = self.__encrypt_block(block, key_schedule)
            encrypted_data += self.__matrix_to_bytes(eb)

        return encrypted_data

    def decrypt(self, msg: bytes):
        key_schedule = self.key_manager.expand_keys()
        blocks = self.block_manager.divide_by_blocks(msg)

        decrypted_data = b''

        for block in blocks:
            eb = self.__decrypt_block(block, key_schedule)
            bytes = self.__matrix_to_bytes(eb)
            decrypted_data += bytes

        return self.block_manager.unfill_block(decrypted_data)

    def __matrix_to_bytes(self, matrix: Matrix) -> bytes:
        return bytes([matrix[row][col] for col in range(4) for row in range(4)])

    def __encrypt_block(self, block: list[int], key_schedule: list[Key]):
        state_matrix = get_state_matrix(block)
        a = self.__add_round_key(state_matrix, key_schedule[0])

        for i in range(1, 10):
            b = self.__sub_bytes(a)
            c = self.__shift_rows(b)
            d = self.__mix_columns(c)
            a = self.__add_round_key(d, key_schedule[i])

        b = self.__sub_bytes(a)
        c = self.__shift_rows(b)

        return self.__add_round_key(c, key_schedule[10])

    def __decrypt_block(self, block: list[int], key_schedule: list[Key]):
        state_matrix = get_state_matrix(block)
        a = self.__add_round_key(state_matrix, key_schedule[10])
        b = self.__shift_rows(a, inverse=True)
        c = self.__sub_bytes(b, inverse=True)

        for i in range(9, 0, -1):
            a = self.__add_round_key(c, key_schedule[i])
            d = self.__mix_columns(a, inverse=True)
            b = self.__shift_rows(d, inverse=True)
            c = self.__sub_bytes(b, inverse=True)

        return self.__add_round_key(c, key_schedule[0])

    def __mix_columns(self, matrix: Matrix, inverse: bool = False) -> Matrix:
        new_state = [[0] * 4 for _ in range(4)]
        multiplication_matrix = MULTIPLICATION_INV_MATRIX if inverse else MULTIPLICATION_MATRIX

        for i in range(4):
            for j in range(4):
                new_state[i][j] = self.__mixColumnOperation(
                    matrix, multiplication_matrix, i, j)

        return new_state

    def __mixColumnOperation(self, matrix: Matrix, multiplication_matrix: Matrix, row: int, col: int) -> int:
        operation_column = [matrix[r][col] for r in range(4)]
        operation_row = [multiplication_matrix[row][c] for c in range(4)]

        return self.__galois_muiltiplication(operation_column, operation_row)

    def __galois_muiltiplication(self, col: list[int], row: list[int]) -> int:
        result = 0
        for i in range(4):
            result ^= self.__gf_mul(row[i], col[i])

        return result

    def __gf_mul(self, a: int, b: int) -> int:
        result = 0
        for _ in range(8):
            if b & 1:
                result ^= a
            hi_bit_set = a & 0x80
            a = (a << 1) & 0xFF
            if hi_bit_set:
                a ^= 0x1B
            b >>= 1
        return result

    def __sub_bytes(self, matrix: Matrix, inverse: bool = False) -> Matrix:
        sbox = AES_INV_SBOX if inverse else AES_SBOX
        return [[sbox[i] for i in linha] for linha in matrix]

    def __shift_rows(self, matrix: Matrix, inverse: bool = False) -> Matrix:
        new_state = [[0] * 4 for _ in range(4)]

        new_state[0] = matrix[0]

        for i in range(1, 4):
            if inverse:
                new_state[i] = matrix[i][-i:] + matrix[i][:-i]
            else:
                new_state[i] = matrix[i][i:] + matrix[i][:i]
        return new_state

    def __add_round_key(self, simple_text: Matrix, round_key: Key) -> Matrix:
        return [[simple_text[row][col] ^ round_key[col][row] for col in range(4)] for row in range(4)]
