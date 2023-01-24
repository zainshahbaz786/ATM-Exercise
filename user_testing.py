import os.path
import os
import json
from datetime import datetime
class user:


    def obj_to_json(self, dict,fname):
        self.dict = dict
        self.fname = fname

        #converting dict to json
        #file_path = r'./Accounts/{}.json'.format(fname)
        with open(fname, "w") as outfile:
            json.dump(dict, outfile, indent=4)


    def user_login(self,  user_id, user_pswrd):
        # dir_path = r'Accounts/{}'.format(user_id)
        file_path = r'./Accounts/{}.json'.format(user_id)
        # file_name = user_id
        flag = os.path.isfile(file_path)
        if flag:
            # print(f'The file {file_path} exists')
            with open(file_path) as json_file:
                data = json.load(json_file)
                json_file.close()
                # print(data)
                if data["password"] != user_pswrd:
                    print("Incorrect Credentials.")
                elif data["password"] == user_pswrd:
                    print("Login Successful...")
                    print("\t\t\t MENU")
                    print("1. View Profile \n2.Perform Transaction \n3.Deposit Money\n4.Withdraw Money")
                    print("0. Exit Program")
                    option = 1000
                    while option != 0:
                        option = (int(input("Enter the Option: ")))

                        if option == 1:
                            print("\t\t ***- Profile Data -***")
                            # displaying data in better format
                            for key, value in data.items():
                                print(key, ' : ', value)
                        elif option == 2:
                            amount = int(input("Enter the Amount you want to transfer: "))
                            sender_acc = user_id
                            rec_acc = int(input(("Enter the Receiver Account Number: ")))
                            rec_acc = str(rec_acc)

                            try:
                                file_path2 = r'./Accounts/{}.json'.format(rec_acc)
                                flag = os.path.isfile(file_path2)
                                if flag:
                                    with open(file_path2) as json_file:
                                        data2 = json.load(json_file)
                                        json_file.close()
                                        print("xxx")
                                        print(data2)

                            except:
                            # file_name = user_id
                                print("File not found")
                                break
                            else:
                                if amount <= data["balance"]:
                                    real_amount = amount
                                    data["balance"] = data["balance"] - amount
                                    data2["balance"] = data2["balance"] + amount
                                    self.obj_to_json(data, file_path )
                                    self.obj_to_json(data2, file_path2)


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
                                        file_a = open("./Accounts/Transactions.json", "a")
                                        # file_a.write(data )
                                        # converting old record again
                                        # file_a.write(str(data))
                                        file_a.write("\n\n ")
                                        file_a.write((json_object + ","))
                                        file_a.close()
                                        # file_a.write(json_object)
                                        print("Transaction is saved for records.")



                                else:
                                    print("Insufficent amount in your account")

                        elif option == 3:
                            amount = int(input("Enter the Amount you want  to deposit: "))
                            data["balance"] += amount
                            print("Amount has been added to your amount")
                            print("Your New Balance is:")
                            print(data["balance"])
                            self.obj_to_json(data, file_path)
                            # print(data)

                        elif option == 4:
                            amount = int(input("Enter the Amount you want  to Withdraw: "))
                            if amount <= data["balance"]:
                                real_amount = amount
                                data["balance"] = data["balance"] - amount
                                self.obj_to_json(data, file_path)

                                #print(data)
                        elif option == 0:
                            exit()

            # print(self.pswrd)
        else:
            print(f'The file {file_path} does not exist')
            # you can create it if required



person = user()
u_name = str(input("Enter the Username of Customer: "))
u_pass = str(input("Enter the Password of Customer: "))
person.user_login(u_name, u_pass)
