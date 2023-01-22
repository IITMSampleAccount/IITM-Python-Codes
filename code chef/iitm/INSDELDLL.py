"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
"""

def insertNode(head, position, value):
    if position == 1:
        new_node = Node(value)
        new_node.next = head
        head.prev = new_node
        head = new_node
        return head
    else:
        current = head
        for i in range(position-2):
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        if new_node.next:
            new_node.next.prev = new_node
        return head
    
def deleteNode(head, position):
    if position == 1:
        head = head.next
        head.prev = None
        return head
    else:
        current = head
        for i in range(position-2):
            current = current.next
        current.next = current.next.next
        if current.next:
            current.next.prev = current
        return head

