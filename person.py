from datetime import datetime
# from database import Database, Table
# from project_manage import
import random

# for response date and time
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
response = now.strftime("%d/%m/%Y %H:%M:%S")


def long_text(my_table, header):
    print(f'-{header}-')
    txt = input(': ')
    # my_table
    # my_table = table.filter(lambda x:x['ProjectID'] == ProjectID)
    # if len(my_table.table) == 0:
    #     print(1)
    #     return False
    print(my_table)
    my_table.update(header, txt)
    print(my_table)
    # return True


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

    def __find_vals(self, tablename, key_select):
        temp = []
        for _id in self.__db.search(tablename).select(key_select):
            temp.append(_id[key_select])
        return temp

    def __show_row(self, tablename, key, val):
        table = self.__db.search(tablename).filter(lambda x: x[key] == val)
        return table

    def main(self):
        x = ''
        while x != 'Q':
            print('Welcome Admin!')
            print('What do you want to do?')
            print('1.add user to database\n2.delete user from database\n3.reset password\n4.update table')
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
            elif x == '4':
                print('Update table')

                table_name = _check_input(['persons', 'login', 'project', 'advisor_pending_request', 'member_pending_request', 'joined_person_login', 'project_proposal', 'project_report', 'evaluation', 'mail'], 'Enter table name: ', 'Please enter valid table name')

                if table_name != 'login':
                    __id_list = self.__find_vals(table_name, 'ProjectID')
                    # print(55,__id_list)
                    condition = _check_input(__id_list, 'Enter project\'s id: ', 'Please enter valid id')

                else:
                    __id_list = self.__find_vals('login', 'ID')
                    # print(55,__id_list)
                    condition = _check_input(
                        __id_list, 'Enter user\'s id: ', 'Please enter valid id')
                    # print(self.__db.search('login').table[0].values())

                keys = self.__find_keys(table_name)
                # print(keys)
                Admin.__show_keys(table_name, keys)
                temp2 = _check_input(keys, 'Enter key: ', 'Please enter valid key')
                val = input('Enter key\'s value: ')
                if table_name != 'login':
                    my_table = self.__db.search(table_name).filter(lambda y: y['ProjectID'] == condition)
                else:
                    my_table = self.__db.search(table_name).filter(lambda z: z['ID'] == condition)
                my_table.update(temp2, val)
            elif x == '5':
                table_name = _check_input(['persons', 'login', 'project', 'advisor_pending_request', 'member_pending_request',
                     'joined_person_login', 'project_proposal', 'project_report', 'evaluation', 'mail'],
                    'Enter table name: ', 'Please enter valid table name')
                keys = self.__find_keys(table_name)
                Admin.__show_keys(table_name, keys)
                key = _check_input(keys, 'Enter key: ', 'Please enter valid key')
                val = input('Enter key value for filter: ')
                print(self.__show_row(table_name, key, val))


            # print(self.__db.search('login').table)
            print('+------------------------------------+')


class Mail:

    def __init__(self, db, user_info):
        self.__db = db
        self.__project = db.search('project')
        self.__member_pending = db.search('member_pending_request')
        self.__advisor_pending = db.search('advisor_pending_request')
        self.__login_db = db.search('login')
        self.__ext = db.search('joined_person_login')
        self.user_info = user_info
        self.role = user_info['role']
        self.username = user_info['username']
        self.id = user_info['ID']
        self.name = f"{user_info['first']} {user_info['last']}"
        self.__eval_team = self.__db.search('login').filter(lambda x: x['role'] == 'faculty')  # not advisor can eval project
        self.__random = []

    def sent_eval_notification(self, eval_team, project_id):
        # print(17055,self.DB.search('mail'))
        for user in eval_team:
            print(user['username'])
            temp = {'ProjectID': project_id,
                    'evaluation_team': user['username'],
                    'Date_sent': response}
            self.__db.search('mail').insert(temp)
        # print('Messages sent successfully.')

    # print(self.DB.search('mail'))
    # print(eval_team)
    def mailbox(self, role, my_mail):  # roles are lead, student, advisor, faculty
        # See who has responded to the requests sent out
        # Send requests to potential members
        # NOTE Send out requests to a potential advisor # ; can only do one at a time and after all potential members have accepted or denied the requests
        # Member_pending_request and Advisor_pending_request  table needs to be updated
        # see if someone join the project
        # when join make sure the project is not full
        print('omg', role)
        if role != 'faculty' and role != 'advisor':
            # __my_mail = self.__member_pending.filter(
            #     lambda x: x['to_be_member'] == self.user_info['username']).filter(
            #     lambda x: x['Response'] == 'None')
            print('All inboxes')
            print(f'You got {len(my_mail.table)} message!')
            if len(my_mail.table) > 0:
                choice = _check_input(['1', '2'], 'View messages?,yes(1)/no(2): ')
                if choice == '1':
                    for msg in my_mail.table:
                        if msg['Response'] == 'Declined':
                            break
                        # print(msg)
                        __my_potential_project = self.__db.search('project').filter(
                            lambda x: x['ProjectID'] == msg['ProjectID'])
                        #         print(111,msg)
                        for project_info in __my_potential_project.table:  # loop in request to join
                            # print(222, project_info)
                            print(f"-> {project_info['Lead']} invites you to join project {project_info['Title']}")
                            choice2 = _check_input(['1', '2'], 'Accept or Deny this request,yes(1)/no(2): ')

                            if choice2 == '1':
                                msg['Response'] = 'Accepted'
                                msg['Response_date'] = response
                                Mail.__decline_request(my_mail)
                                self.__add_member(project_info, role)
                                self.__change_status('member')

                                break
                            elif choice2 == '2':
                                msg['Response'] = 'Declined'

        else:  # fac and advisor
            # print(1111)
            # __my_mail = self.__advisor_pending.filter(
            #     lambda x: x['to_be_advisor'] == self.faculty_info['username']).filter(lambda x: x['Response'] == 'None')
            # print(__my_mail)
            # print(__my_mail.table)
            # print(len(__my_mail.table))
            __noti = self.__db.search('mail').filter(lambda x: x['evaluation_team'] == self.username)
            print(34567, __noti)
            msg = len(my_mail.table) + len(__noti.table)
            print(__noti)
            print('All inboxes')
            print(f'You got {msg} message!')

            if msg > 0:
                choice = _check_input(['1', '2'], 'View messages?,yes(1)/no(2): ')
                print()
                if choice == '1':
                    if len(__noti.table) > 0:
                        for noti in __noti.table:
                            print(f"Date: {noti['Date_sent']}\nYou are on Project: {noti['ProjectID']} evaluation team.")

                    for msg in my_mail.table:
                        if msg['Response'] == 'Declined':
                            break
                        # print(msg)
                        __my_potential_project = self.__db.search('project').filter(
                            lambda x: x['ProjectID'] == msg['ProjectID'])
                        #         print(111,msg)
                        for project_info in __my_potential_project.table:  # loop in request to join
                            # print(222, project_info)
                            print(f"-> {project_info['Lead']} invites you to join project {project_info['Title']}")
                            choice2 = _check_input(['1', '2'], 'Accept or Deny this request,yes(1)/no(2): ')

                            if choice2 == '1':
                                msg['Response'] = 'Accepted'
                                print(my_mail)
                                # __my_mail.update('Response_date',response)
                                msg['Response_date'] = response
                                print(msg['Response_date'])
                                self.__add_member(project_info, role)
                                status = self.__change_status('advisor')
                                return status
                                break
                            elif choice2 == '2':
                                msg['Response'] = 'Declined'
                                msg['Response_date'] = response

                        print(__my_potential_project)
                        print(self.__advisor_pending)
                        print(self.__member_pending)
                        print(self.__project)

    # second version
    # if len(__my_mail.table) > 0:
    #     choice = _check_input(['1', '2'], 'View messages?,yes(1)/no(2): ')
    #     if choice == '1':
    #         for msg in __my_mail.table:
    #             if msg['Response'] == 'Declined':
    #                 break
    #             # print(msg)
    #             __my_potential_project = self.DB.search('project').filter(
    #                 lambda x: x['ProjectID'] == msg['ProjectID'])
    #             #         print(111,msg)
    #             for project_info in __my_potential_project.table:  # loop in request to join
    #                 # print(222, project_info)
    #                 print(
    #                     f"-> {project_info['Lead']} invites you to join project {project_info['Title']}")
    #                 choice2 = _check_input(['1', '2'], 'Accept or Deny this request,yes(1)/no(2): ')
    #
    #                 if choice2 == '1':
    #                     msg['Response'] = 'Accepted'
    #                     print(__my_mail)
    #                     # __my_mail.update('Response_date',response)
    #                     msg['Response_date'] = response
    #                     print(msg['Response_date'])
    #                     self.__add_member(project_info, role)
    #                     self.__change_status('advisor')
    #
    #                     # print(self.status)
    #
    #                     break
    #                 elif choice2 == '2':
    #                     msg['Response'] = 'Declined'
    #                     msg['Response_date'] = response
    #
    #             # print(__my_potential_project)
    #             print(self.advisor_pending)
    #             # print(self.__member_pending)
    #             # print(self.project)

    # lead---------------------
    def send(self, project):
        _project_id = project.table[0]['ProjectID']
        if project.table[0]['Status'] == 'Approved' and self.role == 'lead':  # only lead can send
            print('\nDo you want to sent request for project evaluation,yes(1)/no(2)')
            choice = _check_input_v2(['1', '2'], 'Action: ')
            if choice == '1':
                print('Randomizing Faculty to evaluate your project...')
                self.random_team()
                print(self.__random)
                # print(self.__random)
                self.sent_eval_notification(self.__random, _project_id)
                print(self.__db.search('mail'))

        else:
            print('Who do you want to send an invitation to?')
            # fIX loop pass the person who already got invitation by that user
            # looking for student only and had not been invited yet
            temp = []
            __pending = self.__member_pending.filter(lambda x: x['ProjectID'] == _project_id).select(
                ['to_be_member', 'ProjectID', 'Response'])  # all requests sent by lead

            __advisor_pend = self.__advisor_pending.filter(lambda x: x['ProjectID'] == _project_id).select(
                ['to_be_advisor', 'ProjectID', 'Response'])  # all requests sent by lead
            print('1.Students\n2.Faculty')
            print(__advisor_pend)
            # print(len(__advisor_pend))
            # print(555,temp)

            choice = _check_input_v2(['1', '2'], 'Action: ')
            if choice == '1':
                print(1)
                if len(__pending) != 0:
                    for user in __pending:  # check whether this user request was sent?
                        # print(len(__pending))
                        temp.append(user['to_be_member'])
                        print(temp)
                        # print(self.__member_pending)
                for student in self.__ext.filter(lambda x: x['role'] == 'student').select(
                        ['first', 'last', 'username']):
                    if student['username'] not in temp:
                        # print(user['to_be_member'],student['username'])
                        print(
                            f"first: {student['first']}, lastname: {student['last']}, username: {student['username']}")
                        ask = _check_input_v2(['1', '2'],
                                              'Do you want to invite this user into your project?,yes(1)/no(2): ')
                        if ask == 'Q':
                            break
                        elif ask == '1':
                            # update member pending table
                            # for pend in self.__member_pending.filter(lambda x:x['ProjectID']):
                            #     if pend['"to_be_member"'] != student['username']:2

                            pending = {"ProjectID": _project_id,
                                       "to_be_member": student['username'],
                                       "Response": 'None',
                                       "Response_date": 'None'
                                       }

                            self.__member_pending.insert(pending)

                            break
        # Send out requests to a potential advisor;
        # can only do one at a time and after all potential members have accepted or denied the requests
        # print(self.__advisor_pending)
        # print(__advisor_pend)

        if choice == '2':
            print(__advisor_pend)
            # old req was view and response(accept/decline)
            reply = self.__advisor_pending.filter(lambda x: x['Response'] != 'None').filter(lambda x: x['ProjectID'] == _project_id)
            print(reply)
            print(len(reply.table)>0)
            if len(reply.table) > 0:
                print(11111)
                print('Your project already has an advisor!')
            else:
                print(300)
                if len(__advisor_pend) > 0:  # second time have to check whether request had sent to this faculty
                    for user in __advisor_pend:
                        if user['Response'] == 'None':
                            temp.append(user['to_be_advisor'])  # temp keep user with none response
                # print(temp)
                if len(temp) == 0:
                    for teacher in self.__ext.filter(lambda x: x['role'] == 'faculty' or x['role'] == 'advisor').select(
                            ['first', 'last', 'username']):
                        if teacher['username'] not in temp:
                            print(f"first: {teacher['first']}, lastname: {teacher['last']}, username: {teacher['username']}")
                            ask = _check_input_v2(['1', '2'],
                                                  'Do you want to invite this user into your project?,yes(1)/no(2): ')
                            if ask == 'Q':
                                break
                            elif ask == '1':
                                pending = {"ProjectID": _project_id,
                                           "to_be_advisor": teacher['username'],
                                           "Response": 'None',
                                           "Response_date": 'None'
                                           }

                                self.__advisor_pending.insert(pending)

                                break
                            print()
                else:
                    print('Your cannot send more request when there\'s pending advisor')
                    # print('After', self.__advisor_pending)
                temp.clear()



    @staticmethod
    def __decline_request(my_mail):  # automatically decline after user accept request to join project
        for mail in my_mail.table:
            if mail['Response'] == 'None':
                mail['Response'] = 'Declined'
                mail['Response_date'] = response
                # print(my_mail)


    # for eval
    def random_team(self):
        while len(self.__random) != 3: # faculty members will evaluate their project
            picked = random.choice(self.__eval_team.table)
            if picked not in self.__random:
                self.__random.append(picked)
        print(len(self.__eval_team.table))
        print(self.__random)


    # for lead-------------------------------
    def __add_member(self, project_info, role):
        member = 1
        print(5000, project_info)  # fix
        if role == 'faculty' or role == 'advisor':

            project_info['Advisor'] = self.name
        elif project_info[f'Member{member}'] == 'None':
            project_info[f'Member{member}'] = self.name
        member += 1
        print(project_info)

    def __change_status(self, role):  # lead ver
        self.status = role
        print(self.__login_db)
        self.__login_db.filter(lambda x: x['ID'] == self.id).update('role', role)
        self.__ext.filter(lambda x: x['ID'] == self.id).update('role', role)
        # print(self.__login_db)
        return True

class Project:
    def __init__(self, db):
        self.__db = db
        self.__project = db.search('project')
        self.__projectID = str(random.randint(10000, 99999))
        self.title = 'None'
        self.lead = 'None'
        self.member1 = 'None'
        self.member2 = 'None'
        self.advisor = 'None'
        self.project_status = 'None'
        self.__project_proposal = db.search('project_proposal')
        self.__project_report = db.search('project_report')


    # for lead initialization-------------------------------
    def create_project(self, title):
        print('Creating project...')
        # only students can create project
        # print(self.__projectID)
        print(self.title)
        self.title = title
        print(self.title)
        temp = {'ProjectID': self.__projectID,
                'Title': self.title,
                'Lead': self.lead,
                'Member1': self.member1,
                'Member2': self.member2,
                'Advisor': self.advisor,
                'Status': self.project_status

                }

        temp2 = {'ProjectID': self.__projectID,
                 'Title': self.title,
                 'Abstract': 'None',
                 'Goals': 'None',
                 'Timeline': 'None',
                 'Budget': 'None',
                 'Comments': 'None',  # for advisor
                 'Status': 'None'  # for advisor

                 }

        temp3 = {'ProjectID': self.__projectID,
                 'Title': self.title,
                 'Conclusion': 'None',
                'Comments' : 'None', # ad
                 'Status': 'None'  # for advisor
                 }
        self.__project.insert(temp)
        self.__project_proposal.insert(temp2)
        self.__project_report.insert(temp3)

    # for member and lead-------------------------------

    def __initialization(self, my_project):
        print(self.title, self.member1, self.advisor, self.project_status, self.__projectID)
        self.__project = my_project
        self.__projectID = self.__project.table[0]['ProjectID']
        self.title = self.__project.table[0]['Title']
        self.lead = self.__project.table[0]['Lead']
        self.member1 = self.__project.table[0]['Member1']
        self.member2 = self.__project.table[0]['Member2']
        self.advisor = self.__project.table[0]['Advisor']
        self.project_status = self.__project.table[0]['Status']
        self.__project_proposal = self.__db.search('project_proposal').filter(
            lambda x: x['ProjectID'] == self.__projectID)
        self.__project_report = self.__db.search('project_report').filter(lambda x: x['ProjectID'] == self.__projectID)

    def __check_status(self):
        status_proposal = self.__project_proposal.table[0]['Status']
        print(status_proposal)
        # print(status_proposal)
        status_report = self.__project_report.table[0]['Status']
        print(status_report)
        # print(1,status_proposal)
        if status_proposal == 'Approved' and status_report == 'Approved' and self.project_status == 'Approved':
            return True
        return False

    def project_menu(self, my_project, pending_members):
        # print(self.__projectID, self.__project, self.title, self.lead, self.member1, self.member2, self.advisor)
        # make sure members have these attr too
        for i in pending_members:
            print(i)
        print(pending_members)
        print(44444, my_project.table)
        print(44444,my_project.table[0]['ProjectID'])
        # self.__initialization(my_project)
        # print(self.__project)
        # print(f'Welcome {self.name}!')
        print(234, my_project)
        if self.__check_status():
            print('Your project was approved by your advisor')

        print('What do you want to do?')

        print("1.Change project's title\n2.My project's status\n3.Modify project")

        choice = _check_input_v2(['1', '2', '3'], 'Action: ')
        # change title
        if choice == '1':
            print(self.__project)
            self.change_title()
            print(self.__project)
        # see status
        elif choice == '2':
            self.see_project_status(pending_members)
        elif choice == '3':
            self.modify_project(my_project)

        print('+------------------------------------+')

    def project_menu_2(self, my_project):  # advisor version
        self.__initialization(my_project)
        # print(self.__project)
        print('What do you want to do?')
        print("1.Modify project\n2.Change project status")

        choice = _check_input_v2(['1', '2'], 'Action: ')
        # change title
        if choice == '1':
            self.view_project()
            self.modify_project(my_project, 'advisor')

        elif choice == '2':
            # print(23243535, self.__project_proposal)
            # print(23243535, self.__project_report)
            # print(23243535, self.__project)
            print('Which status do you want to edit?')
            print('1.Proposal\n2.Report\n3.Project')
            choice = _check_input_v2(['1', '2', '3'], 'Action: ')
            if choice == '1':  # proposal
                # print(f'Current project status: {self.project_status}')
                print(f'Pick status')
                print('1.Approve\n2.Decline')
                _choice = _check_input_v2(['1', '2'], 'Action: ')

                if _choice == '1':

                    status = 'Approved'

                else:
                    status = 'Declined'
                self.__project_proposal.update('Status', status)

            elif choice == '2':  # report
                print(f'Current project status: {self.project_status}')
                print(f'Pick status')
                print('1.Approve\n2.Decline')
                _choice = _check_input_v2(['1', '2'], 'Action: ')
                if _choice == '1':

                    status = 'Approved'

                else:
                    status = 'Declined'
                self.__project_report.update('Status', status)
            elif choice == '3':  # overall
                print(f'Current project status: {self.project_status}')
                print(f'Pick status')
                print('1.Approve\n2.Decline')
                _choice = _check_input_v2(['1', '2'], 'Action: ')
                if _choice == '1':
                    self.project_status = 'Approved'
                else:
                    self.project_status = 'Declined'
                self.__project.update('Status', self.project_status)
            print(23243535, self.__project_proposal)
            print(23243535, self.__project_report)
            print(23243535, self.__project)

    def change_title(self):
        ask = input('Enter project name: ')
        self.title = ask
        self.__project.update('Title', self.title)
        self.__project_report.update('Title', self.title)
        self.__project_proposal.update('Title', self.title)

    def change_project_status(self):  # FIXXX
        self.project_status = 'ready to solicit'
        self.__project.update('Status', self.project_status)

    def see_project_status(self, my_pending):  # for display my_pending[0],my_pending[1]
        # (pending member, pending advisor, or ready to solicit an advisor)
        if self.__check_status():
            print('Please contact for evaluation process')
        for i in my_pending:
            print(11,i)
        if self.member1 == 'None' or self.member2 == 'None':
            print('Pending members...')
            print(self.__db.search('member_pending_request'))
            print(my_pending[0])
            for member in my_pending[0].table:
                print(
                    f"Pending member: {member['to_be_member']}, Response: {member['Response']}, Response_date: {member['Response_date']}")
        print()
        # advisor pending
        if self.advisor == 'None':  # still have no advisor
            print('Pending advisors...')

            for member in my_pending[1].table:
                print(
                    f"Pending member: {member['to_be_advisor']}, Response: {member['Response']}, Response_date: {member['Response_date']}")
        # else:
        #     print('No pending member at the moment.')
        # print('+------------------------------------+')
        elif self.member1 != 'None' and self.member2 != 'None' and self.advisor != 'None':
            print('Your project is ready to solicit an advisor!')
            self.change_project_status()
        print('+------------------------------------+')

    def view_project(self):  # advisor
        # print(11111,self.__project_proposal)
        for txt in self.__project_proposal.table:
            print()
            print(
                f"Title:\n {txt['Title']}\nAbstract:\n {txt['Abstract']}\nGoals:\n {txt['Goals']}\nTimeline:\n {txt['Timeline']}\nBudget:\n {txt['Budget']}\n")
            print(f"Comments: {txt['Comments']}\nStatus: {txt['Status']}")

    def modify_project(self, my_project, role=''):

        # Project table needs to be updated
        # project proposal
        if role == 'advisor':
            print('Editing project fields...')
            self.view_project()
            choice = _check_input_v2(['1', '2'], 'Add comments to, proposal(1)/ report(2): ')
            my_proposal_ad = self.__project_proposal.filter(lambda x: x['ProjectID'] == my_project.table[0]['ProjectID'])
            my_report_ad = self.__project_report.filter(
                lambda x: x['ProjectID'] == my_project.table[0]['ProjectID'])
            print(self.__project_proposal)
            # print(33333,my_project)
            if choice == '1':
                long_text(my_proposal_ad,'Comments')
                print(self.__project_proposal)
            elif choice == '2':
                long_text(my_report_ad, 'Comments')
                print(self.__project_report)




        # def long_text(my_table, header):
        else:
            while True:
                # print(666,my_project)
                # print(1234566, self.__project_proposal)
                print('Which part do you want to modify?')
                print("1.Proposal\n2.Report")  # comment and status are for advisor
                pick = _check_input_v2(['1', '2'], 'Enter: ')
                my_report = self.__project_report.filter(lambda x:x['ProjectID'] == my_project.table[0]['ProjectID'])
                my_proposal = self.__project_proposal.filter(lambda x:x['ProjectID'] == my_project.table[0]['ProjectID'])
                print(34,self.__project_proposal.filter(lambda x:x['ProjectID'] == my_project.table[0]['ProjectID']))
                if pick == '1':
                    print('What field do you want to modify?')
                    print("1.Abstract\n2.Goals\n3.Timeline\n4.Budget")  # comment and status are for advisor
                    choice = _check_input_v2(['1', '2', '3', '4'], 'Action: ')
                    if choice == 'Q':
                        break
                    # print(66666,self.__project_proposal.table['Timeline'])
                    if choice == '1':
                        # my_proposal.update('Abstract')
                        long_text(my_proposal, 'Abstract')


                    elif choice == '2':
                        long_text(my_proposal, 'Goals')
                    elif choice == '3':
                        long_text(my_proposal, 'Timeline')
                    elif choice == '4':
                        long_text(my_proposal, 'Budget')
                # print(self.__project_proposal)
                elif pick == '2':
                    conc = input('Conclusion')
                    my_report.update('Conclusion', conc)

    @property
    def projectID(self):
        return self.__projectID


# make sure all project proposal and report approved
class Evaluation(Mail):
    # self.__eval_instance = Evaluation(self.__db, self.__faculty_info)

    # def __init__(self,db,project):
    #     self.__db = db
    #     # self.__project = project
    #     # self.__evaluation = self.__db.search('evaluation')

    def __init__(self, db):
        self.__db = db
        self.__evaluation = self.__db.search('evaluation')




    def view_criteria(self):
        print('-Criteria-')
        print("""-Functionality 20%
-Creativity 20%
-Effectiveness 20%
-Relevance 20%
-Impact 20%
Need 50% to pass the project""")
        print('+------------------------------------+')

    def __check_eval_existance(self,this_ival_id):
        if len(self.__evaluation.filter(lambda x:x['ProjectID'] == this_ival_id).table) == 0 :
            return True # there is this eval somewhere
        return False

    def rate_criteria(self, this_eval_project):  # passed

        this_eval_id = this_eval_project['ProjectID']
        this_eval_score_table = self.__evaluation.filter(lambda x: x['ProjectID'] == this_eval_id)
        print(this_eval_score_table)
        this_project = self.__db.search('project').filter(lambda x:x['ProjectID'] == this_eval_id)
        print(400,this_project)
        print(500,self.__evaluation)
        temp = []

        for i in range(1, 21):
            temp.append(str(i))
        functionality = _check_input(temp, 'Enter functionality score(1-20%): ')
        creativity = _check_input(temp, 'Enter creativity score(1-20%): ')
        effectiveness = _check_input(temp, 'Enter usability score(1-20%): ')
        relevance = _check_input(temp, 'Enter relevance score(1-20%): ')
        impact = _check_input(temp, 'Enter impact score(1-20%): ')

        temp2 = [int(functionality), int(creativity), int(effectiveness), int(relevance), int(impact)]
        calculated = self.total(this_project, temp2)
        if self.__check_eval_existance(this_eval_id):
            self.__evaluation.insert({'ProjectID': this_eval_id,
                                      'Functionality': functionality,
                                      'Creativity': creativity,
                                      'Effectiveness':effectiveness,
                                      'Relevance': relevance,
                                    'Impact': impact,
                                      'Total': calculated})

        else:
            # print(this_eval_score_table)
            this_eval_score_table.update('Functionality', functionality)
            this_eval_score_table.update('Creativity', creativity)
            this_eval_score_table.update('Effectiveness', effectiveness)
            this_eval_score_table.update('Relevance', relevance)
            this_eval_score_table.update('Impact', impact)
            calculated = self.total(this_project, temp2)
            this_eval_score_table.update('Total', calculated)

        if calculated > 50:
            # print('passed')
            # return True
            status = 'Passed'
            this_project.update('Status', status)
            # print(this_project)

        else:
            print('fail')
            status = 'Failed'
            this_project.update('Status', status)
            print(this_project)
            return False


    def total(self,this_project, score):
        total = sum(score)
        print(total)
        print(f'Total score = {total}/100')
        # this_project.update('Total', total)
        return total
        # if total == 50:
        #     return True  # passed
        # return False



class Student(Project, Mail):
    def __init__(self, DB, info):
        self.__DB = DB
        self.__member_pending = DB.search('member_pending_request')
        self.__advisor_pending = DB.search('advisor_pending_request')
        self.__login_db = DB.search('login')
        self.__project = DB.search('project')
        self.__ext = DB.search('joined_person_login')
        self.id = info[0]
        self.__student_info = self.__ext.filter(lambda x: x['ID'] == self.id).table[0]
        self.firstname = self.__student_info['first']
        self.lastname = self.__student_info['last']
        self.name = f'{self.firstname} {self.lastname}'
        self.status = self.__student_info['role']
        super().__init__(self.__DB)
        self._mail_instance = Mail(DB, self.__student_info)
        self.my_project_id = 'None'
        self.my_project = 'None'

    def find_pending_members(self, project_id):
        # print(self.__member_pending)
        # print(project_id)
        pending_members = self.__member_pending.filter(
            lambda x: x['Response'] == 'None').filter(lambda x: x['ProjectID'] == project_id)
        pending__advisor = self.__advisor_pending.filter(
            lambda x: x['Response'] == 'None').filter(lambda x: x['ProjectID'] == self.__projectID)
        # print(2345,pending_members)
        temp = [pending_members, pending__advisor]
        return temp

    def __change_status(self, role):  # lead ver
        self.status = role
        # update table with roles involved
        self.__login_db.filter(lambda x: x['ID'] == self.id).update('role', role)
        self.__ext.filter(lambda x: x['ID'] == self.id).update('role', role)

    def __check_status(self):  # only not lead and member can create project
        if self.status == 'student':
            # print(self.status)
            return True
        return False

    def project_info(self): # need fix
        print('All project', self.__project)
        member = 1  # someone who's not member does not work
        print(self.status)
        print(self.name)
        if self.status != 'student':
            if self.status == 'lead':
                print('is lead')
                _project_info = self.__project.filter(lambda x: x['Lead'] == self.name)
                print('My project', _project_info)
            else:
                # print('is not lead')
                _project_info = self.__project.filter(lambda x: x[f'Member{member}'] == self.name)
            _project_id = _project_info.table[0]['ProjectID']
            return _project_info, _project_id

    def __view(self):
        # will show people that lead can send request to
        print('All students')
        for student in self.__ext.filter(lambda x: x['role'] == 'student').select(['first', 'last', 'username']):
            print(f"first: {student['first']}, lastname: {student['last']}, username: {student['username']}")
            print()

    def __initialization(self, my_project):
        print(self.title, self.member1, self.advisor, self.project_status)
        self.__project = my_project
        self.__projectID = self.__project.table[0]['ProjectID']
        self.title = self.__project.table[0]['Title']
        self.lead = self.__project.table[0]['Lead']
        self.member1 = self.__project.table[0]['Member1']
        self.member2 = self.__project.table[0]['Member2']
        self.advisor = self.__project.table[0]['Advisor']
        self.project_status = self.__project.table[0]['Status']
        self.__project_proposal = self.__DB.search('project_proposal').filter(
            lambda x: x['ProjectID'] == self.__projectID)
        self.__project_report = self.__DB.search('project_report').filter(lambda x: x['ProjectID'] == self.__projectID)
        print(self.title, self.member1, self.advisor, self.project_status)

    def main(self):
        if self.status == 'lead':
            self.lead = self.name
            my_project, my_project_id = self.project_info()  # alr had project
            self.__initialization(my_project)
        # print('info', self.__student_info)
        # print(self.project)
        # print(34577,my_project.table[0])
        # print(self.status)

        # print(self.__student_info)
        # print(self.id, self.firstname, self.status)
        # print(self.lead, self.member1, self.member2)

        while True:
            # if not self.__check_status() and self.status != 'lead':  # alr had project
            #     my_project, my_project_id = self.project_info()
            #     # print(500,my_project)
            #     self.__initialization(my_project)
            if not self.__check_status():  # alr had project
                my_project, my_project_id = self.project_info()
                # print(500,my_project)
                self.__initialization(my_project)

            # print(self.status)
            print(self.__project)  # all projects
            # print(self.__login_db)
            print(self.__student_info)
            print()
            print(f'Welcome {self.firstname} {self.lastname[0]}.')
            print('What do you want to do?')
            print('1.Create project\n2.My project\n3.Send invitation\n4.My mailbox')
            choice = _check_input_v2(['1', '2', '3', '4'], 'Enter: ')
            print('+------------------------------------+')
            if choice == 'Q':
                break
            if choice == '1':
                # check status first
                # print(self.status)
                if self.__check_status():  # students can create project
                    # student must deny all member requests first
                    self.lead = self.name
                    title = input('Enter project title: ')
                    self.create_project(title)
                    self.__change_status('lead')

                else:
                    print('You already in existed project!')
            elif choice == '2':
                if self.status != 'student':
                    # print(77777, my_project_id, my_project)

                    # print(self.lead)

                    print(f'Welcome {self.name}!')
                    pending_members = self.find_pending_members(my_project_id)
                    print(111111,pending_members)
                    super().project_menu(my_project, pending_members)
                else:
                    print("The project do not exists.")
                    print('Create project first.')
            elif choice == '3':
                # print all students
                # print(my_project_id)
                if not self.__check_status() and self.status == 'lead':
                    self._mail_instance.send(my_project)
                else:
                    print('Only the lead is eligible to send invitations.')

            elif choice == '4':
                __my_mail = self.__member_pending.filter(
                    lambda x: x['to_be_member'] == self.__student_info['username']).filter(
                    lambda x: x['Response'] == 'None')
                self._mail_instance.mailbox(self.status, __my_mail)

            # print(self.__student_info)
            # print(self.id, self.firstname, self.status)
            # print(self.lead, self.member1, self.member2)
            # print(self.project)
            # print(self.__login_db)
            # print(self.__student_info)
            print('+------------------------------------+')


# Mail,Project,Evaluation
class Faculty(Project):
    def __init__(self, db, info):
        # access self.DB self.member_pending
        self.__db = db
        self.id = info[0]
        self.__login_db = db.search('login')
        self.__evaluation = db.search('evaluation')
        self.__advisor_pending = db.search('advisor_pending_request')
        self.__ext = db.search('joined_person_login')
        self.__faculty_info = self.__ext.filter(lambda x: x['ID'] == self.id).table[0]
        self.firstname = self.__faculty_info['first']
        self.lastname = self.__faculty_info['last']
        self.username = self.__faculty_info['username']
        self.__eval_projects = self.__db.search('mail').filter(lambda x: x['evaluation_team'] == self.username)
        self.name = f'{self.firstname} {self.lastname}'
        self.status = self.__faculty_info['role']
        if self.status == 'advisor':
            self.__project = db.search('project').filter(lambda x: x['Advisor'] == self.name)
        self.__mail_instance = Mail(self.__db,self.__faculty_info)
        super().__init__(db)

        self.__eval_instance = Evaluation(self.__db) # if broke

    @property
    def db(self):
        return self.__db
    def view_my_project(self):
        # print('1.My project\n2.Evaluate projects\n3.My mailbox')
        # choice = _check_input_v2(['1', '2', '3'], 'Action: ')
        my_project = self.__project.filter(lambda x: x['Advisor'] == self.name)
        print('-My projects-')
        for project in my_project.table:
            print(
                f"Project Id: {project['ProjectID']}\nTitle: {project['Title']}, Lead: {project['Lead']}, Status: {project['Status']}")
            choice = _check_input(['1', '2'], 'Do you want to modify this project?,yes(1)/no(2): ')
            if choice == '1':
                return my_project.filter(lambda x: x['ProjectID'] == project['ProjectID'])
            print()

    def pick_to_eval(self):
        for project in self.__eval_projects.table:
            print(f"Project Id: {project['ProjectID']}\nDate: {project['Date_sent']}")
            choice = _check_input(['1', '2'], 'Do you want to evaluate this project?,yes(1)/no(2): ')
            if choice == '1':
                return project
            print()

        # print(my_project)

    # def project_info(self):
    #     print('All project', self.__project)
    #     # print('is not lead')
    #     _project_info = self.__project.filter(lambda x: x[f'Member{member}'] == self.name)
    #     _project_id = _project_info.table[0]['ProjectID']
    #     return _project_info, _project_id


    def __initialization(self, my_project):
        print(43,self.title, self.member1, self.advisor, self.project_status)
        self.__project = my_project
        self.__projectID = self.__project.table[0]['ProjectID']
        self.title = self.__project.table[0]['Title']
        self.lead = self.__project.table[0]['Lead']
        self.member1 = self.__project.table[0]['Member1']
        self.member2 = self.__project.table[0]['Member2']
        self.advisor = self.__project.table[0]['Advisor']
        self.project_status = self.__project.table[0]['Status']
        self.__project_proposal = self.__db.search('project_proposal').filter(
            lambda x: x['ProjectID'] == self.__projectID)
        self.__project_report = self.__db.search('project_report').filter(lambda x: x['ProjectID'] == self.__projectID)
        print(self.title, self.member1, self.advisor, self.project_status)

    @staticmethod
    def check_eval(eval_projects):
        if len(eval_projects.table) > 0:
            return True
        return False

    def main(self):
        if self.status == 'advisor':
            self.__initialization(self.__project)
        print('faculty',self.__faculty_info)
        print(self.__eval_projects)
        print(self.__db)
        print('status', self.status)
        while True:
            if self.status == 'advisor':
                self.__project = self.__db.search('project').filter(lambda x: x['Advisor'] == self.name)
            print('status', self.status)
            print('faculty', self.__faculty_info)
            print(f'Welcome {self.firstname} {self.lastname[0]}.')
            print('What do you want to do?')
            print('1.Modify project\n2.My mailbox\n3.Evaluate project')
            choice = _check_input_v2(['1', '2', '3'], 'Action: ')
            print('+------------------------------------+')

            if choice == 'Q':
                break
            if choice == '1':
                if self.status == 'advisor':
                    my_project = self.view_my_project()
                    print(444,my_project)
                    print(f'Welcome {self.name}!')
                    super().project_menu_2(my_project)
                else:
                    print('You can\'t access not existence project!')

            if choice == '2':
                __my_mail = self.__advisor_pending.filter(
                    lambda x: x['to_be_advisor'] == self.__faculty_info['username']).filter(
                    lambda x: x['Response'] == 'None')
                status = self.__mail_instance.mailbox('faculty',__my_mail)
                if status:
                    self.status = 'advisor'


            if choice == '3':
                # print(self.__eval_projects) # keep track
                if Faculty.check_eval(self.__eval_projects):
                    # print(self.__db.search('project'))

                    project = self.pick_to_eval()
                    print(project)
                    # print(project['ProjectID'])
                    # self.eval_instance.view_criteria()
                #
                    project_score = self.__eval_instance.rate_criteria(project)
                #     print(project)
                #
                #     print(project_score)
                # else:
                #     print('You have no permission to evaluate project')

            print('+------------------------------------+')


            # if choice == '3':
            #     # print(self.__eval_projects) # keep track
            #     if Faculty.check_eval(self.__eval_projects):
            #         # print(self.__db.search('project'))
            #
            #         project = self.pick_to_eval()
            #         # print(project)
            #         # print(project['ProjectID'])
            #         eval_instance = Evaluation(self.__db, project)
            #         eval_instance.view_criteria()
            #
            #         project_score = eval_instance.rate_criteria(self.__db, project['ProjectID'])
            #         print(project)
            #
            #         print(project_score)
            #     else:
            #         print('You have no permission to evaluate project')
            #
            # print('+------------------------------------+')