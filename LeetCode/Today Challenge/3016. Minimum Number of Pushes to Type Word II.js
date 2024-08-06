3016. Minimum Number of Pushes to Type Word II
You are given a string word containing lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

/**
 * @param {string} word
 * @return {number}
 */

var minimumPushes = function(word) {
    const count = Array(26).fill(0);
    let min_pushes = 0;

    // Loop through each character in the word to populate the frequency in the count array
    for(const char of word){
        ++count[char.charCodeAt(0) - 'a'.charCodeAt(0)];
    }

    // Sort the count array in descending order
    count.sort((a,b) => b-a);

    for(let i = 0; i < 26; i++){
        /* The pushes required is determined by the position of the letter
        and its frequency in the word. The position is affected by which
        group of 8 letters it is in, which is calculated by i/8 and rounded down.
        The first group (i/8 = 0) incurs a multiplier of 1, the second a multiplier of 2, etc. */
        min_pushes += (((i / 8) | 0) + 1) * count[i];
    }
    return min_pushes;
};
