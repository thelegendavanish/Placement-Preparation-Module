class Solution:
    def maxLen(self, n, arr):
        #Code here
        m= {}
        sum=0
        ans=0
        for i in range(n):
            sum+=arr[i]
            if sum==0:
                ans = max(ans, i+1)
            elif sum in m:
                ans = max(ans, i-m[sum])
            else:
                m[sum] = i
        return ans
