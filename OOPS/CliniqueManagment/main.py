from OOPS.CliniqueManagment.clinique import Clinicservice


class Clinic_Management:
    def __init__(self):
        self.obj = Clinicservice()

    def Clinic_Management(self):
        try:
            while True:

                print("1.Add appointment\n2.Delete appointment\n3.open\n4.save\n5.quit")
                self.obj.Open()
                                                                                                                                                                                                            # opening the file

                choice = int(input("select your choice: "))
                if choice == 5:
                    self.obj.Save()
                    print("Exited")
                    return
                elif choice > 5:
                    print("You have selected wrong choice.")
                    continue
                choice1 = {1: "Add_appointment", 2: "delete_appointment", 3: "Open", 4: "save"}
                fun = getattr(self.obj, choice1[choice])
                fun()
        except ValueError:
                print("You have enter wrong input.")
                self.Clinic_Management()
                return "done"


if __name__ == "__main__":

    obj = Clinic_Management()
    obj.Clinic_Management()