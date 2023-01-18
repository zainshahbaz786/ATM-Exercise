# Atm Exercise to develop all functionalities of ATM Machine including some additonal features
#import os
import json


class Admin:
    def create_user(self, name, cnic, age, pswrd, addr, dep ):
        self.name = name
        self.cnic = cnic
        self.age = age
        self.addr = addr
        self.pswrd = pswrd
        self.dep = dep
        # your cnic is your account number, as to make it unique
        print("Congratulations, Your Account has been created Successfully...")
        print("Your CNIC is you bank Account Number.")
        print("Use your CNIC and Password for Login In Purpose.")
        # now creating a dictionary in the JSON Format.So that to make a file for the user
        directory = f"Accounts/{cnic}.json"

        # making a dictionary, so that to use it in JSON file
        user_dict = {
            "Name": name,
            "CNIC": cnic,
            "AGE": age,
            "Address": addr,
            "Balance": dep,
            "password": pswrd,
        }
        # Serializing json
        json_object = json.dumps(user_dict, indent=4)

        # Writing to sample.json
        file_A = open(directory, "w")
        file_A.write(json_object)

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
        self.create_user(name, c_id, u_age, paswrd, addr, paswrd)













