# Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

### Example 1:

<img width="542" height="222" alt="image" src="https://github.com/user-attachments/assets/c4a5e118-b4d1-4512-a8e7-aa56e3c69a5c" />



    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]

### Example 2:

    Input: head = [5], left = 1, right = 1
    Output: [5]
 

## Constraints:
- The number of nodes in the list is n.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

----------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ans = []
        stack = []

        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next
        

        x = left - 1
        y = right - 1
        while x <= y:
            stack[x].val, stack[y].val = stack[y].val, stack[x].val
            x += 1
            y -= 1

        return head
        

```
