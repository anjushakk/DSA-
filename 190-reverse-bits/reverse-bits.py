class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Take the last bit of n and add it to result
            result = (result << 1) | (n & 1)
            # Shift n to process the next bit
            n >>= 1
        return result
        