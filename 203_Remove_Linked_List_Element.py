from typing import Optional

# Define a class to represent a node in the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Assign the value to the node
        self.next = next  # Assign the next node

# Define a class that contains methods to manipulate linked lists
class Solution:
    def removeLinkedListElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to simplify the removal of nodes
        dummy = ListNode(0)
        dummy.next = head  # Point dummy's next to the head of the list
        curr = dummy  # Start with the dummy node
        
        # Traverse the linked list
        while curr.next:
            # If the next node's value is the one we want to remove
            if curr.next.val == val:
                curr.next = curr.next.next  # Bypass the node to remove it
            else:
                curr = curr.next  # Move to the next node
        
        # Return the modified linked list, skipping the dummy node
        return dummy.next

# Helper function to print the linked list in a readable format
def print_linked_list(head: Optional[ListNode]) -> None:

    curr = head  # Start with the head of the list
    while curr:
        # Print the value of the current node followed by an arrow
        print(curr.val, end=" -> ")
        curr = curr.next  # Move to the next node
    print("None")  # Indicate the end of the linked list

# Helper function to create a linked list from a list of values
def create_linked_list(values):

    if not values:
        return None  # Return None if the input list is empty
    
    # Create the head of the linked list
    head = ListNode(values[0])
    curr = head  # Set curr to point to the head
    
    # Iterate over the remaining values to create the linked list
    for value in values[1:]:
        curr.next = ListNode(value)  # Create a new node and link it
        curr = curr.next  # Move curr to the new node
    
    return head  # Return the head of the linked list

# Testing the function
solution = Solution()  # Create an instance of the Solution class

# Create a linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
print("Original linked list:")
print_linked_list(head)  # Print the original linked list

# Remove elements with value 6
new_head = solution.removeLinkedListElements(head, 6)
print("Linked list after removing 6:")
print_linked_list(new_head)  # Print the linked list after removal