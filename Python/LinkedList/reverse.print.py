# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reversePrint(llist):
    # Write your code here
    stack = []
    while llist:
        stack.append(llist.data)
        llist = llist.next
    while stack:
        print(stack.pop())