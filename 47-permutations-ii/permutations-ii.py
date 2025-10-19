class Solution(object):
    def permuteUnique(self, nums):
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return

            seen = set()  # track used elements at this level
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue  # skip duplicates at current recursion level
                seen.add(nums[i])

                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack

        res = []
        nums.sort()
        backtrack(0)
        return res
