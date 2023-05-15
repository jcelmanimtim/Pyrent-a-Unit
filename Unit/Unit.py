class Unit:
    """
    Class to represent a Unit Object
    ...

    Attributes
    ----------
    floor(int):
        Represents how many
    unit(str):
        Represents the unit of the condo
    """
    def __init__(self, floor, unit) -> None:
        self.floor = floor
        self.unit = unit
