import json


class AddressBook:
    def __init__(self):
        """
        This initial method represents the empty list
        """
        self.list = []
        with open("people.json") as data:
            # It access the json file with data
            try:
                data = json.load(data)
                # It converts json file to python file data
                for i in data:
                    # It adds the data to the list one by one
                    self.list.append(i)
            # except IndexError:
            except Exception:
                # Exception is handle here
                print("File is empty")

    def add_Person(self):
        """
        Here the list of data is created
        :return: It returns list
        """

        dt = {
            "first_name": '',
            "last_name": '',
            "address": '',
            "city": '',
            "state": '',
            "zip": '',
            "phone_num": ''

        }

        try:
            first_name = input("Enter the First Name:").strip()
            if not first_name.isalpha():
                first_name = input(" Enter valid First Name:").strip()

            last_name = input("Enter the Last Name: ").strip()
            if not last_name.isalpha():
                last_name = input("Enter valid Last Name: ").strip()
            address = input("Enter the address:").strip()
            if not address.isalpha():
                address = input("Enter valid address:").strip()
            city = input("Enter City:").strip()
            if not city.isalpha():
                city = input("Enter Valid City:").strip()

            state = input("Enter State: ").strip()
            if not state.isalpha():
                state = input("Enter Valid State: ").strip()

            zip = input("Enter Zip:").strip()
            if not zip.isnumeric() and len(zip) != 6:
                zip = input("Enter Zip:").strip()

            phone_num = input("Enter Phone number:").strip()
            if not phone_num.isnumeric() and len(phone_num) == 10:
                phone_num = input("Enter Valid Phone number:").strip()

        except ValueError:
            print("You have entered wrong data:")

            # Here all the value is assign to the input
        else:
            dt["first_name"] = first_name
            dt["last_name"] = last_name
            dt["address"] = address
            dt["city"] = city
            dt["state"] = state
            dt["zip"] = zip
            dt["phone_num"] = phone_num
            return dt
    def people_report(self):
        """
        This function is for writing data in file.
        """
        dt = self.add_Person()
        self.list.append(dt)

        with open("people.json", 'w') as data:
            # Here all the data write in the json file
            json.dump(self.list, data,indent=2)
            # It converts python file to json file da
            print("Person Added")

    def delete_person(self):
        """
        This function is for deleting the person form json file
        :return: It prints the data deleted msg after deleting info.
        """

        # function to remove the particular information
        try:
            first_name = input("Enter the first name:").strip()
            last_name = input("Enter the last name").strip()
            if not first_name.isalpha() and not last_name.isalpha():
                    raise ValueError
        except ValueError:
            print("You have entered data in alphabetic")

        else:
            for i in range(len(self.list)):
                if self.list[i]["first_name"] == first_name and self.list[i]["last_name"] == last_name:
                    # dt = self.delete_person()
                    self.list.remove(self.list[i])
                    with open("people.json", 'w') as data:
                        # Here all the data write in the json file
                        json.dump(self.list, data, indent=2)
                        # It converts python file to json file da

                    # self.Save()
                    print("Data Deleted")
                    break
            else:
                print("Not matching with the data")

    def edit_person(self):
        """
        This function is for edit the data in address book.
        :return: It shows data edited msg after editing
        """

        # function for editing person information

        print("Enter data for editing")
        try:
            first_name = input("Enter first name : ").strip()  # taking user name
            last_name = input("Enter last name : ").strip()
            print(first_name, last_name)
            if not first_name.isalpha() and not last_name.isalpha():
                raise ValueError
        except ValueError:  # exception handling
            print("You have to enter name in alphabet.")
        else:
            flag = True
            for i in range(len(self.list)):
                try:
                    # checking users first name or last name in file
                    if self.list[i]["first_name"] == first_name and self.list[i]["last_name"] == last_name:

                        flag = False
                        while True:
                            choice = int(input(
                                "\t1.First Name\n\t"
                                "2.Last Name\n\t"
                                "3.Address\n\t"
                                "4.City\n\t"
                                "5.State\n\t"
                                "6.Zip Code\n\t"
                                "7.Mobile Number\n\t"
                                "8.Nothing want to change\n\t"
                                "Select choice : "))
                            if choice == 1:  # functions for editing information
                                first = input("Enter first name : ").strip()
                                if not first.isalpha():
                                    print("You have to enter first name in alphabet.")
                                else:
                                    self.list[i]["first_name"] = first_name
                            elif choice == 2:
                                last = input("Enter last name : ").strip()
                                if not last.isalpha():
                                    print("You have to enter last name in alphabet.")
                                else:
                                    self.list[i]["last_name"] = last_name
                            elif choice == 3:
                                address = input("Enter address : ").strip()
                                self.list[i]["address"] = address
                            elif choice == 4:
                                city = input("Enter city : ").strip()
                                if not city.isalpha():
                                    print("You have to enter city in alphabet.")
                                else:
                                    self.list[i]["city"] = city
                            elif choice == 5:
                                state = input("Enter state : ").strip()
                                if not state.isalpha():
                                    print("You have to enter state in alphabet.")
                                else:
                                    self.list[i]["state"] = state
                            elif choice == 6:
                                zip = input("Enter zip code : ").strip()
                                if not zip.isnumeric() and len(zip) != 6:
                                    print("You have to enter zip code in numeric with 6 digit.")
                                else:
                                    self.list[i]["zip"] = zip
                            elif choice == 7:
                                phone_num = input("Enter phone number : ").strip()
                                if not phone_num.isnumeric() and len(phone_num) == 10:
                                    print("You have to enter phone number in numeric with 10 digit.")
                                else:
                                    self.list[i]["phone_number"] = phone_num

                                return

                            else:
                                print("You selected wrong choice.")
                                # self.Save()
                            with open("people.json", 'w') as data:
                                # Here all the data write in the json file
                                json.dump(self.list, data, indent=2)
                            print("data edited")
                            break
                except Exception:
                            print("you have entered wrong name")
            if flag:
                print("Data not available.")
if __name__ == "__main__":
    s = AddressBook()
    s.people_report()




