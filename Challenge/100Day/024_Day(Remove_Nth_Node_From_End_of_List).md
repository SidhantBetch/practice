# 🐦‍🔥 Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

### 🤦🏻 Example 1:


    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

### 🤦🏻 Example 2:

    Input: head = [1], n = 1
    Output: []

### 🤦🏻 Example 3:

    Input: head = [1,2], n = 1
    Output: [1]
 

## 🕖 Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

-------------------------------------------------------------------------------------------------------------------

# ⚓ Solution
```Cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        vector<ListNode*> st;
        ListNode* curr = head;
        
        while(curr != NULL){
            st.push_back(curr);
            curr = curr->next;
        }
        
        int size = st.size();
        int indx = size - n;
        if(indx == 0){
            return head->next;
        }

        st[indx- 1]->next = (indx+1 < size )?  st[indx + 1] : NULL;
        
        return head;
    }
};
```
