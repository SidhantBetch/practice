# Problem Statement
The royal family exchanges gifts at Christmas, where the youngest member receives gifts from everyone but doesn't give any gifts. Given the data for all the exchanged gifts among the family members, you need to identify the youngest member, who is the one receiving gifts from everyone but not giving any.  
Note: A family member does not give more than one gift to the same member.

## Input Format
```
The first line of the input contains two integers n and m denoting the number of family members
and the number of gifts that were exchanged.

The next m lines contain two integers each. In the ith line, two integers ai, bi represent that
 a gift was given by ai to bi.
```

## Output Format
```
Print a single integer, the number that represents the youngest member of the family.

If no such member is found, print “-1” instead.
```

## Constraints
```
1 <= n <= 104

0 <= m <= 105

1 <= ai, bi, <= n
```

## Sample Testcase 0

### Testcase Input
```
2 1
1 2
```
### Testcase Output
```
2
```
### Explanation
Family member 1 gave a gift to family member 2. Now, we can see that 2 did not give any gift to anyone but received a gift from all other members (member 1). Hence, 2 is the youngest member.
Sample Testcase 1


### Testcase Input
```
3 2
1 3
2 3
```
### Testcase Output
```
3
```
### Explanation
We can see that 3 received gifts from 1 and 2 but did not give any gifts to anyone. Therefore, 3 must be the youngest member.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```C++
#include <iostream>
#include <map>
using namespace std;

void find_youngest_member(int n, int m, int gifts[][2]) {
    if(n<1 || n>=10000 || m<0 || m>100000)
    {
        cout<<-1;
    }else{
            
        map<int, bool> rec;
        for(int i=1; i<=n; i++)
        {
            rec[i] = false;
        }
        for(int j=0; j<m; j++)
        {
            rec[gifts[j][0]] = true;
        }
        
        bool flag = false;
        int count = 0;
        int ans;
        for (auto it : rec) {
            if (it.second == false) {
                flag = true;
                count++;
                ans = it.first;
            }
        }
        if(flag && count == 1){
            cout<< ans;
        }else{
            cout<< -1;
        }
    }
    
        
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int gifts[m][2];
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &gifts[i][0], &gifts[i][1]);
    }

    find_youngest_member(n, m, gifts);
    return 0;
}
```
