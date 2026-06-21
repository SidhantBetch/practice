# Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

### Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

### Example 2:

Input: nums = [0]
Output: [[],[0]]
 

## Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        giveli = sorted(nums)
        ans = []
        ans.append([])

        def backtrack(i, temp):
            nonlocal ans
            if i >= len(giveli):
                return
            
            temp.append(giveli[i])
            if temp not in ans:
                ans.append(temp[:])
        
            backtrack(i+1,temp)
            temp.pop()
            backtrack(i+1, temp)
        
        backtrack(0,[])

        return ans

```
