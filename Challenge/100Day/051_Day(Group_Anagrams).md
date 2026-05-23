# 🕖 Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

### ⚓ Example 1:

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

### ⚓ Example 2:

    Input: strs = [""]
    
    Output: [[""]]

### ⚓ Example 3:

    Input: strs = ["a"]
    
    Output: [["a"]]

 

## 🚐 Constraints:
- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

-----------------------------------------------------------------------------------------------------

# 🤦🏻 Solution
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = []

        sorted_words = []

        for s in strs:
            sorted_words.append(sorted(s))

        for i in range(len(strs)):

            if strs[i] is None:
                continue

            temp = []
            temp.append(strs[i])

            for j in range(i + 1, len(strs)):

                if strs[j] is None:
                    continue

                if sorted_words[i] == sorted_words[j]:

                    temp.append(strs[j])
                    strs[j] = None

            ans.append(temp[:])

        return ans
```
