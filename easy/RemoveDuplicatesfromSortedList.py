# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        dummy = curr = ListNode(None)
        while head:
            print(head.val,curr.val)
            if head.val != curr.val:
                curr.next = head
                curr = curr.next
            head = head.next
        if curr.next != None:
            if curr.val == curr.next.val:
                curr.next = None
        return dummy.next