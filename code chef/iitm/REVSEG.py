"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def reverseSegment(head, L, R):
    if L == R:
        return head
    curr = head
    prev = None
    count = 1
    while count < L:
        prev = curr
        curr = curr.next
        count += 1
    start = prev
    end = curr
    while count <= R:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1
    if start:
        start.next = prev
    else:
        head = prev
    end.next = curr
    return head

