# Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

### Example 1:

    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]

### Example 2:

    Input: s = "a"
    Output: [["a"]]
 

## Constraints:
- 1 <= s.length <= 16
- s contains only lowercase English letters.

-----------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
class Solution:
    def partition(self, s: str):

        ans = []

        def palindrome(left, right):

            while left < right:

                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True


        def backtrack(index, path):

            if index == len(s):
                ans.append(path[:])
                return


            for end in range(index, len(s)):

                if palindrome(index, end):

                    path.append(s[index:end+1])

                    backtrack(end+1, path)

                    path.pop()


        backtrack(0, [])

        return ans
```
