
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    carry = 0
    dummy = LinkedList(-1)
    current = dummy

    while linkedListOne or linkedListTwo or carry:
        total_one = linkedListOne.value if linkedListOne else 0
        total_two = linkedListTwo.value if linkedListTwo else 0
        total = total_one + total_two + carry

        value = total % 10
        current.next = LinkedList(value)
        current = current.next

        carry = total // 10

        if linkedListOne:
            linkedListOne = linkedListOne.next

        if linkedListTwo:
            linkedListTwo = linkedListTwo.next

    return dummy.next