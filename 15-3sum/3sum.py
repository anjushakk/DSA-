from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: sort the array
        res = []
        n = len(nums)

        for i in range(n):
            # Step 2: skip duplicate elements for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Step 3: skip duplicates for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Step 4: skip duplicates for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1  # need a larger sum
                else:
                    right -= 1  # need a smaller sum

        return res
