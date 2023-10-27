# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    counter = 1
    slow = head
    fast = head
    # move fast by k steps ahead
    while counter <= k:
        fast = fast.next
        counter += 1
    # if moving fast k ahead gets it to the end then
    # the item to be removed is the head of the linkedlist
    if fast is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    # if not head, then keep moving
    # both slow and fast until fast.next is None,
    # basically you reach the last node
    # since fast was k distance ahead of slow
    # slow.next is what needs to be adjusted
    # slow.next = slow.next.next (dropping slow.next node)
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next