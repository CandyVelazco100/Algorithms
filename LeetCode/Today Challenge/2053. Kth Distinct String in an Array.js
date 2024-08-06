2053. Kth Distinct String in an Array
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. 
If there are fewer than k distinct strings, return an empty string "".

/**
 * @param {string[]} arr
 * @param {number} k
 * @return {string}
 */
var kthDistinct = function(arr, k) {
    const frequencyMap = {};

    // Count the frequency of each string in the array.
    for(const i of arr){
        frequencyMap[i] = (frequencyMap[i] || 0) + 1;
    }

    // Iterate through the array to find the k-th distinct string.
    for(const i of arr){
        if(frequencyMap[i] === 1){
            // Decrement k and check if we have found the k-th distinct string.
            k --;
            if(k===0){
                return i;
            }
        }
    }
    // If the k-th distinct string is not found, return an empty string.
    return "";
};
