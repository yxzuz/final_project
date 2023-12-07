from database import Database,Table
# from project_manage import


class Admin:
    def __init__(self,DB):
        self.__DB = DB

    def __delete_user(self,username):
        print(self.__DB)
        for i in range(len(self.__DB.search('login').table)):
            if self.__DB.search('login').table[i]['username'] == username:
                del self.__DB.search('login').table
            return True



    def main(self):
        print('Welcome Admin!')
        print('What do you want to do?')
        # print('add user to database(1)\ndelete user from database(2)\nreset password(3)')
        print('del user')
        username = input('Please enter the username: ')
        self.__delete_user(username)

# class Student:
#     def __init__(self):
#         self.status =  'student'

# m =Admin(DB)
# m.main()
# print(DB.search('login'))