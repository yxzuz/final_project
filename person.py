from database import Database,Table
# from project_manage import


class Admin:
    def __init__(self,DB):
        self.__DB = DB

    def __check_user(self,username):
        for i in range(len(self.__DB.search('login').table)):
            if self.__DB.search('login').table[i]['username'] == username:
                return True

    def __delete_user(self,username):
        # print(self.__DB)
        for i in range(len(self.__DB.search('login').table)):
            if self.__DB.search('login').table[i]['username'] == username:
                # print(self.__DB.search('login').table[i])
                del self.__DB.search('login').table[i]
                return True


    def main(self):
        print('Welcome Admin!')
        print('What do you want to do?')
        # print('add user to database(1)\ndelete user from database(2)\nreset password(3)')
        print('del user')
        __confirm_del = int(input('Are you sure that you want to delete this user, yes(1)/no(2)? '))
        if __confirm_del == 1:
            while True:

                username = input('Please enter the username: ')
                if self.__check_user(username):
                    break
                if username == 'Q':
                    break
                print('Invalid username')
                print('Type Q to quit')

            self.__delete_user(username)
            print(self.__DB.search('login').table)


# class Student:
#     def __init__(self):
#         self.status =  'student'

# m =Admin(DB)
# m.main()
# print(DB.search('login'))