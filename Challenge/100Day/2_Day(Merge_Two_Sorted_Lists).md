# Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.  
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.  
Return the head of the merged linked list.

Example 1:  
Input: list1 = [1,2,4], list2 = [1,3,4]  
Output: [1,1,2,3,4,4]  


Example 2:  
Input: list1 = [], list2 = []  
Output: []  


Example 3:   
Input: list1 = [], list2 = [0]  
Output: [0]  
 

Constraints:  
The number of nodes in both lists is in the range [0, 50].  
-100 <= Node.val <= 100  
Both list1 and list2 are sorted in non-decreasing order.  

## solution
```C++
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        vector<int> v;

        // Step 1: store values
        while(list1) {
            v.push_back(list1->val);
            list1 = list1->next;
        }

        while(list2) {
            v.push_back(list2->val);
            list2 = list2->next;
        }

        // Step 2: sort
        sort(v.begin(), v.end());

        // Step 3: create new list
        ListNode* dummy = new ListNode(0);
        ListNode* temp = dummy;

        for(int i = 0; i < v.size(); i++) {
            temp->next = new ListNode(v[i]);
            temp = temp->next;
        }

        return dummy->next;
    }
};

```
