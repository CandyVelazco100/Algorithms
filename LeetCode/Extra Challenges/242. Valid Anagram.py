Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

class Solution:
    def sortString(self, text: str) -> str:
        return ''.join(sorted(text))

    def isAnagram(self, s: str, t: str) -> bool:
        return self.sortString(s) == self.sortString(t)
