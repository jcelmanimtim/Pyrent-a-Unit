from UnitLinkedList.UnitLinkedList import UnitLinkedList
from NodeTemplates.RentedUnitNode import RentedUnitNode
from datetime import datetime as dt


class RentedList(UnitLinkedList):
    """
    Class Template for Rented Unit Linked List
    ...

    Attributes
    ----------
    None
    """

    def __init__(self) -> None:
        super().__init__()

    def insertNode(self, unit, floor, expectedReturn) -> None:
        new_node = RentedUnitNode(floor, unit, expectedReturn)
        a = dt.strptime(expectedReturn, "%Y-%m-%d")

        if self.head is None:
            self.head = new_node
            return
        elif dt.strptime(self.head.expectedReturn, "%Y-%m-%d") >= a:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None and dt.strptime(temp.next.expectedReturn, "%Y-%m-%d") < a:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        return
