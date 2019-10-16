import json

class StackAccount:
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

