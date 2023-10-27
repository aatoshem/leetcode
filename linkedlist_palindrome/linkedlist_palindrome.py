# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def linkedListPalindrome(head):
    # Write your code here.
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # when fast reaches the end, slow should be in the middle, since
    # slow moves at x rate and fast at 2x rate.
    reversedSecondHalf = reverseLinkedList(slow)
    firstHalfNode = head

    while reversedSecondHalf:
        if reversedSecondHalf.value != firstHalfNode.value:
            return False
        reversedSecondHalf = reversedSecondHalf.next
        firstHalfNode = firstHalfNode.next

    return True


def reverseLinkedList(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next
    return prev