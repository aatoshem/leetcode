# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # we are not starting at slow = fast = head coz we will then
    # immediately hit the while slow != fast condition
    # Hence, we have to start slow = head.next and fast = head.next.next
    slow = head.next
    fast = head.next.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow