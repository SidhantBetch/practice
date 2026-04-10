# 🔥 Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


### 🔧 Example 1:

    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.


### 🛠️ Example 2:

    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

## 🥦 Constraints:
- 1 <= haystack.length, needle.length <= 104
- haystack and needle consist of only lowercase English characters.

---

# solution
```C++
class Solution {
public:
    int strStr(string haystack, string needle) {
        int i=0;
        int fo = INT_MIN;
        bool isOccurs = false;
        string str = "";
        for(int j=0; j<haystack.size(); j++)
        {
            if(haystack[j] == needle[i] && str != needle)
            {
                i++;
                if(str == "" && !isOccurs )
                    fo = j;
                str +=haystack[j];

                if(str == needle){
                    isOccurs = true;
                    str = "";
                    i = 0;
                }
            }
            else if(str != "" && i != 0){
                i = 0; 
                j = j - (str.size());
                str = "";
            }
            
            
        }
        if(isOccurs){
            return fo;
        }else{
            return -1;
        }
        return{};
    }
};
```

