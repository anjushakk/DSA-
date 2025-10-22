class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1] * n  # list of super ugly numbers
        k = len(primes)
        idx = [0] * k   # pointer for each prime

        for i in range(1, n):
            # Next candidates for all primes
            next_vals = [ugly[idx[j]] * primes[j] for j in range(k)]
            next_ugly = min(next_vals)
            ugly[i] = next_ugly

            # Increment indices for all primes that match the min
            for j in range(k):
                if next_ugly == next_vals[j]:
                    idx[j] += 1

        return ugly[-1]
