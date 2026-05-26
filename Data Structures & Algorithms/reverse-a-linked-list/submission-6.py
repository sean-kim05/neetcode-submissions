# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_value = None
        current_value = head
        while current_value:
            temp = current_value.next
            current_value.next = prev_value
            prev_value= current_value
            current_value = temp
        return prev_value

        