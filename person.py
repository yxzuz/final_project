from database import Database,Table
# from project_manage import
import random,sys

class Admin:
    def __init__(self,DB):
        self.__DB = DB

    def __check_user(self,username):
        for i in range(len(self.__DB.search('login').table)):
            if self.__DB.search('login').table[i]['username'] == username:
                return True



    def __add_user(self):
        print('add user to database')
        print('Generating User\'s id...')
        id = ''
        for _ in range(7):
            id+=str(random.randint(1,9))
        # print(id)
        name = input('Enter user\'s firstname: ').strip()
        last_name = input('Enter user\'s lastname: ').strip()
        print('Generating username...')
        username = name.capitalize() + '.'
        username += last_name[0].capitalize()
        print(username)
        print('Generating password...')
        password = ''
        for _ in range(4):
            password += str(random.randint(1,9))
        # print(password)
        while True:
            role = input('Pick user\'s role, student(1)/faculty(2): ')
            if role in ['1','2']:
                break

            print('Please enter valid choice')
        if role == '1':
            role = 'student'
        elif role == '2':
            role = 'faculty'
        # print(role)
        my_dict = {"ID": id,
                "username": username,
                "password": password,
                "role": role}
        self.__DB.search('login').insert(my_dict)
        # print(self.__DB.search('login'))
        return True

    def __delete_user(self):
        # print(self.__DB)
        print('Delete user from database')
        while True:
            username = input('Please enter the username: ')
            if self.__check_user(username):
                __confirm_del = int(input('Are you sure that you want to delete this user, yes(1)/no(2)? '))
                if __confirm_del == 1:
                    for i in range(len(self.__DB.search('login').table) - 1):
                        if self.__DB.search('login').table[i]['username'] == username:
                            # print(self.__DB.search('login').table[i])
                            del self.__DB.search('login').table[i]
                            return True
                return False
            if username == 'Q':
                break
            print('Invalid username')
            print('Type Q to quit')




    def main(self):
        print('Welcome Admin!')
        print('What do you want to do?')
        print('1.add user to database(1)\n2.delete user from database(2)\n3.reset password(3)')
        x = int(input('Action: '))
        if x == 1:
            self.__add_user()
            print('Adding user was successful')
        elif x == 2:
            # self.__delete_user()
            if self.__delete_user():
                print('Deleting user was successful.')
            else:
                print('No')
            print(self.__DB.search('login').table)









# class Student:
#     def __init__(self):
#         self.status =  'student'

# m =Admin(DB)
# m.main()
# print(DB.search('login'))