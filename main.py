# Atm Exercise to develop all functionalities of ATM Machine including some additonal features
#import os
import json
import os.path
import os
import json
from datetime import datetime


class Admin:
    # def __init__(self):
    #     None
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
                    admin_dict.update({new_admin_name: new_admin_pswrd})
                    print("Admin Add Successfully.")
                    # opt = int(input("Enter the option number: "))

                elif opt == 2:
                    a_id = str(input("Enter the Username of that admin to update its password:"))
                    a_key = str(input("Enter the new Password for this Admin Profile: "))
                    admin_dict[a_id] = a_key
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
                # else:
                #   opt = int(input("Enter the option number: "))


class user:

    def user_login(self,  user_id, user_pswrd):
        # dir_path = r'Accounts/{}'.format(user_id)
        file_path = r'./Accounts/{}.json'.format(user_id)
        # file_name = user_id
        flag = os.path.isfile(file_path)
        if flag:
            print(f'The file {file_path} exists')
            with open(file_path) as json_file:
                data = json.load(json_file)
                json_file.close()
                print(data)
                if data["password"] == user_pswrd:
                    print("Login Successful...")
                    print("\t\t\t MENU")
                    print("1. View Profile \n2.Perform Transaction \n3.Deposit Money\n4.Withdraw Money")
                    print("0. Exit Program")
                    option = 1000
                    while option !=0:
                        option = (int(input("Enter the Option: ")))

                        if option == 1:
                            print("\t\t\tProfile Data\n" , data)
                        elif option == 2:
                            amount = int(input("Enter the Amount you want to transfer: "))
                            if amount <= data["balance"]:
                                real_amount = amount
                                data["balance"] = data["balance"] - amount
                                dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                                # saving the transaction in transactions
                                trans_dict = {
                                    "CNIC": data["cnic"],
                                    "Transaction Amount": real_amount,
                                    "Time": dt_string,
                                    "Remaining": data["balance"]
                                }

                                os.remove(file_path)
                                with open(file_path, 'a') as f:
                                    json.dump(data, f, indent=4)
                                    print("Your Account has been updated again")
                                    json_object = json.dumps(trans_dict, indent=6)
                                    file_a = open("./Accounts/Transactions.json", "w")
                                    # file_a.write(data )
                                    # converting old record again
                                    # file_a.write(str(data))
                                    file_a.write("\n\n")
                                    file_a.write((json_object))

                                    # file_a.write(json_object)
                                    print("Transaction is saved for records.")


                            else:
                                print("Insufficent amount in your account")

                        elif option == 3:
                            amount = int(input("Enter the Amount you want  to deposit: "))
                            data["balance"] += amount
                            print(data)

                        elif option == 4:
                            amount = int(input("Enter the Amount you want  to Withdraw: "))
                            if amount <= data["balance"]:
                                real_amount = amount
                                data["balance"] = data["balance"] - amount
                                print(data)
                        elif option == 0:
                            exit()







            # print(self.pswrd)
        else:
            print(f'The file {file_path} does not exist')
            # you can create it if required





# main file
print("\n\n\n****   ATM MENU   *****")
menu_opt = int(input("1.For Admin Panel \n2.For User Panel \nEnter the Option Number: "))
if menu_opt == 1:
    admin = Admin()
    print("1.Create Customer Profile\n2.View Customer Profile\n3.Access Admin Functionalities\n4.For Exit ")
    #menu_opt = int(input("Enter the option: "))
    menu_opt =1000
    while menu_opt != 4:
        menu_opt = int(input("Enter the option: "))
        if menu_opt == 1:
            admin.set_user_profile()
        elif menu_opt == 2:
            admin.view_user_details()
        elif menu_opt == 3:
            admin.admin_profile()

#person = user()
#person.user_login("111", "1212")














