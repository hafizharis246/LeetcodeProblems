from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for i in values[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    return head

def print_list(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

class Solution:
    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


s1 = Solution()
head = create_linked_list([1,2,3,4,5])
print("Before Reversal:")
print_list(head)

new_node = s1.reverse_linked_list(head)
print("After Reversal")
print_list(new_node)