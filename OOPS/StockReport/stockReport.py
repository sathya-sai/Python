import json


class StockReport:
    def __init__(self):
        """
        This initial method represents the empty list
        """
        self.list = []
        with open("stock.json") as data:
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

    def new_data(self):
        """
        Here the list of data is created
        :return: It returns list
        """

        dt = {
        "name": '',
        "share_no": '',
        "Share_Price": ''
        }

        try:
            name = input("Enter the company name:").strip()
            share_no = input("Enter the Number of share: ").strip()
            share_price = input("Enter the share price:").strip()

        except ValueError:
            print("You have entered wrong data:")

            # Here all the value is assign to the input
        else:
            dt["name"] = name
            dt["share_no"] = share_no
            dt["Share_Price"] = share_price
            return dt

    # It adds the all new data to the list
    def Stock_report(self):
        """
        This function is for writing data in file.
        """
        dt = self.new_data()
        self.list.append(dt)

        with open("stock.json", 'w') as data:
            # Here all the data write in the json file
            json.dump(self.list, data,indent=2)
            # It converts python file to json file da
            print("Company Added")

    def display(self):
        """
        It displays all file data.
        """
        # It displays all the information
        print("Company name\t\tNo of share\t\tPer share price\t\ttotal price")
        for i in self.list:
            print(i["name"], "\t\t\t\t", i["share_no"], "\t\t\t\t", i["Share_Price"],
                "\t\t\t\t", int(i["share_no"]) * int(i["Share_Price"]))
            print()


if __name__ == "__main__":
    stock = StockReport()
    stock.display()
    stock.Stock_report()
    stock.display()