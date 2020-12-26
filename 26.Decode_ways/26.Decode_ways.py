'''
	A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
Example 4:

Input: s = "1"
Output: 1
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).






'''

class Solution:
    def numDecodings(self, s):
        dp = [1, 0, 0]
        for c in s:
            dp_new = [0,0,0]
            dp_new[0]  = (c > '0') * dp[0] + dp[1] + (c <= '6') * dp[2]
            dp_new[1]  = (c == '1') * dp[0]
            dp_new[2]  = (c == '2') * dp[0]
            dp = dp_new
        return dp[0]