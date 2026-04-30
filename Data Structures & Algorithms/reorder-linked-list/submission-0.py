# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       
        slow = head
        fast = head

        while fast and fast.next: # phase 1, find the midpoint
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while curr: # phase 2: reverse the linked list
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        l1 = head
        l2 = prev

        while l2: # phase 3: merge both lists
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2
        