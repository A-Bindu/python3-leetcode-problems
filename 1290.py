# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #head = [1,0,1]
        i = head
        s = ''
        while i!= None:
            s = s+str(i.val)
            i = i.next
        return int(s,2)