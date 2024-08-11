# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = llist
        llist = new_node
        return
    current_node = llist
    current_index = 0
    while current_index < (position - 1):
        current_node = current_node.next
        current_index += 1
    new_node.next = current_node.next
    current_node.next = new_node
    return llist