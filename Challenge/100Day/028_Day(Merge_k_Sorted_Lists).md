# 🐦‍🔥 Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

### 🍟 Example 1:

    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6


### 🍟 Example 2:

    Input: lists = []
    Output: []


### 🍟 Example 3:

    Input: lists = [[]]
    Output: []
 

## 🎡 Constraints:
- k == lists.length
- 0 <= k <= 104
- 0 <= lists[i].length <= 500
- -104 <= lists[i][j] <= 104
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 104.

-----------------------------------------------------------------------------------------------------------------

# 🚐 Solution
```Cpp
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        if(lists.empty()) return NULL;

        ListNode* head = lists[0];

        for(int i = 1; i < lists.size(); i++){
            ListNode* Listi = lists[i];

            while(Listi != NULL){
                ListNode* nextNode = Listi->next;  // save next

                // insert Listi into sorted list "head"
                if(head == NULL || Listi->val < head->val){
                    Listi->next = head;
                    head = Listi;
                } else {
                    ListNode* curr = head;

                    // find correct position
                    while(curr->next != NULL && curr->next->val < Listi->val){
                        curr = curr->next;
                    }

                    // insert
                    Listi->next = curr->next;
                    curr->next = Listi;
                }

                Listi = nextNode; // move forward safely
            }
        }
        return head;
    }
};
```
