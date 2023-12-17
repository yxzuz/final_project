from datetime import datetime
from database import Database, Table
# from project_manage import
import random

# for response date and time
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
response = now.strftime("%d/%m/%Y %H:%M:%S")


def long_text(header, table):
    print(f'-{header}-')
    txt = input(': ')
    table.update(header, txt)


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


class Mail:
    def sent_eval_notification(self, eval_team):
        # print(17055,self.DB.search('mail'))
        for user in eval_team:
            print(user['username'])
            temp = {'ProjectID': self.projectID,
                   'evaluation_team': user['username'],
                    'Date_sent': response}
            self.DB.search('mail').insert(temp)
        print('Messages sent successfully.')
        # print(self.DB.search('mail'))
        # print(eval_team)

    def mailbox(self, role):  # roles are lead, student, advisor, faculty
        # See who has responded to the requests sent out
        # Send requests to potential members
        # NOTE Send out requests to a potential advisor # ; can only do one at a time and after all potential members have accepted or denied the requests
        # Member_pending_request and Advisor_pending_request  table needs to be updated
        # see if someone join the project
        # when join make sure the project is not full
        # __my_mail = None
        print('omg', role)
        if role != 'faculty' and role != 'advisor':
            __my_mail = self.member_pending.filter(lambda x: x['to_be_member'] == self.student_info['username']).filter(
                lambda x: x['Response'] == 'None')
            print('All inboxes')
            print(f'You got {len(__my_mail.table)} message!')
            if len(__my_mail.table) > 0:
                choice = _check_input(['1', '2'], 'View messages?,yes(1)/no(2): ')
                if choice == '1':
                    for msg in __my_mail.table:
                        if msg['Response'] == 'Declined':
                            break
                        # print(msg)
                        __my_potential_project = self.DB.search('project').filter(
                            lambda x: x['ProjectID'] == msg['ProjectID'])
                        #         print(111,msg)
                        for project_info in __my_potential_project.table:  # loop in request to join
                            # print(222, project_info)
                            print(f"-> {project_info['Lead']} invites you to join project {project_info['Title']}")
                            choice2 = _check_input(['1', '2'], 'Accept or Deny this request,yes(1)/no(2): ')

                            if choice2 == '1':
                                msg['Response'] = 'Accepted'
                                msg['Response_date'] = response
                                self.__decline_request(__my_mail)
                                self.__add_member(project_info, role)
                                self.__change_status('member')

                                break
                            elif choice2 == '2':
                                msg['Response'] = 'Declined'

        else:  # fac and advisor
            # print(1111)
            __my_mail = self.advisor_pending.filter(
                lambda x: x['to_be_advisor'] == self.faculty_info['username']).filter(lambda x: x['Response'] == 'None')
            # print(__my_mail)
            # print(__my_mail.table)
            # print(len(__my_mail.table))
            __noti = self.DB.search('mail').filter(lambda x:x['evaluation_team'] == self.username)
            print(34567,__noti)
            msg = len(__my_mail.table) + len(__noti.table)
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

                    for msg in __my_mail.table:
                        if msg['Response'] == 'Declined':
                            break
                        # print(msg)
                        __my_potential_project = self.DB.search('project').filter(
                            lambda x: x['ProjectID'] == msg['ProjectID'])
                        #         print(111,msg)
                        for project_info in __my_potential_project.table:  # loop in request to join
                            # print(222, project_info)
                            print(f"-> {project_info['Lead']} invites you to join project {project_info['Title']}")
                            choice2 = _check_input(['1', '2'], 'Accept or Deny this request,yes(1)/no(2): ')

                            if choice2 == '1':
                                msg['Response'] = 'Accepted'
                                print(__my_mail)
                                # __my_mail.update('Response_date',response)
                                msg['Response_date'] = response
                                print(msg['Response_date'])
                                self.__add_member(project_info, role)
                                self.__change_status('advisor')
                                break
                            elif choice2 == '2':
                                msg['Response'] = 'Declined'
                                msg['Response_date'] = response

                        # print(__my_potential_project)
                        # print(self.advisor_pending)
                        # print(self.__member_pending)
                        # print(self.project)




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

    def __decline_request(self, my_mail):
        for mail in my_mail.table:
            if mail['Response'] == 'None':
                mail['Response'] = 'Declined'
                mail['Response_date'] = response

        # print(my_mail)

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
        self.login_db.filter(lambda x: x['ID'] == self.id).update('role', role)
        self.ext.filter(lambda x: x['ID'] == self.id).update('role', role)
class Project(Mail):
    def __init__(self, lead, db):
        self.__DB = db
        self.__project = db.search('project')
        self.__projectID = str(random.randint(10000, 99999))
        self.title = 'None'
        self.lead = lead
        self.member1 = 'None'
        self.member2 = 'None'
        self.advisor = 'None'
        self.project_status = 'None'
        self.__project_proposal = db.search('project_proposal')
        self.__project_report = db.search('project_report')
        self.__eval_team = self.__DB.search('login').filter(lambda x: x['role'] == 'faculty')
        self.__random = []


    # for lead initialization-------------------------------
    def create_project(self, title):
        print('Creating project...')
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
                 'Summary': 'None',
                 'Results': 'None',
                 'Challenges': 'None',
                 'Lessons': 'None',
                 'Conclusion': 'None',
                 'Status': 'None'  # for advisor

                 }
        self.__project.insert(temp)
        self.__project_proposal.insert(temp2)
        self.__project_report.insert(temp3)

    # for member and lead-------------------------------

    def __initialization(self, my_project):
        self.__project = my_project
        self.__projectID = self.__project.table[0]['ProjectID']
        self.title = self.__project.table[0]['Title']
        self.lead = self.__project.table[0]['Lead']
        self.member1 = self.__project.table[0]['Member1']
        self.member2 = self.__project.table[0]['Member2']
        self.advisor = self.__project.table[0]['Advisor']
        self.project_status = self.__project.table[0]['Status']
        self.__project_proposal = self.DB.search('project_proposal').filter(
            lambda x: x['ProjectID'] == self.__projectID)
        self.__project_report = self.DB.search('project_report').filter(lambda x: x['ProjectID'] == self.__projectID)

    def __check_status(self):
        status_proposal = self.__project_proposal.table[0]['Status']
        # print(status_proposal)
        status_report = self.__project_report.table[0]['Status']
        # print(1,status_proposal)
        if status_proposal == 'Approved' and status_report =='Approved' and self.project_status == 'Approved':
            return True
        return False

    def project_menu(self, my_project):
        # print(self.__projectID, self.__project, self.title, self.lead, self.member1, self.member2, self.advisor)
        # make sure members have these attr too

        self.__initialization(my_project)
        # print(self.__project)
        print(f'Welcome {self.name}!')
        print('What do you want to do?')

        print("1.Change project's title\n2.My project's status\n3.Modify project\n4.Sent request for evaluation")

        choice = _check_input_v2(['1', '2', '3', '4'], 'Action: ')
        # change title
        if choice == '1':
            print(self.__project)
            self.change_title()
            print(self.__project)
        # see status
        elif choice == '2':
            self.see_project_status()
        elif choice == '3':
            self.modify_project()
        elif choice == '4':
            if not self.__check_status():
                print('Your project are not approved by your advisor yet')
            else:
                print('Randomizing Faculty to evaluate your project...')
                self.random_team()
                print(self.__random)
                super().sent_eval_notification(self.__random)

        print('+------------------------------------+')

    def project_menu_2(self, my_project):  # advisor version
        self.__initialization(my_project)
        # print(self.__project)
        print(f'Welcome {self.name}!')
        print('What do you want to do?')
        print("1.Modify project\n2.Change project status")

        choice = _check_input_v2(['1','2'], 'Action: ')
        # change title
        if choice == '1':
            self.view_project()
            self.modify_project()

        elif choice == '2':
            print(23243535,self.__project_proposal)
            print(23243535, self.__project_report)
            print(23243535, self.__project)
            print('Which status do you want to edit?')
            print('1.Proposal\n2.Report\n3.Project')
            choice = _check_input_v2(['1', '2','3'], 'Action: ')
            if choice == '1':  # proposal
                # print(f'Current project status: {self.project_status}')
                print(f'Pick status')
                print('1.Approve\n2.Decline')
                _choice = _check_input_v2(['1', '2'], 'Action: ')

                if _choice == '1':

                    status = 'Approved'

                else:
                    status = 'Declined'
                self.__project_proposal.update('Status',status)

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
            print(23243535,self.__project_proposal)
            print(23243535, self.__project_report)
            print(23243535, self.__project)




    def change_title(self):
        ask = input('Enter project name: ')
        self.title = ask
        self.__project.update('Title', self.title)
        self.__project_report.update('Title', self.title)
        self.__project_proposal.update('Title', self.title)

    def change_project_status(self): #FIXXX
        self.project_status = 'ready to solicit'
        self.__project.update('Status', self.project_status)

    def see_project_status(self):  # for display
        # (pending member, pending advisor, or ready to solicit an advisor)
        print()
        if self.member1 == 'None' or self.member2 == 'None':
            print('Pending members...')

            # pending_members = self._Student__member_pending.filter(
            #     lambda x: x['Response'] == 'None' and x['ProjectID'] == self.__projectID)
            pending_members = self.member_pending.filter(
                lambda x: x['Response'] == 'None' and x['ProjectID'] == self.__projectID)
            for member in pending_members.table:
                print(
                    f"Pending member: {member['to_be_member']}, Response: {member['Response']}, Response_date: {member['Response_date']}")
        print()
        # advisor pending
        if self.advisor == 'None':  # still have no advisor
            # self._Student__advisor_pending
            print('Pending advisors...')
            pending_members = self.advisor_pending.filter(
                lambda x: x['Response'] == 'None' and x['ProjectID'] == self.__projectID)
            for member in pending_members.table:
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

    def modify_project(self):
        # Project table needs to be updated
        # project proposal
        if self.status == 'advisor':
            print('Editing project fields...')
            self.view_project()
            choice = _check_input_v2(['1', '2'], 'Add comments?,yes(1)/no(2): ')
            if choice == '1':
                long_text('Comments', self.__project_proposal)



        else:
            while True:
                print('What field do you want to modify?')
                print("1.Abstract\n2.Goals\n3.Timeline\n4.Budget")  # comment and status are for advisor
                choice = _check_input_v2(['1', '2', '3', '4'], 'Action: ')
                # for key in self.__project_proposal.table:
                #     temp = key.values()
                if choice == 'Q':
                    break
                # print(66666,self.__project_proposal.table['Timeline'])
                if choice == '1':
                    long_text('Abstract', self.__project_proposal)
                elif choice == '2':
                    long_text('Goals', self.__project_proposal)
                elif choice == '3':
                    long_text('Timeline', self.__project_proposal)
                elif choice == '4':
                    long_text('Budget', self.__project_proposal)
            # print(self.__project_proposal)




    def random_team(self):
        for _ in range(3):  # faculty members will evaluate their project
            picked = random.choice(self.__eval_team.table)
            if picked not in self.__random:
                self.__random.append(picked)
        # print(len(self.__eval_team.table))
        # print(self.__random)

    @property
    def project(self):
        return self.__project

    @property
    def projectID(self):
        return self.__projectID






# make sure all project proposal and report approved
class Evaluation:
    weight_func = 0.4
    weight_creativity = 0.3
    weight_usability = 0.2
    weight_adherence = 0.1

    def __init__(self,db,project):
        self.__db = db
        self.__project = project
        self.__evaluation = self.__db.search('evaluation')
        # self.__evaluation.insert({'ProjectID': self.__project['ProjectID'],
        #                           'Title': self.__project["Title"],
        #                           'Functionality':'None',
        #                           'Creativity':'None',
        #                           'Usability':'None',
        #                           'Adherence_to_requirements': 'None',
        #                           'Total': 'None'})


    def view_criteria(self):
        print("""Functionality 40%
5: Excellent 4: Good, 3: Satisfactory,2: Needs Improvement,1: Poor

Creativity 30%
5: Highly Creative, 4: Creative 3: Average 2: Limited Creativity 1: Lacks Creativity

Usability 20%
5: Very User-Friendly 4: User-Friendly3: Acceptable Usability,2: Some Usability Issues,1: Poor Usability

Adherence to Requirements 10%
5: Fully Adheres,4: Mostly Adheres,3: Partial Adherence,2: Limited Adherence,1: Does Not Adhere""")



    def rate_criteria(self,project_id):
        choice = _check_input(['1','2','3','4'],'Which criteria do you want to modify?')
        if choice == '1':
            print('Functionality 40%\n5: Excellent 4: Good, 3: Satisfactory,2: Needs Improvement,1: Poor')
            functionality  = _check_input(['1', '2', '3', '4','5'], 'Enter: ')
            self.__evaluation.update('Functionality',int(functionality))

        if choice == '2':
            print('Creativity 30%\n5: Highly Creative, 4: Creative 3: Average 2: Limited Creativity 1: Lacks Creativity')
            creativity = _check_input(['1', '2', '3', '4', '5'], 'Enter: ')
            self.__evaluation.update('Creativity', int(creativity))

        if choice == '3':
            print('Usability 20%\n5: Very User-Friendly 4: User-Friendly3: Acceptable Usability,2: Some Usability Issues,1: Poor Usability')
            usability = _check_input(['1', '2', '3', '4', '5'], 'Enter: ')
            self.__evaluation.update('Usability', int(usability))


        if choice == '4':
            print('Adherence to Requirements 10%\n5: Fully Adheres,4: Mostly Adheres,3: Partial Adherence,2: Limited Adherence,1: Does Not Adhere')
            adherence_to_requirements = _check_input(['1', '2', '3', '4', '5'], 'Enter: ')
            self.__evaluation.update('Adherence_to_requirements', int(adherence_to_requirements))

        print(self.__evaluation)




class Student(Project, Mail):
    def __init__(self, DB, info):
        self.__DB = DB
        self.__member_pending = DB.search('member_pending_request')
        self.__advisor_pending = DB.search('advisor_pending_request')
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


    @property
    def ext(self):
        return self.__ext

    @property
    def login_db(self):
        return self.__login_db

    @property
    def DB(self):
        return self.__DB

    @property
    def advisor_pending(self):
        return self.__advisor_pending

    @property
    def member_pending(self):
        return self.__member_pending

    @property
    def student_info(self):
        return self.__student_info

    def __change_status(self, role):  # lead ver
        self.status = role
        self.__login_db.filter(lambda x: x['ID'] == self.id).update('role', role)
        self.__ext.filter(lambda x: x['ID'] == self.id).update('role', role)

    def __check_status(self):
        if self.status == 'student':
            # print(self.status)
            return True  # only not lead and member can create project
        return False

    def project_info(self):
        member = 1  # someone who's not member does not work
        if self.status != 'student':
            if self.status == 'lead':
                _project_info = self.project.filter(lambda x: x['Lead'] == self.name)
            # print(_project_info)
            else:
                _project_info = self.project.filter(lambda x: x[f'Member{member}'] == self.name)
            # member+=1
            _project_id = _project_info.table[0]['ProjectID']
            # print(77,_project_id)
            return _project_info, _project_id


    # lead---------------------
    def send(self, _project_id):
        # print(self.project)
        print('Who do you want to send an invitation to?')
        # fIX loop pass the person who already got invitation by that user
        # looking for student only and had not been invited yet
        temp = []
        __pending = self.__member_pending.filter(lambda x: x['ProjectID'] == _project_id).select(
            ['to_be_member', 'ProjectID', 'Response'])  # all requests sent by lead

        __advisor_pend = self.__advisor_pending.filter(lambda x: x['ProjectID'] == _project_id).select(
            ['to_be_advisor', 'ProjectID', 'Response'])  # all requests sent by lead
        print('1.Students\n2.Faculty')
        # print(len(__advisor_pend))
        # print(555,temp)

        choice = _check_input_v2(['1', '2'], 'Action: ')
        if choice == '1':
            if len(__pending) != 0:
                for user in __pending:  # check whether this user request was sent?
                    # print(len(__pending))
                    temp.append(user['to_be_member'])
                    # print(temp)
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
            # print(__advisor_pend)
            # old req was view and response(accept/decline)
            # if len(__advisor_pend)!= 0:
            # print(__advisor_pend[0]['Response'])
            # if user['Response'] != 'None' and user[0]['Response'] != 'None':

            if len(__advisor_pend) > 0:  # second time have to check whether request had sent to this faculty
                for user in __advisor_pend:
                    temp.append(user['to_be_advisor'])  # can invite any faculty member
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

            # print(temp)
        # print(__pending)
        # print(__advisor_pend)
        # print(self.__advisor_pending)

    # temp.clear()
    # print(self.__member_pending)

    def __view(self):
        # will show people that lead can send request to
        print('All students')
        for student in self.__ext.filter(lambda x: x['role'] == 'student').select(['first', 'last', 'username']):
            print(f"first: {student['first']}, lastname: {student['last']}, username: {student['username']}")
            print()

    def main(self):
        print(self.status)
        if not self.__check_status():
            self.__my_project, self.my_project_id = self.project_info()
            # print(self.__my_project)
        print(self.__student_info)
        # print(self.id, self.firstname, self.status)
        # print(self.lead, self.member1, self.member2)
        # print()
        while True:
            print(self.status)
            print(f'Welcome {self.firstname} {self.lastname[0]}.')
            print('What do you want to do?')
            print('1.Create project\n2.My project\n3.Send invitation\n4.My mailbox')
            choice = _check_input_v2(['1', '2', '3', '4'], 'Action: ')
            print('+------------------------------------+')
            if choice == 'Q':
                break
            if not self.__check_status():
                self.__my_project, self.my_project_id = self.project_info()
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
                if self.status != 'student':
                    print(77777, self.my_project_id, self.__my_project)
                    self.project_menu(self.__my_project)
                else:
                    print("The project do not exists.")
                    print('Create project first.')
            elif choice == '3':
                # print all students
                if not self.__check_status() and self.status == 'lead':
                    self.send(self.my_project_id)
                else:
                    print('Only the lead is eligible to send invitations.')

            elif choice == '4':
                super().mailbox(self.status)
            # print(self.__student_info)
            # print(self.id, self.firstname, self.status)
            # print(self.lead, self.member1, self.member2)
            print(self.project)
            print(self.__login_db)
            print(self.__student_info)
            print('+------------------------------------+')



class Faculty(Project,Mail,Evaluation):
    def __init__(self, DB, info):
        # access self.DB self.member_pending
        self.__DB = DB
        self.id = info[0]

        self.__login_db = DB.search('login')

        self.__advisor_pending = DB.search('advisor_pending_request')
        self.__ext = DB.search('joined_person_login')
        self.__faculty_info = self.__ext.filter(lambda x: x['ID'] == self.id).table[0]
        self.firstname = self.__faculty_info['first']
        self.lastname = self.__faculty_info['last']
        self.username = self.__faculty_info['username']
        self.__eval_projects = self.__DB.search('mail').filter(lambda x: x['evaluation_team'] == self.username)
        self.name = f'{self.firstname} {self.lastname}'
        self.status = self.__faculty_info['role']
        self.__project = DB.search('project').filter(lambda x: x['Advisor'] == self.name)

    @property
    def login_db(self):
        return self.__login_db

    @property
    def advisor_pending(self):
        return self.__advisor_pending

    @property
    def DB(self):
        return self.__DB

    @property
    def faculty_info(self):
        return self.__faculty_info

    @property
    def ext(self):
        return self.__ext

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
    @staticmethod
    def check_eval(eval_projects):
        if len(eval_projects.table) > 0:
            return True
        return False
    def main(self):
        # print(self.__faculty_info)
        print(self.__eval_projects)
        print(self.__DB)
        print(5535454, self.status)
        while True:
            print(self.status)
            print(f'Welcome {self.firstname} {self.lastname[0]}.')
            print('What do you want to do?')
            print('1.View my project\n2.Modify project\n3.My mailbox\n4.Evaluate project')
            choice = _check_input_v2(['1', '2', '3','4'], 'Action: ')
            print('+------------------------------------+')
            # if choice == 'Q':
            #     break
            # if choice == '1':

            # print(my_project)

            if choice == 'Q':
                break
            if choice == '2':
                my_project = self.view_my_project()
                super().project_menu_2(my_project)

            if choice == '3':
                self.mailbox('faculty')
                # print(self.status)
            #
            if choice == '4':
                if Faculty.check_eval(self.__eval_projects):
                    project = self.pick_to_eval()
                    # print(project['ProjectID'])
                    super().view_criteria()
                    super().rate_criteria(project['ProjectID'])
