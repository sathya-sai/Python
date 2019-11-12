import json


class Clinicservice:
    def __init__(self):
        """
        This is the constructor which initialise list
        """
        # initializing the empty list
        self.patients = []
        self.doctors = []
        self.file_name = None

        # create method for creating the new address book


    def Open(self):
        """
        This method is for open the json file
        :return: It will open json file
        """
        # function to open file
        file_name = input("Enter the file name")
        try:
            with open(file_name + ".json") as data:
                # opening the json file
                self.patients = json.load(data)
                # load the data from file
                self.file_name = file_name
        except IOError:
            # exception handling
            print("File is not Found.")
        # print(self.patients)
        # displaying the file content

    def Save(self):
        """
        This function is to save data
        :return: It will save data in json file
        """
        try:
            with open(self.file_name + ".json", 'w') as data:
                # opening the file
                data = json.dump(self.patients, data, indent=2)
                # dump all the data into the data
                # self.Save()
                # saving that information
                data.close()
                # closing the file
        except Exception:
            # exception handling
            print("File is saved")

    def Add_appointment(self):
        """
        This method is to add a patient appointment
        :return: It will create appointment
        """
        try:
            first_name = input("Enter the name:")
            # taking users input
            last_name = input("Enter the last name")
            phone_number = int(input("Enter the mobile number"))

            # asking user for which speciality doctors appointment you have
            print(
                "\nIn our hospital 1.heart specialist 2.brain specialist 3.multispecialist 4.Dermatologists 5.Geriatric Medicine Specialists"
                "\nThese doctors are available")
            appointment_reason = input("Enter which speciality doctor's appointment you want: ")

            # time = json.dumps(datetime.datetime.now())
            flag = True

            while flag:
                with open("doctors.json", "r") as f:
                    # loading the file data into doctors data list
                    self.doctors = json.load(f)
                    for i in range(len(self.doctors)):
                        # checking the speciality doctor available in hospital or not
                        if self.doctors[i]["data"]["speciality"] == appointment_reason:
                            print("doctor is available")
                            doctor_name = self.doctors[i]["data"]["doctor name"]
                            break
                        else:
                            print("doctor is not available")
                    break

            # exception handling
        except ValueError:
            print("You have entered wrong data.")

        else:
            new_person = {"data": {}}
            # new_person["data"]["time"] = time
            new_person["data"]["phone_number"] = phone_number
            new_person["data"]["firstname"] = first_name
            new_person["data"]["lastname"] = last_name
            new_person["data"]["appointment_reason"] = appointment_reason
            new_person["data"]["with doctor"] = doctor_name
            flag = True
            # if done then flag will true

            if flag:
                self.patients.append(new_person)
                # adding users information in file
                self.Save()
                # save that information
                print(self.patients)
                # display appointment fixed msg
                print("your appointment is fixed")

    def delete_appointment(self):
        """
        This method is to delete a patient appointment
        :return: It will delete appointment
        """
        # function to remove the particular information
        try:
            first_name = input("Enter the first name:").strip()
            last_name = input("Enter the last name:").strip()
            if not first_name.isalpha() and not last_name.isalpha():
                raise ValueError
        except ValueError:
            print("You have entered data in alphabetic:")

        else:
            for i in range(len(self.patients)):
                if self.patients[i]["data"]["firstname"] == first_name and self.patients[i]["data"][
                                "lastname"] == last_name:
                    self.patients.remove(self.patients[i])
                    self.Save()
                    print("Data Deleted")
                    break


if __name__ == "__main__":
    s = Clinicservice()
    s.Add_appointment()
    s.Open()
    s.Save()
