# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        res = ListNode(0)
        curr = res

        while list1 and list2:
            if list1.val <= list2.val:
                tmp = list1.next
                curr.next = list1
                list1 = tmp
                curr = curr.next
            else:
                tmp = list2.next
                curr.next = list2
                list2 = tmp
                curr = curr.next
        curr.next = list1 or list2
        return res.next


