class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==1:
            return 10
        if n>10:
            n=10
        count=1
        product=9
        for k in range(1,n+1):
            if k==1:
                count+=9
            else:
                product*=(10-(k-1))
                count+=product
        return count
