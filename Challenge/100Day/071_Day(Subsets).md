# Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

### Example 1:
    
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

### Example 2:

    Input: nums = [0]
    Output: [[],[0]]
 

## Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

-----------------------------------------------------------------------------------------------------------------------------

# Solution
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(start, temp):
            nonlocal ans

            ans.append((temp[:]))

            for i in range(start, len(nums)):
                temp.append(nums[i])
                backtrack(i+1,temp)
                temp.pop()

        backtrack(0,[])
        return ans
```
