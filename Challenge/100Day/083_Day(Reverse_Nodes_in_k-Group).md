# Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

### Example 1:

<img width="542" height="222" alt="image" src="https://github.com/user-attachments/assets/9e40293b-4767-4b95-bd5b-d38cca3a2f43" />


    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

### Example 2:

<img width="542" height="222" alt="image" src="https://github.com/user-attachments/assets/3e9e9977-4136-4c41-98fc-fcae3943d68c" />


    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
 

## Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

---------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        stack = []
        temp = head
        while temp != None:
            stack.append(temp)
            temp = temp.next
        
        for i in range(0,len(stack),k):
            left = i
            right = i+k-1

            while(left < right and len(stack) > right):
                store = stack[left].val
                stack[left].val = stack[right].val
                stack[right].val = store

                left += 1
                right -=1

        return head

        
```
