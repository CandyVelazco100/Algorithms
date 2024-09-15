Given a string s and a dictionary of strings wordDict, return true if s 
can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)  # Convertir wordDict en un conjunto para búsquedas rápidas
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Una cadena vacía siempre es válida
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[len(s)]
