import json
class Clinique:
    def __init__(self):
        """
        This initial method represents the empty list
        """
        self.list = []
        with open("patients.json") as data:
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

    def add_Patient(self):
        """
        Here the list of data is created
        :return: It returns list
        """

        dt = {
            "name": '',
            "patient_id": '',
            "phone_num": '',
            "Age": '',
            "specilist_Required":''
        }

        try:
            name = input("Enter the Patient Name:").strip()
            if not name.isalpha():
                name = input(" Enter valid Patient Name:").strip()

            patient_id = input("Enter Patient ID:").strip()
            if not patient_id.isnumeric() and len(patient_id) != 6:
                patient_id = input("Enter Patient ID in Numbers:").strip()

            phone_num = input("Enter Phone number:").strip()
            if not phone_num.isnumeric() and len(phone_num) == 10:
                phone_num = input("Enter Valid Phone number:").strip()

            Age = input("Enter Patient Age:").strip()
            if not Age.isnumeric() and len(patient_id) >= 100:
                Age = input("Enter Patient Age in Numbers:").strip()
            specilist_Required = input("Enter specilist_Required:").strip()
            if not name.isalpha():
                specilist_Required = input(" Enter specilist_Required in Alphabets:").strip()




        except ValueError:
            print("You have entered wrong data:")

            # Here all the value is assign to the input
        else:
            dt["name"] = name
            dt["patient_id"] = patient_id
            dt["phone_num"] = phone_num
            dt["Age"] = Age
            dt["specilist_Required"] = specilist_Required
            return dt

    def patient_report(self):
            """
            This function is for writing data in file.
            """
            dt = self.add_Patient()
            self.list.append(dt)

            with open("patients.json", 'w') as data:
                # Here all the data write in the json file
                json.dump(self.list, data, indent=2)
                # It converts python file to json file da
                print("Patient Added")

    def appointment(self):
        print("Searching Patient")
        try:
            name = input("Enter the Patient Name:").strip()
            if not name.isalpha():
                name = input(" Enter valid Patient Name:").strip()

            patient_id = input("Enter Patient ID:").strip()
            if not patient_id.isnumeric() and len(patient_id) != 6:
                patient_id = input("Enter Patient ID in Numbers:").strip()
            specilist_Required = input("Enter specilist_Required:").strip()
            if not name.isalpha():
                specilist_Required = input(" Enter specilist_Required in Alphabets:").strip()
        except ValueError:
            print("You have entered wrong data:")
        else:
            flag = True
            for i in range(len(self.list)):
                try:
                    # checking users first name or last name in file
                    if self.list[i]["name"] == name and self.list[i]["patient_id"] == patient_id and self.list[i]["specilist_Required"] == specilist_Required:

                        flag = False
                        while True:
                            with open("doctors.json","r") as f:
                                self.doctors = json.load(f)
                                for i in range(len(self.doctors)):
                                    if self.doctors[i]["data"]["Specialization"] == specilist_Required:
                                        print("doctor is available")
                                        name = self.doctors[i]["name"]
                                        break
                                    else:
                                        print("doctor is not available")
                                    break

                    else:
                        new_person = {"data": {}}
                        # new_person["data"]["time"] = time
                        # new_person["phone_num"] = phone_num
                        new_person["data"]["name"] = name
                        new_person["data"]["specilist_Required"] = specilist_Required
                        new_person["data"]["with doctor"] = name
                        flag = True
                    # if done then flag will true

                        if flag:
                            self.list.append(new_person)
                            # adding users information in file

                            # save that information
                            print(self.patient_report())
                            # display appointment fixed msg
                            print("your appointment is fixed")
                except ValueError:
                    print("You have entered your data.")
if __name__ == "__main__":
    s = Clinique()
    # s.patient_report()
    s.appointment()










