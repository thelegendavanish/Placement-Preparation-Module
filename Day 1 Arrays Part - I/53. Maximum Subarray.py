def SubArray(a, s, e):
    if s == e: return a[s]
    maxLeftBorderSum, maxRightBorderSum = -99999999, -9999999
    mid = s + ((e - s) >> 1)

    maxLeftSum = SubArray(a, s, mid)
    maxRightSum = SubArray(a, mid + 1, e)

    # Max Cross Border Sum
    leftBorderSum, rightBorderSum = 0, 0

    for i in range(mid, s-1, -1):
        leftBorderSum += a[i]
        if leftBorderSum > maxLeftBorderSum: maxLeftBorderSum = leftBorderSum

    for i in range(mid + 1, e + 1):
        rightBorderSum += a[i]
        if rightBorderSum > maxRightBorderSum: maxRightBorderSum = rightBorderSum

    crossBorderSum = maxLeftBorderSum + maxRightBorderSum
    return max(maxLeftSum, maxRightSum, crossBorderSum)

class Solution(object):
    def maxSubArray(self, nums):
        return SubArray(nums, 0, len(nums) - 1)