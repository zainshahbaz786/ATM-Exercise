# Atm Exercise to develop all functionalities of ATM Machine including some additonal features
import json


class Admin:

    def create_user(self, name, cnic, age, pswrd, addr, dep):

        # your cnic is your account number, as to make it unique
        print("Congratulations, Your Account has been created Successfully...")
        print("Your CNIC is you bank Account Number.")
        print("Use your CNIC and Password for Login In Purpose.")
        # now creating a dictionary in the JSON Format.So that to make a file for the user
        directory = f"Accounts/{cnic}.json"

        # making a dictionary, so that to use it in JSON file
        user_dict = {
            "name": name,
            "cnic": cnic,
            "age":  age,
            "address": addr,
            "balance": dep,
            "password": pswrd,
        }
        # Serializing json
        json_object = json.dumps(user_dict, indent=4)

        # Writing to sample.json
        file_a = open(directory, "w")
        file_a.write(json_object)

    def set_user_profile(self):
        name = str(input("Enter your Full Name: "))
        c_id = str(input("Enter your CNIC: "))
        u_age = int(input("Enter your Age: "))
        addr = str(input("Enter your Permanent address: "))

        dummy_p1 = str(input("Enter the Password for your account carefully: "))
        dummy_p2 = str(input("Enter the Password  Again : "))
        while dummy_p1 != dummy_p2:
            print("Both Passwords arent same.Please Enter Again ")
            dummy_p1 = str(input("Enter the Password for your account carefully: "))
            dummy_p2 = str(input("Enter the Password  Again : "))
        paswrd = dummy_p1
        print("If you want to deposit any amount Now, Then Enter Amount otherwise Enter zero.")
        deposit = int(input("Enter the Amount: "))
        #self.create_user(name, c_id, u_age, paswrd, addr, deposit)
        self.create_user(name, c_id, u_age, paswrd, addr, deposit)

    @staticmethod
    def view_user_details(self):
        dummy = str(input("Enter the CNIC OF User to view his Account Details: "))
        file_name = "Accounts/{}.json".format(dummy)
        with open(file_name, 'r') as f2:
            data = f2.read()
            print(data)
    def admin_profile(self):
        admin_dict = {
            "admin": "admin123"
        }
        print("\tPlease Enter the credentials to Access Admin Panel.")
        a_id = str(input("Enter the Administrative Username: "))
        a_key = str(input("Enter the Administrative Password: "))
        if a_id in admin_dict and a_key == admin_dict[a_id]:
            print("Login Successfully...")
            print("Choose the Option Carefully.")
            print("1. Create new Admin Profile \n2. Update admin Profile \n3.Delete Admin Profile \n 4.View Admins")
            print("5.Exit")
            opt = 1000

            while opt != 0:
                opt = int(input("Enter the option number: "))
                if opt == 1:
                    new_admin_name = str(input("Enter the Username: "))
                    new_admin_pswrd = str(input("Enter the Password: "))
                    admin_dict.update({new_admin_name : new_admin_pswrd})
                    print("Admin Add Successfully.")
                    #opt = int(input("Enter the option number: "))

                elif opt == 2:
                    a_id=str(input("Enter the Username of that admin to update its password:"))
                    a_key=str(input("Enter the new Password for this Admin Profile: "))
                    admin_dict[a_id]=a_key
                    print("Password of Admin {} updated successfully. ".format(a_id))
                elif opt == 3:
                    a_id = str(input("Enter the Username of the admin you want to delete:"))
                    if a_id in admin_dict:
                        del admin_dict[a_id]
                        print("{} profile deleted successfully.".format(a_id))
                    else:
                        print("{} is not an Admin".format(a_id))
                        pass

                elif opt == 4:
                    print(admin_dict)

                elif opt == 5:
                    exit()
                #else:
                 #   opt = int(input("Enter the option number: "))





obj = Admin()
#obj.set_user_profile()
#obj.view_user_details()
obj.admin_profile()










