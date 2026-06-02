# 🐦‍🔥 Rotate List

Given the head of a linked list, rotate the list to the right by k places.

 

### 🚐 Example 1:

```text
          1 → 2 → 3 → 4 → 5
rotate 1: 5 → 1 → 2 → 3 → 4
rotate 2: 4 → 5 → 1 → 2 → 3
```

    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]
### 🚐 Example 2:

```txt
          0 → 1 → 2
rotate 1: 2 → 0 → 1
rotate 2: 1 → 2 → 0
rotate 3: 0 → 1 → 2
rotate 4: 2 → 0 → 1
```

    Input: head = [0,1,2], k = 4
    Output: [2,0,1]
 

## 📚 Constraints:
- The number of nodes in the list is in the range [0, 500].
- -100 <= Node.val <= 100
- 0 <= k <= 2 * 109

--------------------------------------------------------------------------------------------------------------------

# ⚓ Solution
```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        temp = head
        length = 0
        stack = []

        while temp:
            stack.append((temp, length))
            temp = temp.next
            length += 1

        k = k % length

        for i in range(k):
            stack[-1][0].next = head
            head = stack[-1][0]

            stack[-2][0].next = None

            stack.pop()

        return head
```
