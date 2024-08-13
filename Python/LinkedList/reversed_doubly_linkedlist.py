# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):
    # Write your code here
    current = llist
    stack = []
    while current:
        stack.append(current.data)
        current = current.next
        
    current = llist
    while current:
        current.data = stack[-1]
        stack.pop()
        current = current.next
    return llist