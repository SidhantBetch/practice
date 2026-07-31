# Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

### Example 1:

<img width="531" height="171" alt="image" src="https://github.com/user-attachments/assets/205cc313-6b7e-45fd-b2c4-d5676597111e" />


    Input: head = [3,2,0,-4], pos = 1
    Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

### Example 2:

<img width="201" height="105" alt="image" src="https://github.com/user-attachments/assets/7420ed26-4143-43f6-a2f8-a4100186a2b7" />


    Input: head = [1,2], pos = 0
    Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

### Example 3:

<img width="65" height="65" alt="image" src="https://github.com/user-attachments/assets/bcc58486-2333-46b1-b7a1-8d1ddb307f7b" />


    Input: head = [1], pos = -1
    Output: false
Explanation: There is no cycle in the linked list.
 

## Constraints:
- The number of the nodes in the list is in the range [0, 104].
- -105 <= Node.val <= 105
- pos is -1 or a valid index in the linked-list.

--------------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        stack = []

        temp = head

        while temp:
            if temp in stack:
                return True

            stack.append(temp)
            temp = temp.next  

        return False  
        

```
