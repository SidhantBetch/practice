# Path Sum II

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

### Example 1:

<img width="592" height="421" alt="image" src="https://github.com/user-attachments/assets/5b341a74-39e5-4652-87f7-8f6558e8fef8" />

    
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

### Example 2:


    Input: root = [1,2,3], targetSum = 5
    Output: []

###Example 3:

    Input: root = [1,2], targetSum = 0
    Output: []
 

## Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

---------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):

        ans = []

        def dfs(node, total, path):

            if node is None:
                return

            path.append(node.val)
            total += node.val

            if node.left is None and node.right is None:
                if total == targetSum:
                    ans.append(path[:])

            dfs(node.left, total, path)
            dfs(node.right, total, path)

            path.pop()      
        dfs(root, 0, [])

        return ans
```
