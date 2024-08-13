# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    # Write your code here
    prev = None
    current = llist
    while current:
        node = current.next
        current.next = prev
        
        prev = current
        current = node
    llist = prev
    return llist