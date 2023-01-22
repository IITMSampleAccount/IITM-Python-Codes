class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#returns n th node from end of linked list

def getNthNodeFromEnd(head, n):
    dummy = head
    for _ in range(n):
        dummy = dummy.next
    while dummy:
        head = head.next
        dummy = dummy.next
    return head.data
