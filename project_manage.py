
from database import Table, Database, ReadCsv, WriteCsv

from person import Admin, Student, Faculty, Evaluation
from person import _check_input

# define a function called initializing
DB = Database()
_login_user = []
_login_pass = []

def initializing():
    read_person = ReadCsv('persons.csv')
    my_person = read_person.read()
    table1 = Table('persons', my_person)

    read_login = ReadCsv('login.csv')
    my_login = read_login.read()
    table2 = Table('login', my_login)

    read_project = ReadCsv('project.csv')
    my_project = read_project.read()
    table3 = Table('project', my_project)

    read_advisor_pending = ReadCsv('advisor_pending_request.csv')
    my_advisor_request = read_advisor_pending.read()
    table4 = Table('advisor_pending_request', my_advisor_request)

    read_member_pending_request = ReadCsv('member_pending_request.csv')
    my_member_request = read_member_pending_request.read()
    table5 = Table('member_pending_request', my_member_request)

    my_ext = table1.join(table2, 'ID')
    my_ext.table_name = 'joined_person_login'

    read_proposal = ReadCsv('project_proposal.csv')
    my_proposal = read_proposal.read()
    proposal = Table('project_proposal', my_proposal)

    read_report = ReadCsv('project_report.csv')
    my_report = read_report.read()
    report = Table('project_report', my_report)

    read_eva = ReadCsv('evaluation.csv')
    my_evaluation = read_eva.read()
    evaluation = Table('evaluation', my_evaluation)

    read_eva = ReadCsv('mail.csv')
    my_mail = read_eva.read()
    mail = Table('mail', my_mail)
    # add all these tables to the database
    DB.insert(table1)
    DB.insert(table2)
    DB.insert(table3)
    DB.insert(table4)
    DB.insert(table5)
    DB.insert(my_ext)
    DB.insert(proposal)
    DB.insert(report)
    DB.insert(evaluation)
    DB.insert(mail)

    for i in DB.search('login').table:
        _login_user.append(i['username'])
    for i in DB.search('login').table:
        _login_pass.append(i['password'])


initializing()

# here are things to do in this function:
# create an object to read all csv files that will serve as a persistent state for this program
# create all the corresponding tables for those csv files

# see the guide how many tables are needed
# define a function called login
# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None


def login(db):
    print('-------Login-------')
    user = _check_input(_login_user, 'Enter your username: ', 'Please enter valid username')
    pas = _check_input(_login_pass, 'Enter your password: ', 'Please enter valid password')
    for x in db.search('login').table:
        if x['username'] == user and x['password'] == pas:
            if x['role'] == 'lead' or x['role'] == 'member':
                role = 'student'
                return [x['ID'], role]
            elif x['role'] == 'advisor' or x['role'] == 'faculty':
                role = 'faculty'
                return [x['ID'], role]
            else:
                return [x['ID'], x['role']]
    return None

# define a function called exit
# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python

def exit():
    WriteCsv('persons.csv', DB, 'persons', ['ID', 'first', 'last', 'type'])
    WriteCsv('login.csv', DB, 'login', ['ID', 'username', 'password', 'role'])
    WriteCsv('project.csv', DB, 'project', ['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status'])
    WriteCsv('advisor_pending_request.csv', DB, 'advisor_pending_request', ['ProjectID', 'to_be_advisor', 'Response', 'Response_date'])
    WriteCsv('member_pending_request.csv', DB, 'member_pending_request', ['ProjectID', 'to_be_member', 'Response', 'Response_date'])
    WriteCsv('joined_person_login.csv', DB, 'joined_person_login', ['ID', 'first', 'last', 'type', 'username', 'password', 'role'])
    WriteCsv('project_proposal.csv', DB, 'project_proposal', ['ProjectID', 'Title', 'Abstract', 'Goals', 'Timeline', 'Budget', 'Comments', 'Status'])
    WriteCsv('project_report.csv', DB, 'project_report', ['ProjectID', 'Title','Conclusion','Comments', 'Status'])
    WriteCsv('evaluation.csv', DB, 'evaluation', ['ProjectID', 'Functionality', 'Creativity', 'Effectiveness', 'Relevance', 'Impact', 'Total'])
    WriteCsv('mail.csv', DB, 'mail', ['ProjectID', 'evaluation_team', 'Date_sent'])

# val = login(DB)

# print(val)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# due to the errors I have to return login in such weird manner but my class is divide into these three sub cultures
# run = Student(DB,['4788888', 'student'])
# if val[1] == 'admin':
#     run = Admin(DB, val)
#     run.main()
# elif val[1] == 'student':
#     # for all students members and lead
#     run = Student(DB, val)
#     run.main()
# elif val[1] == 'faculty':
#     # for both faculty and advisor (same class)
#     run = Faculty(DB, val)
#     run.main()
#LEAD
# run = Student(DB,['9898118', 'student'])

#mem1 ,Manuel.N,1244,student
# run = Student(DB,['5662557', 'student'])
# run.main()
#mem2
# run = Student(DB,['5687866', 'student'])

#other project lead
# run = Student(DB,['3938213', 'student'])

#faculty
# run = Faculty(DB, ['8466074', 'faculty'])
#
#eval
# run =Faculty(DB,['2472659', 'faculty'])

#eval2

# run =Faculty(DB,['2567260', 'faculty'])
# run.main()
#my login does not work so use id and person type advisor use faculty and faculty also use faculty (same class)
run = Faculty(DB, ['8466074', 'faculty'])
run.main()
exit()