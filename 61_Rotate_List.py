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
    def rotateList(self, head:Optional[ListNode], k: int ) -> Optional[ListNode]:
        # This method is with use of another data type i.e Array
        # if not head:
        #     return head
        
        # arr = []
        # curr = head
        # while curr:
        #     arr.append(curr.val)
        #     curr = curr.next

        # k = k % len(arr)
        # if k == 0:
        #     return head
        
        # arr = arr[-k:] + arr[:-k]

        # dummy = ListNode()
        # curr = dummy
        
        # for val in arr:
        #     curr.next = ListNode(val)
        #     curr = curr.next
        
        # return dummy.next

        # Without using Arrays
        if not head:
            return head
        
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head
        
        curr = head
        for i in range(length - k -1):
            curr = curr.next

        newHead = curr.next
        curr.next = None
        tail.next = head

        return newHead

s1 = Solution()
list = create_linked_list([1,2,3,4,5])

print("Before Linked-List")
print_list(list)

print("After Linked-List")
k = 2
result = s1.rotateList(list, k)
print_list(result)

