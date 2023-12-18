# ****Evaluation Process****  

NOTE(s):   
**Each project will have 3 (random) faculty members to grade them**   
Each project have 2 submission to finish this project
1. project proposal and checked by their advisor (status:approved/declined)
2. project report and checked by their advisor (status:approved/declined)
3. advisor mark project as approved
4. student send request for evaluation
5. evaluation team will rate the score and change Evaluation table score 
6. and change status project to pass/fail  

Need 50% to pass the project

**criteria for evaluation process (grading) by faculty**  
ProjectID 20%  
Functionality 20%  
Creativity 20%  
Effectiveness 20%  
Relevance 20%
Impact 20%
---
**1.See detail of the final project report**  
-make calls to list_project and look into the final project report

**2.Rate score of each topic**  
define a function called rate_score   
here are things to do in this function  
    -user(faculty members) will rate the score from each criterion  
    -stores the score in evaluation.csv  
    -change project status from approved(need to be approved first then it will be evaluated) to pass/fail

**3.Calculate total score**  
define a function called cal_score   
here are things to do in this function
    add code that performs calculation score
        -calculate the scores from scores data
        -return scores/100
