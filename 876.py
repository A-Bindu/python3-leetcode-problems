# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #head = [1,2,3,4,5]
        first = head
        last = head
        while first and first.next:
                first = first.next.next
                last = last.next
        return last
