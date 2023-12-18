# **TODO LIST**
#SO WE NEED TO MAKE CLASS IN ANOTHER FILE AND IMPORT  
#NOTE ROLE WILL CHANGE eg. student to member/lead, faculty to advisor

## An admin
**check_user**  
check whether the username existed  
return True or False  

**check_input**  
check if user's input suits the condition

**add in code for adding user to database**  
define a function called add_new_user 
here are things to do in this function:  
* add code that performs adding user
* ask user for firstname, lastname and role
* then generate password and username and insert to login, joined_person_login and persons table.


**add in code for reset user's password**    
define a function called reset_password  
**NOTE: affect: login and joined_person_login table**  
here are things to do in this function:  
* add code that performs reset user's password  
* ask user for person's username

**add in code for deleting user from database**  
define a function called delete_user  
here are things to do in this function:
* add code that performs deleting user
* ask user for username to delete
* ask user for confirmation 'Are you sure you want to delete account'  
* print('Username was deleted successfully') if deleted successfully
* update login table

**update user field**  
define a function called update_user  
here are things to do in this function:  
add code that performs updating user's info
ask user for username to update stuff  

**see rows**  
define a function called update_user  
here are things to do in this function:  
ask for row and display it
----------

# **Additional Class**  
## Evaluation class
## Mail class
## project class
-**Create a project**(Only for lead)   
here are things to do in this function:  
add code that performs creating project
    ask user for project name and project details
    save project details  
    update project, project_proposal, project_report table

-**initialization(self, my_project_id, my_project)**(Only for lead and members)   
here are things to do in this function:  
initialize attributes for members and lead


-**project_menu(self,my_project_id,my_project)**(Only for lead and members)   
here are things to do in this function:  
call functions and for display

-**change_title**(Only for lead and members)   
here are things to do in this function:  
change project's title
update project table

-**See project status**(Only for lead and members) 
(pending member, pending advisor, or ready to solicit an advisor)  
define a function called project status   
here are things to do in this function:  
this function will make use of existed project table in DB and access to it status   
**Note: Project table needs to be updated**
  
-**See and modify his own project details**  
define a function called modify_project   
here are things to do in this function:  
    add code that performs modifying project
        ask user for project name and ask what project details to update  
        save project details into project table
  


----------
## **student**  
-See **pending requests** to become members of existed projects  
-**Accept or deny the requests**   
Member_pending_request table needs to be updated   
Project table needs to be updated   

-**Create a project**   
inherit from project class  
**_Note:student must deny all member requests first_**  
then student change role to become a lead  
**_Project table_** and _**Login table**_ needs to be updated  
  
If more members needed, send out requests and update the member_pending_request table  




----------

## **A lead student**  


**Project table needs to be updated**




Advisor_pending_request table needs to be updated

**See project status**  

**See and modify his own project details**

**See who has responded to the requests sent out**

**Send invitational messages to potential members**  
_**_Note: requests can only go to those whose role is student_**_  
**Member_pending_request table needs to be updated** 	
define a function called invite_member   
here are things to do in this function:   
* add code that performs invitation members
* ask user for project name and student's username for potential members
* save invitation message into user's inbox and update Member_pending_request table

**Send request messages to potential advisors**   

**Note: Send out requests to a potential advisor can only do one at a time 
and after all potential members have accepted or denied the requests**
define a function called request_advisor   
here are things to do in this function:  
*    add code that performs requesting advisors
*    ask user for project name and student's username for potential advisor
*    save request message into user's inbox and update Advisor_pending_request table

  
**Submit the final project report**    
define a function called submit_project   
here are things to do in this function:  
    ask user for project name and add project report   
    ask user for confirmation
    print('Submit successfully') if saved successfully


----------
## **A member student**  
**See project status**  
define a function called project status  
here are things to do in this function:  
    this function will make use of existed project table in DB and access to its status


**See who has responded to requests**
note: it's either other potential member or advisor
define a function called check_inbox   
here are things to do in this function:  
    add code that performs checking inbox

**See and modify his project details**  
    make calls to modify_project (only allow the project that user's a member of.)

----------
## **A normal faculty who is not an advisor**  

**See request to be a supervisor**  
**Send response denying to serve as an advisor**
    make calls to check_inbox by make use of to_be_advisor table to check requests to be a supervisor msg 
    also able to deny requests

**See details of all the project**  
define a function called list_project   
here are things to do in this function:
    add code that performs listing project
        show all project and details  

**Evaluate projects** (this is the missing step that you will explain in your proposal; see details in the tasks below)

----------
## **An advising faculty**  

**See request to be a supervisor** 


**Send accept response (for projects eventually serving as an advisor)** 

**Send deny response (for projects not eventually serving as an advisor)**  
    make calls to check_inbox to check requests to be a supervisor msg  
    ask user for answer to a request to be a supervisor  
    if user accept:
* add supervisor to project
* update the request status in inbox to accept
* print('You accepted to be a supervisor')    

else:
* update the request status in inbox to deny
print('You denied to be a supervisor')

MODIFY AND ADD PROJECT FEEDBACK

**See details of all the project**  
    make calls to project tables that have this user as their advisor to show details  

**Approve the project** 
    make calls to cal_score (see detail in Proposal.md)
    if the net scores is acceptable:
        save project status to Approve
        Print('Project Approved')
    else:
        Print('Please fix the project.')

