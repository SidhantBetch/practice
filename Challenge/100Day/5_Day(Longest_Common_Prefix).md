# Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.  

If there is no common prefix, return an empty string "".

 
### Example 1:
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

### Example 2:
```
Input: strs = ["dog","racecar","car"]
Output: ""
```
Explanation: There is no common prefix among the input strings.  


## Constraints:
1 <= strs.length <= 200  
0 <= strs[i].length <= 200  
strs[i] consists of only lowercase English letters if it is non-empty.  

----------------------------------------------------------------------------------------------------------------------------------

# Solution
```Cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string s="";
        bool flag = false;
        for(int j=0; j<strs[0].length(); j++)
        {
            for(int k=0; k < strs.size()-1; k++)
            {
                if(strs[k][j]==strs[k+1][j]){
                    flag = true;
                }else{
                    flag = false;
                    break;
                }
            }
            if(flag == true){
                s +=strs[0][j];
            }else{
                break;
            }
        }
            
        if(strs.size() == 1){
            return strs[0];
        }else{
            return s;
        }
        
    }
};
```
