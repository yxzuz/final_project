# **TODO LIST**
#SO WE NEED TO MAKE CLASS IN ANOTHER FILE AND IMPORT  
#NOTE ROLE WILL CHANGE eg. student to member/lead, faculty to advisor

## An admin
**add in code for adding user to database**    
define a function called add_user  
here are things to do in this function:  
    add code that performs adding user
        ask user for person_id, first, last, type
        return their username and password if added successfully

**add in code for deleting user from database**  
define a function called delete_user  
here are things to do in this function:  
    add code that performs deleting user
        ask user for username to delete
        ask user for confirmation 'Are you sure you want to delete first last?'  
        print('Username was deleted successfully') if deleted successfully

**update user field**  
define a function called update_user  
here are things to do in this function:  
    add code that performs updating user
        ask user for username to update
        ask user for field to update (first, last, password)  
        if password was chosen, ask for old password for confirmation  
        ask user for confirmation 'Are you sure you want to update thing?'  
        print('Updated successfully') if updated successfully

## **A lead student**  

**Create a project**  
define a function called create_project  
here are things to do in this function:  
    add code that performs creating project
    ask user for project name and project details
    save project details

**See project status**  
define a function called project status
here are things to do in this function:  
    this function will make use of existed project table in DB and access to it status

**See and modify his own project details**  
define a function called modify_project   
here are things to do in this function:  
    add code that performs modifying project
        ask user for project name and ask what project details to update  
        save project details into project table

**Send invitational messages to potential members**  
define a function called invite_member   
here are things to do in this function: 
    add code that performs invitation members
        ask user for project name and student's username for potential members
        save invitation message into user's inbox and update Member_pending_request table

**Send request messages to potential advisors**  
define a function called request_advisor   
here are things to do in this function:  
    add code that performs requesting advisors
        ask user for project name and student's username for potential advisor
        save request message into user's inbox and update Advisor_pending_request table

  
**Submit the final project report**    
define a function called submit_project   
here are things to do in this function:  
    ask user for project name and add project report   
    ask user for confirmation
    print('Submit successfully') if saved successfully

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

## **An advising faculty**  

**See request to be a supervisor**  
**Send accept response (for projects eventually serving as an advisor)**  
**Send deny response (for projects not eventually serving as an advisor)**  
    make calls to check_inbox to check requests to be a supervisor msg  
    ask user for answer to a request to be a supervisor  
    if user accept:
        add supervisor to project
        update the request status in inbox to accept
        print('You accepted to be a supervisor')  
    else:
        update the request status in inbox to deny
        print('You denied to be a supervisor')

**See details of all the project**  
    make calls to project tables that have this user as their advisor to show details  

**Approve the project** 
    make calls to cal_score (see detail in Proposal.md)
    if the net scores is acceptable:
        save project status to Approve
        Print('Project Approved')
    else:
        Print('Please fix the project.')

