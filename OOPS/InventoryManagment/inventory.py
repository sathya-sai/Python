import json


class Inventory:
    def __init__(self):
        """
        This initial method represents the empty list
        """
        self.list = []
        with open("inventory.json") as data:
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

    def add_inventory(self):
        """
        Here the list of data is created
        :return: It returns list
        """

        dt = {
            "name": '',
            "weight": '',
            "price_per_kg": '',


        }

        try:
            name = input("Enter the Inventory Name:").strip()
            if not name.isalpha():
                name = input(" Enter valid Inventory Name:").strip()

            weight = input("Enter the weight: ").strip()
            if not weight.isnumeric():
                weight = input("Enter valid weight: ").strip()
            price_per_kg = input("Enter the price:").strip()
            if not price_per_kg.isnumeric():
                price_per_kg = input("Enter valid price:").strip()


        except ValueError:
            print("You have entered wrong data:")

            # Here all the value is assign to the input
        else:
            dt["name"] = name
            dt["weight"] = weight
            dt["price_per_kg"] = price_per_kg

            return dt
    def inventory_report(self):
        """
        This function is for writing data in file.
        """
        dt = self.add_inventory()
        self.list.append(dt)

        with open("inventory.json", 'w') as data:
            # Here all the data write in the json file
            json.dump(self.list, data, indent=2)
            # It converts python file to json file da
            print("Inventory Added")

    def display(self):
        """
        It displays all file data.
        """
        # It displays all the information
        print("name\t\t\t\tweight\t\t\t\tPer kg\t\t\t\ttotal price")
        for i in self.list:
            print(i["name"], "\t\t\t\t", i["weight"], "\t\t\t\t", i["price_per_kg"],
                  "\t\t\t\t", int(i["weight"]) * int(i["price_per_kg"]))
            print()



if __name__ == "__main__":
    s = Inventory()
    s.inventory_report()
    s.display()

