# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return
        first = ListNode()
        l = first
        while True:
            
            if list1 is None:
                l.next = list2
                break

            if list2 is None:
                l.next = list1
                break

            if list1.val <= list2.val:
                l.next = list1

                list1 = list1.next
            else:
                l.next = list2
                list2 = list2.next
            l = l.next        
        return first.next