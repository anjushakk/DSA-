from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Step 1: Find the shortest string
        min_len = float("inf")
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
                small = s
        
        # Step 2: Compare characters
        for i in range(min_len):
            char = small[i]
            for s in strs:
                if s[i] != char:
                    return small[:i]
        
        # If we reach here, entire smallest string is common prefix
        return small
