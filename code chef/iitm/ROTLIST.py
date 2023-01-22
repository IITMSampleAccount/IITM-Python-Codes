"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def rotateRight(head, R):
    if head is None:
        return None
    if head.next is None:
        return head
    alpha = head
    leng = 0
    while alpha is not None:
        leng += 1
        alpha = alpha.next
    R = R % leng
    if R == 0:
        return head
    alpha = head
    for i in range(leng - R - 1):
        alpha = alpha.next
    newHead = alpha.next
    alpha.next = None
    alpha = newHead
    while alpha.next is not None:
        alpha = alpha.next
    alpha.next = head
    return newHead
