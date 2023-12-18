# Final project for 2023's 219114/115 Programming I
* Starting files for part 1
  - advisor_pending_request.csv 
    - Description: keep track ad pending
  - database.py
    - Description: method to use in all files
  - evaluation.csv
    - Description: keep track of scores when evaluate
  - joined_person_loging.csv
    - Description: for usage when needed mixed tables dta
  - login.csv
    - Description: keep track of login data
  - mail.csv
    - Description: keep track of evaluate request to faculty
    - Purposes:
  - member_pending_request.csv
    - Description: keep track member pending
  - person.py
    - Description: contains all class
  - person.csv
    - Description:  persons data
  - project.csv
    - Description: project data
  - project_manage.py
    - Description: user interface
  - project_proposal.csv
    - Description: when project was modified keep ('project' proposal')
  - project_report.csv
    - Description: when project was modified('project' report')


* How to compile and run:
    - use run = Student(DB,['4788888', 'student']) then run.main() in project_manage.py
#LEAD
#run = Student(DB,['9898118', 'student'])
run.main`
#member ,Manuel.N,1244,student
# run = Student(DB,['5662557', 'student'])
#member2
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

* Table of Role, Action, Method, Class, Completion percentage:
  
| Role            | Action                                                                | Method          | Class   | Completion percentage |
|-----------------|-----------------------------------------------------------------------|-----------------|---------|-----------------------|
| Admin           | delete user from database                                             | delete_user     | Admin   | 100                   |
| Admin           | check wheter this username existed                                    | __checkuser     | Admin   | 100                   |
| Admin           | generrate new password                                                | reset_password  | Admin   | 100                   |
| Admin           | ask for name and create username and password                         | add_new_user    | Admin   | 100                   |
| Admin           | ask admin to update certain filed wth keys                            | update_field    | Admin   | 70                    |
| Admin           | for display key to ask admin                                          | show_key        | Admin   | 100                   |
| Admin           | admin can update certain field                                        | update_field    | Admin   | 70                    |
| Admin           | display row                                                           | __show_row      | Admin   | 90                    |
| Admin           | for running program                                                   | main            | Admin   | 100                   |
| Student         | for viewing msgs and request                                          | mailbox         | Mail    | 100                   |
| Lead            | lead can use to send request to for potential advisor and members     | send            | Mail    | 100                   |
| Student         | automatically decline request when they accepted to join some project | decline_request | Mail    | 100                   |
| Lead            | for sending request to faculty to evaluate project                    | random_team     | mail    | 100                   |
| -               | Adding memebers to project once they accepted requewt                 | add_members     | Mail    | 100                   |
| Advisor/Faculty | To pick and they will later on modify (return picked project)         | view_project    | faculty | 100                   |
| Advisor/Faculty | for usage later on in clas Project                                    | initialzation   | faculty | 100                   |
| -               |                                                                       |                 |         |                       |
|                 |                                                                       |                 |         |                       |

 * List of missing features and outstanding bugs:
   - login doesn't work so you have tp run progrma in a method above



