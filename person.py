import copy
import sys

from database import Database, Table
# from project_manage import
import random


def _check_input(input_choices, txt, wrong_input_txt=''):
    while True:
        x = input(txt)
        if x in input_choices:
            break
        print(wrong_input_txt)
    return x


def _check_input_v2(input_choices, txt):
    x = ''
    while x != 'Q':
        print('Type Q to quit')
        x = input(txt)

        if x in input_choices:
            break
        if x != 'Q':
            print('Please enter a valid choice.')
    return x


def _generate_thing(len_thing, lower_bound, upper_bound):
    thing = ''
    for _ in range(len_thing):
        thing += str(random.randint(lower_bound, upper_bound))
    return thing


class Admin:
    def __init__(self, db):
        self.__db = db

    def __check_user(self, username):
        # check whether the username existed
        if len(self.__db.search('login').filter(lambda x: x['username'] == username).table) != 0:
            return True
        return False

    def reset_password(self, user):
        if self.__check_user(user):
            password = _generate_thing(4, 1, 9)
            # print(self.__db.search('login'))
            filtered = self.__db.search('login').filter(lambda x: x['username'] == user)
            filtered.update('password', password)
            self.__db.search('joined_person_login').filter(lambda x: x['username'] == user).update('password', password)
            # print(self.__db.search('login'))
            print('Reset password was successful')
        else:
            print('Invalid username')
            print('Type Q to quit')

    def add_new_user(self):
        _id = _generate_thing(7, 1, 9)
        name = input('Enter user\'s firstname: ').strip()  # NO space pls
        last_name = input('Enter user\'s lastname: ').strip().capitalize()
        print('Generating username...')
        username = name.capitalize() + '.'
        username += last_name[0].capitalize()
        # print(username)
        print('Generating password...')
        password = _generate_thing(4, 1, 9)
        role = _check_input(['1', '2'], 'Pick user\'s role, student(1)/faculty(2): ', 'Please enter valid choice')
        if role == '1':
            role = 'student'
        elif role == '2':
            role = 'faculty'
        my_dict = {"ID": _id,
                   "username": username,
                   "password": password,
                   "role": role}
        my_dict2 = {"ID": _id,
                    "first": name,
                    "last": last_name,
                    "type": role}
        my_dict3 = dict(my_dict, **my_dict2)
        print(my_dict3)
        self.__db.search('login').insert(my_dict)
        self.__db.search('persons').insert(my_dict2)
        self.__db.search('joined_person_login').insert(my_dict3)

    def delete_user(self):
        # only delete user's account in login table
        username = input('Please enter the username: ')
        if not self.__check_user(username):
            print('Invalid username')
        elif self.__check_user(username):
            __confirm_del = _check_input(['1', '2'], 'Are you sure that you want to delete this user, yes(1)/no(2)? ')
            if __confirm_del == '1':
                self.__db.search('login').delete('username', username)
                print('Deleting user was successful.')

    def update_field(self, table_name, keys, val):
        self.__db.search(table_name).update(keys, val)

    def __find_keys(self, table_name):
        for item in self.__db.search(table_name).table:
            return item.keys()

    @staticmethod
    def __show_keys(table_name, keys):
        print(f'These are keys in {table_name}')
        count = 1
        for key in keys:
            print(f'{count}. {key}')
            count += 1

    def main(self):
        x = ''
        while x != 'Q':
            print('Welcome Admin!')
            print('What do you want to do?')
            print('1.add user to database(1)\n2.delete user from database(2)\n3.reset password(3)\n4.update table')
            print('Type Q to quit')
            x = input('Action: ')
            print('+------------------------------------+')
            if x == '1':
                print('Add user to database')
                print('Generating User\'s id...')
                self.add_new_user()
                print('Adding user was successful')  # might add this in add_new_user
                # print(self.__DB.search('login').table)
            elif x == '2':
                print('Delete user from database')
                # print(self.__DB.search('login').table)
                self.delete_user()
                # print(self.__DB.search('login').table)
            elif x == '3':
                user = input('Enter username: ')
                self.reset_password(user)
                # print(self.__DB.search('login').table)
            # elif x == '4':
            #     print('Update table')
            #     table_name = _check_input(['persons', 'login', 'project','advisor_pending_request','member_pending_request','joined_person_login'], 'Enter table name: ', 'Please enter valid table name')
            #     keys = self.__find_keys(table_name)
            #     Admin.__show_keys(table_name,keys)
            #     temp = _check_input(keys, 'Enter key: ', 'Please enter valid key')
            #     val = input('Enter key\'s value')
            #     self.update_field(table_name, keys, val)
            print(self.__db.search('login').table)
            print('+------------------------------------+')


class Project:
    def __init__(self, lead, db):
        self.__project = db.search('project')
        self.__projectID = str(random.randint(10000, 99999))
        self.title = 'None'
        self.lead = lead
        self.member1 = 'None'
        self.member2 = 'None'
        self.advisor = 'None'
        self.project_status = 'None'

    def create_project(self, title):
        # print('Creating project...')
        # print('--Name your project--')
        # title = input('Enter project name: ')
        # only not lead and member can create project
        self.title = title
        temp = {'ProjectID': self.__projectID,
                'Title': self.title,
                'Lead': self.lead,
                'Member1': self.member1,
                'Member2': self.member2,
                'Advisor': self.advisor,
                'Status': self.project_status

                }
        self.__project.insert(temp)

    def change_title(self):
        ask = input('Enter project name: ')
        # self.__project.filter(lambda x:x['ProjectID'] ==)
        self.title = ask

    def project_menu(self):
        # print(student_info)
        print(f'Welcome {self.name}!')
        print('What do you want to do?')
        print("1.Change project's title(1)\n2.My project(2)\n3.Send invitation(3)\n4.My mailbox(4)")
        choice = _check_input_v2(['1', '2', '3', '4'], 'Action: ') # Q won't quit
        # change title
        self.change_title()
        print(self.title)
        print(self.__project)
        # self.__project.filter(lambda x:x[])
        # see status
        # self.project_status()



    def project_status(self):
        #(pending member, pending advisor, or ready to solicit an advisor)
        print('pending member...')
        x = self._Student__member_pending.filter(lambda x:x['Response'] == 'None' and x['ProjectID'] == self.__projectID)
        print(x.table)

    @property
    def project(self):
        return self.__project

    @property
    def projectID(self):
        return self.__projectID

    # @property
    # def title(self):
    #     return self.__title
    #
    # @title.setter
    # def title(self, title):
    #     self.__title = title


class Student(Project):
    def __init__(self, DB, info):
        self.__DB = DB
        self.__member_pending = DB.search('member_pending_request')
        self.__login_db = DB.search('login')
        self.__ext = DB.search('joined_person_login')
        self.id = info[0]
        self.__student_info = self.__ext.filter(lambda x: x['ID'] == self.id).table[0]
        self.firstname = self.__student_info['first']
        self.lastname = self.__student_info['last']
        self.name = f'{self.firstname} {self.lastname}'
        self.status = self.__student_info['role']
        super().__init__(self.name, self.__DB)
        self.num_msg = 0
        self.my_project_id = None
        self.my_project = None

    def __change_status(self, role):
        self.status = 'lead'
        self.__login_db.filter(lambda x: x['ID'] == self.id).update('role', role)
        self.__ext.filter(lambda x: x['ID'] == self.id).update('role', role)

    def __check_status(self):
        if self.status == 'student':
            # print(self.status)
            return True  # only not lead and member can create project
        return False

    # Lead
    def see_project_status(self):
        print(f'{self.title} status')
        super().project_status()

    def see_project(self):
        pass

    def modify_project_info(self):
        # Project table needs to be updated
        pass

    def mailbox(self, role):  # roles are lead, student, advisor, faculty
        # See who has responded to the requests sent out
        # Send requests to potential members
        # NOTE   Send out requests to a potential advisor # ; can only do one at a time and after all potential members have accepted or denied the requests
        # Member_pending_request and Advisor_pending_request  table needs to be updated

        if role == 'lead' or role == 'student':
            __my_mail = self.__member_pending.filter(lambda x: x['to_be_member'] == self.__student_info['username'])
        # print(__my_mail)
        self.num_msg = len(__my_mail.table)
        print('All inboxes')
        print(f'You got {self.num_msg} message!')
        if self.num_msg != 0:
            choice = _check_input(['1', '2'], 'View messages?,yes(1)/no(2): ')
            if choice == '1':
                for msg in __my_mail.table:
                    if msg['Response'] == 'Declined':
                        break
                    print(msg)
                    __my_potential_project = self.__DB.search('project').filter(lambda x: x['ProjectID'] == msg['ProjectID'])
            #         print(111,msg)
                    for project_info in __my_potential_project.table:  # loop in request to join
                        print(222,project_info)
                        print(f"-> {project_info['Lead']} invites you to join project {project_info['Title']}")
                        choice2 = _check_input(['1', '2'], 'Accept or Deny this request,yes(1)/no(2): ')

                        if choice2 == '1':
                            msg['Response'] = 'Accepted'
                            self.__decline_request(__my_mail)
                            self.__add_member(project_info)
                            break
                        elif choice2 == '2':
                            msg['Response'] = 'Declined'



        # print(__my_potential_project)
        # print(self.__member_pending)
        # print(self.__member_pending)
        # print(self.project)


    def __add_member(self,project_info):
        member =1
        # print(5000,project_info)
        if project_info[f'Member{member}'] == 'None':
            project_info[f'Member{member}'] = self.name
        member += 1
        # print(project_info)

    def __decline_request(self,my_mail):
        for mail in my_mail.table:
            if mail['Response'] == 'None':
                mail['Response'] = 'Declined'
        # print(my_mail)

    # @property
    # def project_id(self):
    #     _project_info = self.project.filter(lambda x: x['Lead'] == self.name)
    #     _project_id = _project_info.table[0]['ProjectID']
    #     return _project_id

    def project_info(self):
        member =1  # someone who's not member does not work
        if self.status != 'student':
            _project_info = self.project.filter(lambda x: x['Lead'] == self.name)
            # print(_project_info)
            # if self.status == 'lead':
        #     _project_info = self.project.filter(lambda x: x[f'Member{member}'] == self.name)
        # member+=1
            _project_id = _project_info.table[0]['ProjectID']
            # print(77,_project_id)
            return _project_info,_project_id




# lead
    def send(self,_project_id):
        print(self.project)
        print('Who do you want to send an invitation to?')
        # fIX loop pass the person who already got invitation by that user
        # looking for student only and had not been invited yet
        # ProjectID, to_be_member

        __pending = self.__member_pending.filter(lambda x: x['ProjectID'] == _project_id).select(['to_be_member','ProjectID'])
        temp =[]
        for user in __pending:
           temp.append( user['to_be_member'])
           # print(temp)
           # print(self.__member_pending)
        for student in self.__ext.filter(lambda x: x['role'] == 'student').select(['first', 'last', 'username']):
            if student['username'] not in temp:
                # print(user['to_be_member'],student['username'])
                print(f"first: {student['first']}, lastname: {student['last']}, username: {student['username']}")
                ask = _check_input_v2(['1', '2'], 'Do you want to invite this user into your project?,yes(1)/no(2): ')
                if ask == 'Q':
                    break
                elif ask == '1':
                    # update member pending table
                    # for pend in self.__member_pending.filter(lambda x:x['ProjectID']):
                    #     if pend['"to_be_member"'] != student['username']:2

                        pending = {"ProjectID": self.projectID,
                                   "to_be_member": student['username'],
                                   "Response": 'None',
                                   "Response_date": 'None'
                                   }

                        self.__member_pending.insert(pending)

                        break
                print()

        print(self.__member_pending)

    def __view(self):
        # will show people that lead can send request to
        print('All students')
        for student in self.__ext.filter(lambda x: x['role'] == 'student').select(['first', 'last', 'username']):
            print(f"first: {student['first']}, lastname: {student['last']}, username: {student['username']}")
            print()

    # Member
    # None yet

    def main(self):
        print(self.__student_info)
        print(self.id, self.firstname, self.status)
        print(self.lead, self.member1, self.member2)
        while True:
            print(f'Welcome {self.firstname} {self.lastname[0]}.')
            print('What do you want to do?')
            print('1.Create project(1)\n2.My project(2)\n3.Send invitation(3)\n4.My mailbox(4)')
            choice = _check_input_v2(['1', '2', '3', '4'], 'Action: ')
            print('+------------------------------------+')
            if choice == 'Q':
                break

            if choice == '1':
                # check status first
                # print(self.status)
                if self.__check_status():
                    # student must deny all member requests first
                    title = input('Enter project title: ')
                    self.create_project(title)
                    self.__change_status('lead')
                else:
                    print('You already in existed project!')
            elif choice == '2':
                self.project_menu()
            elif choice == '3':
                # print all students
                if not self.__check_status() and self.status == 'lead':
                    self.send()
                else:
                    print('Only the lead is eligible to send invitations.')

            elif choice == '4':
                self.mailbox(self.status)
            # print(self.__student_info)
            # print(self.id, self.firstname, self.status)
            # print(self.lead, self.member1, self.member2)
            print('+------------------------------------+')
    # def test(self):
    #     # only use with member and lead
    #     # insert this main later
    #     print(self.my_project)
    #     print(self.my_project_id)
    #     self.my_project, self.my_project_id = self.project_info()
    #     print(self.my_project)
    #     print(self.my_project_id)
    #     # print(self.project_id)
    #     # print(self.__student_info)
    #     self.project_menu()
# x = Project()
# print(x.project_ID)
# x.title = 'lol'
# print(x.title)
# run = Student(['9898118', 'student'])
# print(run.project_ID)
# run.main()




