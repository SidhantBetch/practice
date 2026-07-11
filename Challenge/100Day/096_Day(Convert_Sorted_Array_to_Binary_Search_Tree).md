# Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

### Example 1:

<img width="302" height="222" alt="image" src="https://github.com/user-attachments/assets/1827f265-0f57-4bbb-9d0f-fe9526b5d52d" />


    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

### Example 2:

<img width="302" height="222" alt="image" src="https://github.com/user-attachments/assets/366ec49e-1437-41bc-826d-2c657a343c32" />


    Input: nums = [1,3]
    Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

## Constraints:
- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in a strictly increasing order.

----------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)
```
