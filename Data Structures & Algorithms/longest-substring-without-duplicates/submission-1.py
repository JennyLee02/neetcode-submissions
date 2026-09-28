class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if r is in seen, its invalid substring -> move l and remove from seen
        longest = 0
        seen = set()
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            # if r is not in seen, its a valid substring -> add to seen and update longest
            w = (r - l) + 1
            longest = max(longest, w)
            seen.add(s[r])
        
        return longest



