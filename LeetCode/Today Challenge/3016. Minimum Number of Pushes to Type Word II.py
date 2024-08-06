3016. Minimum Number of Pushes to Type Word II
You are given a string word containing lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. 
For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. 
The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. 
You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.
  
class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        min_pushes = 0

        # Sort the character counts in descending order
        sorted_counts = sorted(count.values(), reverse=True)

        # Calculate the minimum pushes needed by iterating over the sorted counts
        for i, num in enumerate(sorted_counts):
            """ Every 8 characters can be grouped and pushed together,
            so we divide the index by 8 and add 1 to find the number of pushes.
            Multiply by the count of each character to find total pushes """
            min_pushes +=  ((i // 8) + 1) * num
        return min_pushes
