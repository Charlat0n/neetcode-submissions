class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = [0] * 26
        t_letters = [0] * 26
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            s_letters[index] = s_letters[index] + 1
        for i in range(len(t)):
            index = ord(t[i]) -  ord('a')
            t_letters[index] = t_letters[index] + 1
        for i in range(26):
            if(s_letters[i] != t_letters[i]):
                return False
        return True