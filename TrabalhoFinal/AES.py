from KeyManager import KeyManager
from BlockManager import BlockManager
from Class import Key


class AES():
    def __init__(self, key: list[bytes]):
        self.key = key
        self.key_manager = KeyManager(self.key)
        self.block_manager = BlockManager()

    def encrypt(self, msg: bytes):
        key_schedule = self.key_manager.expand_keys()
        padded = self.block_manager.fill_block(msg)
        blocks = self.block_manager.divide_by_blocks(padded)

    def decrypt(self):
        pass

    def __add_round_key(self, simple_text: list[list[int]], round_key: Key):
        return [simple_text[i] ^ round_key[i] for i in range(4)]


aes = AES(key=b'ABCDEFGHIJKLMNOP')
aes.encrypt(msg=b'DESENVOLVIMENTO!')
