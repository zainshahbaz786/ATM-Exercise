import os.path

class user:

    def user_login(user_id, user_pswrd):
        # dir_path = r'Accounts/{}'.format(user_id)
        file_path = r'./Accounts/{}.json'.format(user_id)

        flag = os.path.isfile(file_path)
        if flag:
            print(f'The file {file_path} exists')

            #print(self.pswrd)
        else:
            print(f'The file {file_path} does not exist')
            # you can create it if required



person = user()
user.user_login("111")
