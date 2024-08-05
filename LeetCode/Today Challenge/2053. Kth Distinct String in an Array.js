2053. Kth Distinct String in an Array
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. 
If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

/**
 * @param {string[]} arr
 * @param {number} k
 * @return {string}
 */
var kthDistinct = function(arr, k) {
    const frequencyMap = {};

    for(const i of arr){
        frequencyMap[i] = (frequencyMap[i] || 0) + 1;
    }

    for(const i of arr){
        if(frequencyMap[i] === 1){
            k --;
            if(k===0){
                return i;
            }
        }
    }
    return "";
};
