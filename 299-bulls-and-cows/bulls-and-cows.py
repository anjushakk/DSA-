from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        count = Counter()

        # First pass: count bulls and build counter for non-bulls
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                count[s] += 1

        # Second pass: count cows using the counter
        for s, g in zip(secret, guess):
            if s != g and count[g] > 0:
                cows += 1
                count[g] -= 1

        return f"{bulls}A{cows}B"
