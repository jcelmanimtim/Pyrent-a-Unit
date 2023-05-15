from UnitLinkedList.UnitLinkedList import UnitLinkedList
from NodeTemplates.InStoreUnitNode import InStoreUnitNode

class AvailableRentList(UnitLinkedList):
    """
    Class Template for Available for Rent Linked List
    ...

    Attributes
    ----------
    None
    """
    def __init__(self) -> None:
        super().__init__()
    
    def insertNode (self, unit, floor) -> None:
        new_node = InStoreUnitNode(floor, unit)
        
        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node
        self.head = self.sortList(self.head)
        return