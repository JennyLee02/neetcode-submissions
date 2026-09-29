class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        longest = 0

        # add to set if not in set
        # if in set, move left by 1, remove from set, check if s[r] in set
        # if not in set, add to set, else:

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, (r-l) + 1)

        return longest

