# Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

### Example 1:

<img width="782" height="222" alt="image" src="https://github.com/user-attachments/assets/ad1f82d9-3566-4087-901c-f531ad7f2464" />

    Input: head = [1,2,3,3,4,4,5]
    Output: [1,2,5]

### Example 2:

<img width="542" height="222" alt="image" src="https://github.com/user-attachments/assets/ed59b04e-b9e0-47f1-9087-1a6092bac6b3" />


    Input: head = [1,1,1,2,3]
    Output: [2,3]
 

## Constraints:
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.

- --------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                val = curr.val

                while curr and curr.val == val:
                    curr = curr.next

                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next

```
