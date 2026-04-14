# Add Binary
Given two binary strings a and b, return their sum as a binary string.


### Example 1:

    Input: a = "11", b = "1"
    Output: "100"

### Example 2:

    Input: a = "1010", b = "1011"
    Output: "10101"
 

## Constraints:
- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.

----------------------------------------------------------------------------------------------------------------------

# Solution
```Cpp
class Solution {
public:
    string addBinary(string a, string b) {
        string result = "";
        char carry ='0';
        int i = a.size()-1;
        int j = b.size()-1;
        while(i >= 0 && j >= 0){
            if(a[i] == b[j]  && a[i]== '1'){
                if(carry == '1'){
                    result = '1' + result;
                }else{
                    result = '0' + result;
                }
                carry = '1';
            }else if(a[i]==b[j]  && a[i] == '0'){
                if(carry == '1'){
                    result = '1' + result;
                    carry = '0';
                }else{
                    result = "0" + result;
                }
            }else if(a[i] != b[j])
            {
                if(carry == '1'){
                    result = '0' + result;
                    carry = '1';
                }else{
                    result = '1' + result;
                }
            }
            
            if(carry =='1' && (j==0 && i == 0) )
            {
                result = '1' + result;
            }
            i--;
            j--;

        }
        
        while(i >= 0){
            if(carry == '1' && a[i]==carry)
            {
                result = '0' +result;
            }else if(carry == a[i] && carry == '0')
            {
                result = '0' +result;
            }else if(carry != a[i])
            {
                result = '1' +result;
                carry = '0';
            }
            if(i == 0 && carry =='1')
            {
                result = '1' + result;
            }
            i--;
        }
        
        while(j >= 0){
            if(carry == '1' && b[j]==carry)
            {
                result = '0' +result;
            }else if(carry == b[j] && carry == '0')
            {
                result = '0' +result;
            }else if(carry != b[j])
            {
                result = '1' +result;
                carry = '0';
            }
            if(j == 0 && carry =='1')
            {
                result = '1' + result;
            }
            j--;
        }
        return result;
    }
};
```
