1460. Make Two Arrays Equal by Reversing Subarrays
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. 
You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.

var canBeEqual = function(target, arr) {
    target.sort();
    arr.sort();
    return target.every((x,i) => x === arr[i]);
};
