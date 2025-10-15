class BlockManager():
    def divide_by_blocks(self, data: bytes) -> list[list[int]]:
        blocks = []
        for i in range(0, len(data), 16):
            block = list(data[i:i+16])
            blocks.append(block)

        return blocks

    def fill_block(self, data: bytes) -> bytes:
        pad_len = 16 - (len(data) % 16)

        return data + bytes([pad_len] * pad_len)

    def unfill_block(self, data: bytes) -> bytes:
        pad_len = data[-1]

        if pad_len < 1 or pad_len > 16:
            raise ValueError("Padding inválido")