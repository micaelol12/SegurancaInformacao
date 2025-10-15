from KeyManager import KeyManager
from Class import Key


class AES():
    def __init__(self, key: list[bytes]):
        self.key = key
        self.key_manager = KeyManager(self.key)

    def encrypt(self, msg: bytes):
        key_schedule = self.key_manager.expand_keys()
        padded = self.__fill_block(msg)
        blocks = self.__divide_by_blocks(padded)
        pass

    def decrypt(self):
        pass

    def __divide_by_blocks(self, data: bytes) -> list[list[int]]:
        blocks = []
        for i in range(0, len(data), 16):
            block = list(data[i:i+16])
            blocks.append(block)

        return blocks

    def __fill_block(self, data: bytes) -> bytes:
        pad_len = 16 - (len(data) % 16)

        return data + bytes([pad_len] * pad_len)

    def __unfill_block(self, data: bytes) -> bytes:
        pad_len = data[-1]

        if pad_len < 1 or pad_len > 16:
            raise ValueError("Padding inválido")

        return data[:-pad_len]

    def __add_round_key(self, simple_text: list[list[int]], round_key: Key):
        return [simple_text[i] ^ round_key[i] for i in range(4)]


aes = AES(key=b'ABCDEFGHIJKLMNOP')
aes.encrypt(msg=b'DESENVOLVIMENTO!')
