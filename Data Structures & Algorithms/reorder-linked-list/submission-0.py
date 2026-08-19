# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_part = slow.next
        # ovo radimo da odvojimo array
        slow.next = None
        prev = None
        while second_part:
            sljedeci = second_part.next
            second_part.next = prev
            prev = second_part
            second_part = sljedeci
        
        second = prev
        first = head

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2