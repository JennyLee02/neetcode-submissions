class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers?
        s = "".join(char.lower() for char in s if char.isalnum())
        ptr_1 = 0
        ptr_2 = len(s) - 1

        while ptr_1 < ptr_2:
            if s[ptr_1] != s[ptr_2]:
                return False
            ptr_1 += 1
            ptr_2 -= 1
        
        return True