# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            zbroj = l1.val + l2.val + carry
            value = zbroj%10
            carry = zbroj//10
            curr.next = ListNode(value)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            zbroj = l1.val + carry
            value = zbroj%10
            carry = zbroj//10    
            curr.next = ListNode(value)
            l1 = l1.next
            curr = curr.next

        while l2:
            zbroj = l2.val + carry
            value = zbroj%10
            carry = zbroj//10    
            curr.next = ListNode(value)
            l2 = l2.next
            curr = curr.next

        if carry != 0:
            curr.next = ListNode(carry)

        return dummy.next
            