# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    prev = None
    curr = head

    while curr:
        # temporarily holds curr.next
        next = curr.next
        # reverse direction of next pointer
        curr.next = prev

        # move to the next two nodes to swap
        prev = curr
        curr = next

    return prev
