import self as self

from OOPS.AddressBook.addressBook import AddressBook


class Address:
    def __init__(self):
        self.obj = AddressBook()
        # creating the object for service class

    def address_book(self):
        try:
            while True:

                print("1.Add Person\n2.Delete Person\n3.Edit Person\n4.Quit")

                choice = int(input("select your choice: "))
                # taking users choice
                if choice == 4:
                    # checking users choice is correct or not
                    # self.obj.Save()
                    print("Exited")
                    return
                elif choice > 4:
                    print("You have selected wrong choice.")
                    continue
                # according to choice calling functions
                choice1 = {1: "people_report", 2: "delete_person", 3: "edit_person"}
                fun = getattr(self.obj, choice1[choice])
                fun()
        except ValueError:
            # exception handling
            print("You have enter wrong input.")
            self.address_book()

        return "done"


if __name__ == "__main__":  # main method

    obj = Address()
    # creating object for address book
    obj.address_book()
