from KeyManager import KeyManager

class AES():
    def __init__(self):
        self.key = b'ABCDEFGHIJKLMNOP'
        self.key_manager = KeyManager(self.key)
        self.key_schedule = self.key_manager.expand_keys()
        
        print(self.key_schedule)

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
