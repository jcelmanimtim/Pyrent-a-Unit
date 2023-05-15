from Unit.Unit import Unit


class RentedUnitNode(Unit):
    """
    Class to represent a Unit Node within the Rented linked list, includes expected return date

    ...

    Attributes
    ----------
    floor(int):
        Represents how many
    unit(str):
        Represents the unit of the condo
    next(node):
        The next unit in the list
    expectedReturn(str):
        The expected return date of the car represented as a String in the format "YYMMDD"
    """

    def __init__(self, floor, unit, expectedReturn) -> None:
        super().__init__(floor, unit)
        self.next = None
        self.expectedReturn = expectedReturn
