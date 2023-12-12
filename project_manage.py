
from database import Table, Database, ReadCsv, WriteCsv
from person import Admin,Student

# define a function called initializing
DB = Database()
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

    # read_joined_table = ReadCsv('joined_person_login.csv')
    # my_ext = read_joined_table.read()
    my_ext = table1.join(table2, 'ID')
    my_ext.table_name = 'joined_person_login'
    # table6 = Table('joined_person_login', my_ext)

    # add all these tables to the database
    DB.insert(table1)
    DB.insert(table2)
    DB.insert(table3)
    DB.insert(table4)
    DB.insert(table5)
    DB.insert(my_ext)

initializing()
# for dict in DB.search('persons').table:
#     for val in dict.values():
#         print(val)
# for table in DB.database:
#     print(table.table_name)

# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files

# see the guide how many tables are needed


# define a function called login
# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# def login(DB):
#     print('-------Login-------')
#     user = input('Enter your username: ')
#     pas = input('Enter your password: ')
#     for x in DB.search('login').table:
#
#         # print(111,x)
#         # print(x['username'],user,x['password'],pas)
#         if x['username'] == user and x['password'] == pas:
#             return [x['ID'], x['role']]
#     return None




# define a function called exit
# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python

def exit():
    WriteCsv('persons.csv', DB,'persons',['ID','first','last','type'])
    WriteCsv('login.csv', DB, 'login', ['ID','username','password','role'])
    WriteCsv('project.csv', DB, 'project', ['ProjectID','Title','Lead','Member1','Member2','Advisor','Status'])
    WriteCsv('advisor_pending_request.csv', DB, 'advisor_pending_request', ['ProjectID','to_be_advisor','Response','Response_date'])
    WriteCsv('member_pending_request.csv', DB, 'member_pending_request', ['ProjectID','to_be_member','Response','Response_date'])
    WriteCsv('joined_person_login.csv', DB, 'joined_person_login', ['ID','first','last','type','username','password','role'])


# temp = {
#     "ProjectID": "1234567",
#     "to_be_advisor": "Sii",
#     "Response": "god",
#     "Response_date": "Super God"
# }
# DB.search("advisor_pending_request").insert(temp)
# print(DB.search("advisor_pending_request").table)
# temp = {
#         'ID':'1234',
#     'first' :'Mary',
#     'last':'kar',
#     'type':'test',
#     'username' : 'mart.R',
#     'password': '1245',
#     'role' : 'mroe'
#     }
# DB.search("joined_person_login").insert(temp)
# print(DB.search("joined_person_login").table)
# val = login(DB)
# print(val)


# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

#
# if val[1] == 'admin':
# run = Admin(DB)
# run.main()
# if val[1] == 'student':
# run = Student(DB,['9898118', 'student'])
# run.main()
# print(type(DB.search('project').table))
# print(type(DB.search('login').table))
# print((type(DB.search('persons_joins_login').table)))
# for i in DB.search('login').table:
#     print(i)
# for i in DB.search('joined_person_login').table:
#     print(i)
# elif val[1] = 'member':
# see and do member related activities
# elif val[1] = 'lead':
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities

# once everything is done, make a call to the exit function
exit()