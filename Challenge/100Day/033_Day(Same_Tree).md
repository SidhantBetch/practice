#  🐦‍🔥 Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

### 🚐 Example 1:

    Tree 1:       Tree 2:
       1            1
      / \          / \
     2   3        2   3
    
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

### 🚐 Example 2:

    Tree 1:       Tree 2:
       1             1
      /               \
     2                 2
    
    Input: p = [1,2], q = [1,null,2]
    Output: false

### 🚐 Example 3:

    Tree 1:       Tree 2:
       1            1
      / \          / \
     2   1        1   2
    
    Input: p = [1,2,1], q = [1,1,2]
    Output: false
 

## 📚 Constraints:
- The number of nodes in both trees is in the range [0, 100].
- -104 <= Node.val <= 104

------------------------------------------------------------------------------------------------------------------

# ⚓ Solution
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        stack = [(p,q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False
            
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True
```
