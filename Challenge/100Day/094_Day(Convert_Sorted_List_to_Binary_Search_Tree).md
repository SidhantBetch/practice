# Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

### Example 1:

<img width="724" height="562" alt="image" src="https://github.com/user-attachments/assets/5b13112e-d462-4872-83fb-d639737e817c" />


    Input: head = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

### Example 2:

    Input: head = []
    Output: []
 

## Constraints:
- The number of nodes in head is in the range [0, 2 * 104].
- -105 <= Node.val <= 105

-----------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        nums = []

        while head:
            nums.append(head.val)
            head = head.next
        
        def BST(left, right):
            if left > right:
                return

            mid = (left + right)//2

            root = TreeNode(nums[mid])

            root.left = BST(left,mid-1)
            root.right = BST(mid+1, right)

            return root
        
        return BST(0, len(nums)-1)

```
