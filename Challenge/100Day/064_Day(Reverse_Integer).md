# 🐦‍🔥 Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

### ⚓ Example 1:

    Input: x = 123
    Output: 321

### 🚐 Example 2:

    Input: x = -123
    Output: -321

### 🎡 Example 3:

    Input: x = 120
    Output: 21
 

## 🤦🏻 Constraints:
- -231 <= x <= 231 - 1

-------------------------------------------------------------------------------------------------------------------

# 🍟 Solution
```python
class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        ans = 0

        while num > 0:
            temp = num % 10
            ans = ans * 10 + temp
            num //= 10

        if x < 0:
            ans = -ans

        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans
```
