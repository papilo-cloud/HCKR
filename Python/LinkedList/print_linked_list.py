# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    current_node = head
    while current_node:
        print(current_node.data)
        current_node = current_node.next