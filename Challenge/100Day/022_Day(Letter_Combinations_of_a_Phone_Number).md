# 🎡 Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

### ⚓ Example 1:

    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


### ⚓ Example 2:

    Input: digits = "2"
    Output: ["a","b","c"]
 

### 🍟 Constraints:
- 1 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

-----------------------------------------------------------------------------------------------------------------------

# 🐦‍🔥 Solution
```Cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> ans;
        map<int, string> num;
        int j = 97;

        for(int i = 2; i <= 9; i++) {
            string temp="";
            for(int k=0; k<3; k++){
                temp = temp + (char)j;
                j++; 
            }
            if(i == 7 || i == 9)
            {
                temp = temp + (char)j;
                j++;
            }
            num[i] = temp;
        }
        if(digits.empty()) return ans;

        ans.push_back("");

        for(int i = 0; i < digits.size(); i++) {
            int val = digits[i] - '0';
            if(val == 0 || val == 1) continue;

            vector<string> temp;

            for(string s : ans) {
                for(char c : num[val]) {
                    temp.push_back(s + c);
                }
            }

            ans = temp;
        }
        return ans;

    }
};
```
