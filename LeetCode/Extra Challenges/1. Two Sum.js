/* 1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. */
var twoSum = function(nums, target) {
    let indexes = [];
    for(let i = 0; i <= nums.length; i++){
        for(let j = i+1; j <= nums.length; j++){
            if(nums[i] + nums[j] === target){
                indexes.push(i);
                indexes.push(j);
            }
        }
    }
    return indexes;
};
