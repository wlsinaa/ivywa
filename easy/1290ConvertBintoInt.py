# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        out_str = str(head.val)
        while head.next != None:
            head = head.next
            out_str += str(head.val)
        print(out_str)
        largest = len(out_str) - 1
        out_int = 0
        for i in out_str:
            out_int += int(i) * 2**(largest)
            largest -= 1
        return out_int