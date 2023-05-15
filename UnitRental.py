from Lists.AvailableForRent import AvailableRentList
from Lists.Rented import RentedList
from Lists.InRepair import RepairList
from Interface.Interface import Interface


class UnitRental:
    def __init__(self) -> None:
        self.avRentList = AvailableRentList()
        self.rentedList = RentedList()
        self.repairList = RepairList()
        self.interface = Interface()

    def addNewUnitToAvRentList(self, unitUnit, floor):
        self.avRentList.insertNode(unitUnit, floor)
        return

    def rentFirstAvailableUnit(self, expectedReturnDate) -> None: #5
        first_available_unit = self.avRentList.head
        self.avRentList.deleteNode(first_available_unit.unit)

        self.rentedList.insertNode(first_available_unit.unit, first_available_unit.floor, expectedReturnDate)
        return

    def addReturnedUnitToRenovationList(self, unitUnit, floor) -> None:
        is_valid_input = self.rentedList.searchTree(unitUnit)

        if is_valid_input is not None:
            self.rentedList.deleteNode(unitUnit)
            self.repairList.insertNode(unitUnit, floor)
            print("Unit successfully added to under renovation list!")
        else:
            print("Error: Unit not found in list. Please add first a unit!")
        return

    def transferUnitFromRepairToAvRentList(self, unitUnit) -> None:
        is_valid_input = self.repairList.searchTree(unitUnit)

        if is_valid_input is not None:
            self.repairList.deleteNode(is_valid_input.unit)
            self.avRentList.insertNode(is_valid_input.unit, is_valid_input.floor)
            print("Unit successfully added back to updated for rent-list!")
        else:
            print("Error: Unit not found on list. Please add first a unit!")
        return

    def addReturnedUnitToAvailableList(self, unitUnit, floor) -> None:
        is_valid_input = self.rentedList.searchTree(unitUnit)

        if is_valid_input is not None: #2
            self.rentedList.deleteNode(unitUnit)
            self.avRentList.insertNode(unitUnit, floor)
            print("Unit successfully added back to updated for rent-list!")
        else:
            print("Error: Unit is not on list. Please add first a unit!")
        return

    def printAllLists(self) -> None:
        print('''
        ▄▄▄▄                                                                      ▄▄▄▄   
       █░░░░█                                                                    █░░░░█
██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀██
█  ██╗░░░██╗██████╗░██████╗░░█████╗░████████╗███████╗██████╗░  ██╗░░░░░██╗░██████╗████████╗  █
█  ██║░░░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ██║░░░░░██║██╔════╝╚══██╔══╝  █
█  ██║░░░██║██████╔╝██║░░██║███████║░░░██║░░░█████╗░░██║░░██║  ██║░░░░░██║╚█████╗░░░░██║░░░  █
█  ██║░░░██║██╔═══╝░██║░░██║██╔══██║░░░██║░░░██╔══╝░░██║░░██║  ██║░░░░░██║░╚═══██╗░░░██║░░░  █
█  ╚██████╔╝██║░░░░░██████╔╝██║░░██║░░░██║░░░███████╗██████╔╝  ███████╗██║██████╔╝░░░██║░░░  █ 
█  ░╚═════╝░╚═╝░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░  ╚══════╝╚═╝╚═════╝░░░░╚═╝░░░  █
██▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██''')
        print("""
        
╒═════════════════════════════════════════════════════════════════════════════════════════════╕
||🇺​​​​​🇵​​​​​🇩​​​​​🇦​​​​​🇹​​​​​🇪​​​​​🇩​​​​​ 🇫​​​​​🇴​​​​​🇷​​​​​ 🇷​​​​​🇪​​​​​🇳​​​​​🇹​​​​​ 🇱​​​​​🇮​​​​​🇸​​​​​🇹:​​​​​ 
||═══════════════════════════════════════════════════════════════════════════════════════════||""")
        print("\n")
        self.avRentList.printList()
        print('''
||═══════════════════════════════════════════════════════════════════════════════════════════||
||​​🇴​​​​​🇺​​​​​🇹​​​​​ 🇫​​​​​🇴​​​​​🇷​​​​​ 🇷​​​​​🇪​​​​​🇳​​​​​🇹​​​​​ 🇱​​​​​🇮​​​​​🇸​​​​​🇹:​​​​​ 
||═══════════════════════════════════════════════════════════════════════════════════════════||''')
        print("\n")
        self.rentedList.printList()
        print('''
||═══════════════════════════════════════════════════════════════════════════════════════════||
|| ​​🇺​​​​​🇳​​​​​🇩​​​​​🇪​​​​​🇷​​​​​ 🇷​​​​​🇪​​​​​🇳​​​​​🇴​​​​​🇻​​​​​🇦​​​​​🇹​​​​​🇮​​​​​🇴​​​​​🇳​​​​​ 🇱​​​​​🇮​​​​​🇸​​​​​🇹:​​​​​
||═══════════════════════════════════════════════════════════════════════════════════════════||''')
        print("\n")
        self.repairList.printList()
        print('''
╘═════════════════════════════════════════════════════════════════════════════════════════════╛''')
        return


def main():
    UnitRentalResolver = UnitRental()
    user_input = -1
    while user_input != 7:
        user_input = UnitRentalResolver.interface.getInteger(UnitRentalResolver.interface.printMenu())

        if user_input == 1:
            unit_input = UnitRentalResolver.interface.getUnitInput()
            floor_input = UnitRentalResolver.interface.getFloorInput()
            UnitRentalResolver.addNewUnitToAvRentList(unit_input, floor_input)
            print("Unit successfully added. Check your updated list!")
        elif user_input == 2:
            expectedReturn_input = UnitRentalResolver.interface.getExpectedReturnDate()
            UnitRentalResolver.rentFirstAvailableUnit(expectedReturn_input)
            print("Unit successfully added to out for rent-list!")
            print("\n View your updated list in option #6.")
        elif user_input == 3:
            unit_input = UnitRentalResolver.interface.getUnitInput()
            floor_input = UnitRentalResolver.interface.getFloorInput()
            UnitRentalResolver.addReturnedUnitToRenovationList(unit_input, floor_input)
        elif user_input == 4:
            unit_input = UnitRentalResolver.interface.getUnitInput()
            UnitRentalResolver.transferUnitFromRepairToAvRentList(unit_input)
        elif user_input == 5:
            unit_input = UnitRentalResolver.interface.getUnitInput()
            floor_input = UnitRentalResolver.interface.getFloorInput()
            UnitRentalResolver.addReturnedUnitToAvailableList(unit_input, floor_input)
        elif user_input == 6:
            UnitRentalResolver.printAllLists()
        elif user_input == 7:
            print("Process Finished. Thank you for using our program!")
            pass
        else:
            pass
        print("\n")


main()