# Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.  

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

    Input: s = "()"
    
    Output: true

Example 2:

    Input: s = "()[]{}"
    
    Output: true

Example 3:

    Input: s = "(]"
    
    Output: false

Example 4:

    Input: s = "([])"
    
    Output: true

Example 5:

    Input: s = "([)]"
    
    Output: false


## Constraints:
1 <= s.length <= 104  
s consists of parentheses only '()[]{}'.


--------------------------------------------------------------------------------------------------------------------------------------

## solution
```C++
class Solution {
public:
    bool isValid(string s) {
        vector<char> num;
        bool start=false;
        for(char c: s)
        {
            if(c=='(' || c=='[' || c=='{')
            {
                num.push_back(c);

            }else if(c==')')
            {
                if(num.empty()) return false;
                char temp = num.back();
                if(temp != '(')
                    return false;
                num.pop_back();
            }else if(c==']' )
            {
                if(num.empty()) return false;
                char temp = num.back();
                
                if(temp != '[')
                    return false;
                num.pop_back();
            }else if(c=='}' )
            {
                if(num.empty()) return false;
                char temp = num.back();
                
                if(temp !='{')
                    return false;
                num.pop_back();
            }else{
                return false;
            }
        }
        if(num.empty())
        {
            return true;
        }
        return {};
    }
};
```
