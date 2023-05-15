from Unit.Unit import Unit
class InStoreUnitNode(Unit):
    """
    Class to represent a Unit Node within the Available For Rent linked list and the Units In Repair Linked List

    ...

    Attributes
    ----------
    floor(int):
        Represents how many 
    unit(str):
        Represents the unit of the condo
    next(node):
        The next unit in the list
    """
    def __init__(self, floor, unit) -> None:
        super().__init__(floor, unit)
        self.next = None
