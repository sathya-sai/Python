import json

from DataStructure.utility import Stack


class TransactionStack:
    def __init__(self):

        self.stack = Stack()
        with open("Transaction.json") as data:
            try:
                temp = json.load(data)
            except Exception:
                pass
            else:
                for i in temp:
                    self.stack.push(i)

    def transaction_stack(self):
        try:
            transaction = input("Enter transaction amount")
            if not transaction.isnumeric():
                transaction = input("Enter ammount in Rupees")

            customer_name = input("Enter name")
            if not customer_name.isalpha():
                customer_name = input("Enter name in Alphabets")

            company_name = input("Enter company name")
            if not company_name.isalpha():
                company_name = input("Enter company name in Alphabets")

            no_of_share = input("Enter no. of shares")
            if not no_of_share.isnumeric():
                no_of_share = input("Enter no. of shares in numbers")

            cost = input("Enter cost")
            if not cost.isnumeric():
                cost = input("Enter cost in Numbers")

            time = input("Enter time")
            new_transaction = {"transaction": transaction, "customer_name": customer_name, "company_name": company_name,
                               "no_of_share": no_of_share, "cost": cost, "time": time}
            self.stack.push(new_transaction)
        except ValueError:
            print("You have entered wrong data:")

    def save_transaction(self):

        temp1 = []
        size = self.stack.size()
        for i in range(size):
            temp1.append(self.stack.pop())
        with open("Transaction.json", 'w') as data:
            json.dump(temp1, data, indent=2)
            print(temp1)


# Main method
if __name__ == "__main__":
    obj = TransactionStack()
    obj.transaction_stack()
    obj.save_transaction()
