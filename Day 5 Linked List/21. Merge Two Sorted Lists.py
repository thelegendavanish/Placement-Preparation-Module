# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        if left == 0: return right
        if right == 0: return left

        ans = ListNode(-1)
        mptr = ans

        while left and right:
            if left.val <= right.val:
                mptr.next = left
                mptr = left
                left = left.next
            else:
                mptr.next = right
                mptr = right
                right = right.next

        if left:
            mptr.next = left
            # mptr = left
            # left = left.next

        if right:
            mptr.next = right
            # mptr = right
            # right = right.next

        return ans.next