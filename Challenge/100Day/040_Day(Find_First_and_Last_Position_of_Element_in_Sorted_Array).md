# 🐦‍🔥 Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

### ⚓ Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

### ⚓ Example 2:

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

### ⚓ Example 3:

    Input: nums = [], target = 0
    Output: [-1,-1]
 

## 🍟 Constraints:
- 0 <= nums.length <= 105
- -109 <= nums[i] <= 109
- nums is a non-decreasing array.
- -109 <= target <= 109

-----------------------------------------------------------------------------------------------------------------------

# 🕖 Solution
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                if 0 < mid < len(nums)-1 and nums[mid-1] != target and nums[mid+1] != target:
                    return [mid,mid]
                else:
                    tsi = mid
                    while tsi > 0 and nums[tsi-1] == target:
                        tsi -= 1

                    tei = mid
                    while tei < len(nums)-1 and nums[tei+1] == target:
                        tei += 1

                    return [tsi,tei]
                    
                
            elif nums[mid] < target:
                start = mid+1

            else:
                end = mid-1

        return [-1,-1]
```
