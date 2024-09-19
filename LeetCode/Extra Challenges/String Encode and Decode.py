class Solution:

    def encode(self, strs: List[str]) -> str:
        return ' '.join(f'{len(s)}:{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0

        while i < len(s):
            colon = s.find(':', i)
            length = int(s[i:colon])
            decoded.append(s[colon + 1:colon + 1 + length])
            i = colon + 1 + length
        return decoded
