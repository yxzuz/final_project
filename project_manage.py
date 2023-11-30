# import database module
from database import Table, Database, ReadCsv


# define a function called initializing
DB = Database()
def initializing():
    read_person = ReadCsv('persons.csv')
    my_person = read_person.read()
    table1 = Table('persons', my_person)
    read_login = ReadCsv('login.csv')
    my_login = read_login.read()
    table2 = Table('login', my_login)
    # add all these tables to the database
    DB.insert(table1)
    DB.insert(table2)
    # print(table1)
    # print(dir(DB))
    # print(table2)
    # print(DB)
    # return DB, table1, table2

initializing()
for table in DB.database:
    print(table.table_name)

# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files

# see the guide how many tables are needed


# define a function called login
# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

def login(DB):
    print('-------Login-------')
    user = input('Enter your username: ')
    pas = input('Enter your password: ')
    for x in DB.search('login').table:

        # print(111,x)
        # print(x['username'],user,x['password'],pas)
        if x['username'] == user and x['password'] == pas:
            return [x['ID'], x['role']]
    return None




# define a function called exit
def exit():
    pass


# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


val = login(DB)
print(val)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
# see and do admin related activities
# elif val[1] = 'student':
# see and do student related activities
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