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
    def addTwoNumbers(self, l1 : Optional[ListNode], l2 : Optional[ListNode]) -> Optional[ListNode]:
        list1 = l1
        list2 = l2
        dummy = ListNode()
        tail = dummy
        sum = 0
        carry = 0

        while list1 or list2 or carry:
            first = list1.val if list1 else 0
            second = list2.val if list2 else 0
            sum = first + second + carry
            carry = sum // 10
            sum = sum % 10
            tail.next = ListNode(sum)
            tail = tail.next

            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None
        return dummy.next
    
s1 = Solution()

l1 = create_linked_list([2,4,3])
l2 = create_linked_list([5,6,4])

result = s1.addTwoNumbers(l1,l2)
print_list(result)

