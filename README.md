# Final project for 2023's 219114/115 Programming I
* Starting files for part 1
  - advisor_pending_request.csv 
    - Description: keep track of advisor pending datas
  - database.py
    - Description: essential methods to use in database and tables such as update, select, search, filter, has read and write csv files
    - class Database: can insert tables and search for tables with name
    - class ReadCsv: read csv file as dict
    - class Table: insert dict to table, update table, delete table, filter, select table with keys and etc.
  - evaluation.csv
    - Description: keep track of ProjectID,Functionality,Creativity,Effectiveness,Relevance,Impact,Total (For evaluation process). The selected faculty members will evaluate the project adn rate the score by each criterion
  - joined_person_login.csv
    - Description: for usage when needed mixed tables data. It has user's ID,first,last,type,username,password,role
  - login.csv
    - Description: keep track of login data
  - mail.csv
    - Description: keep data of mails(notifications) sent to picked evaluation team sent by lead has keys = ProjectID,evaluation_team (1 project will have 3 members),Date_sent 
  - member_pending_request.csv
    - Description: keep track of member pending that lead sent requests
  - person.py
    - Description: contains all class and methods for each role. When logged in from project_manage.py they will enter different class depends on their role which is a data in database. 
    - class Student: Note: this class also use methods from clas Mail person type 'student' with role('lead', 'member', 'student)  can use this class. They can create project(role != 'member' and 'lead') (inherits from class Project), edit project, see mail, send requests
    - class Faculty: role required to use this class is 'faculty' and 'advisor'. user can modify project(if role == 'advisor') and they are also able to read mails from lead. Some faculty members are able to Evaluate project(role must be faculty)
    - class Project: class student inherits from here. It has methods for creating project, add comments , change projects status, display pending and notify when the project was approved by advisor which is a step before actually sending for evaluation team to mark their project as pass/ fail
    - class Mail: All roles except admin will use this for communicating among each other
    - class Evaluation: have methods to calculate scores by criteria
  - person.csv
    - Description:  persons data
  - project.csv
    - Description: project data
  - project_manage.py
    - Description: user will use this file to log in
  - project_proposal.csv
    - Description: when project was modified keep ('project' proposal')
  - project_report.csv
    - Description: when project was modified('project' report')


* How to compile and run:
* There are 2 ways to run code
1. if you run code with COMMIT 8356cb04e9d82575dad603e83be9ee378539165a (the most recent one) (preferable to use this one)
run the program in project_manage.py and run function login
2. if you run code with COMMIT 680135c4b532be350abe91babd84e1045156ba50
- use run = Student(DB,['4788888', 'student']) then run.main() in project_manage.py
FOR ADMIN
run = Admin(DB, ['8466074', 'faculty'])
run.main()
FOR LEAD
run = Student(DB,['9898118', 'student'])
run.main()
FOR MEMBER
run = Student(DB,['5662557', 'student'])
run.main()
FOR FACULTY (same class as advisor)
run = Faculty(DB, ['8466074', 'faculty'])
run.main()
FOR ADVISOR (same class as faculty)
run = Faculty(DB, ['8466074', 'faculty'])
run.main()


* Table of Role, Action, Method, Class, Completion percentage:
  
| Role                     | Action                                                                                                                                 | Method                           | Class      | Completion percentage |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|------------|-----------------------|
| Admin                    | delete user from login.csv                                                                                                             | delete_user                      | Admin      | 100                   |
| Admin                    | check the input to make sure it comes out in certain value                                                                             | _check_input and _check_input_v2 | -          | 70                    |
| Admin                    | use for randomize password and things in certain range                                                                                 | _generate_thing                  | -          | 100                   |
| Admin                    | Find keys and return for choice Update table                                                                                           | _find_keys                       | Admin      | 100                   |
| Except Admin             | ask for txt and update value to its table                                                                                              | long_text                        | -          | 75                    |
| Admin                    | check whether this username existed                                                                                                    | __check_user                     | Admin      | 100                   |
| Admin                    | generate new password                                                                                                                  | reset_password                   | Admin      | 100                   |
| Admin                    | ask for name and create username and password                                                                                          | add_new_user                     | Admin      | 100                   |
| Admin                    | ask admin to update certain filed wth keys                                                                                             | update_field                     | Admin      | 100                   |
| Admin                    | for display key to ask admin                                                                                                           | show_key                         | Admin      | 100                   |
| Admin                    | admin can update certain field                                                                                                         | update_field                     | Admin      | 100                   |
| Admin                    | display row                                                                                                                            | __show_row                       | Admin      | 20                    |
| Admin                    | (for running) add user to database,delete user from database,reset password,update table,see rows                                      | main                             | Admin      | 100                   |
| Student,Advisor,Faculty  | for viewing msgs and and accept / decline requests , adding person to project , Notify faculty to evaluate project                     | mailbox                          | Mail       | 100                   |
| Lead                     | sent evaluation notifications to evaluation team                                                                                       | sent_eval_notification           | Mail       | 100                   |
| Lead                     | lead can use to send request to for potential advisor and members, will notify when project's approved                                 | send                             | Mail       | 100                   |
| Student                  | automatically decline other requests in pending when they accepted to join a project                                                   | decline_request                  | Mail       | 100                   |
| Lead                     | for sending request to faculty to evaluate project                                                                                     | random_team                      | mail       | 100                   |
| Except admin             | Adding members to project once they accepted request                                                                                   | __add_members                    | Mail       | 100                   |
| Student                  | They will change status once they accept lead's invitation                                                                             | __change_status                  | Mail       | 70                    |
| Student                  | insert initial project, project_report, project_proposal to their csv                                                                  | create_project                   | Project    | 80                    |
| Lead,member              | check all projects' sub status and return True if it's ready to be evaluated                                                           | __check_status                   | Project    | 100                   |
| Lead,member              | Display menu about project and notify if the project was approved by advisor                                                           | project_menu                     | Project    | 100                   |
| Advisor                  | Display menu about project ( 1.Modify project 2.Change project status(proposal,report,overall))                                        | project_menu_2                   | Project    | 70                    |
| Lead,member              | All project group to change title                                                                                                      | change_title                     | Project    | 100                   |
| Lead,member              | change project's status when all member is fulfilled                                                                                   | change_project_status            | Project    | 100                   |
| Lead,member              | Show project current status such as pending advisor, members and notify user to contact when all project parts was approved by advisor | see_project_status               | Project    | 100                   |
| Advisor                  | Show project's proposal data                                                                                                           | view_project                     | Project    | 80                    |
| Lead,Member,Advisor      | let user's modify project content, advisor can add comments to project proposal, report                                                | modify_project                   | Project    | 60                    |
| Faculty(Evaluation team) | let evaluation team view project's score criteria                                                                                      | view_criteria                    | Evaluation | 100                   |
| Faculty(Evaluation team) | check if the current evaluation existed (just for usage in rate_criteria method)                                                       | __check_eval_existance           | Evaluation | 100                   |
| Lead, Member             | return pending advisors and pending members for user                                                                                   | find_pending_members             | Student    | 100                   |
| Lead                     | update user role in login.csv and ext table when student created project                                                               | __change_status                  | Student    | 100                   |
| Lead,Member              | for checking status note: only not lead and member can create project (for usage in create_project)                                    | __check_status                   | Student    | 100                   |
| Lead, Member             | return user's project info                                                                                                             | project_info                     | Student    | 100                   |
| Lead                     | will show people that lead can send request to                                                                                         | __view                           | Student    | 100                   |
| Lead, Member             | setting up attribute for class Project                                                                                                 | __initialization                 | Student    | 70                    |
| Student, Lead, Member    | Greet user,  Give options for user to 1.Create project 2.My project 3.Send invitation 4.My mailbox                                     | main                             | Student    | 100                   |
| Faculty(Evaluation team) | Let faculty who is on evaluation team pick which project they want to evaluate                                                         | pick_to_eval                     | Student    | 100                   |
| Advisor and Faculty      | let user pick from options 1.Modify project 2.My mailbox 3.Evaluate project                                                            | main                             | Faculty    | 100                   |
| Faculty(Evaluation team) | check numbers of project they have to evaluate                                                                                         | check_eval                       | Faculty    | 100                   | 
| Advisor,Faculty          | To pick and they will later on modify (return picked project)                                                                          | view_my_project                  | Faculty    | 100                   |
| Advisor,Faculty          | setting up attribute for class Project                                                                                                 | __initialzation                  | Faculty    | 100                   |
| Faculty                  | display score criteria                                                                                                                 | view_criteria                    | Evaluate   | 100                   |
| Faculty                  | rate scores and update involved project, evaluation table                                                                              | rate_criteria                    | Evaluate   | 100                   |
| Faculty                  | calculate net scores/100                                                                                                               | total                            | Evaluate   | 100                   |


* List of missing features and outstanding bugs:
   - login should get role from login.csv not by user simply typing (I have fixed and committed code)
   - class Project method: modify_project should fix missing while looping (I have fixed and committed code)
   - project status(when advisor updated it) it affected whole table(I have fixed and committed code)
   - admin cannot see row




