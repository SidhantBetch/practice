# Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

### Example 1:


<img width="662" height="222" alt="image" src="https://github.com/user-attachments/assets/223faf0a-9e6d-43e8-8af6-ab9a41b7c148" />


    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]

### Example 2:

    Input: head = [2,1], x = 2
    Output: [1,2]
 

## Constraints:
- The number of nodes in the list is in the range [0, 200].
- -100 <= Node.val <= 100
- -200 <= x <= 200

---------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        small_dummy = ListNode(0)
        large_dummy = ListNode(0)

        small = small_dummy
        large = large_dummy

        curr = head

        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                large.next = curr
                large = large.next

            curr = curr.next

        large.next = None
        small.next = large_dummy.next

        return small_dummy.next
```
