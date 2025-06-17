# Calculate Your Percentage
#### Video Demo:  <URL https://youtu.be/7gKKfL0YioQ?si=KYboJpS26miOFRhq>
#### Description: My project checks the percentage of various subject's marks out of 100.It also contains 3 quizzes.

## Structure
The project is implemented using Python,Javascript,SQL and Jinja.It has the following files and directories:
- app.py
- README.md
- project.db
- static folder(has:style.css,thisiscs50.jpg,image-english.jpg)
-templates folder(has:layout.html,index.html,login.html,register.html,calculate.html,quizzes subfolder)
 - quizzes subfolder(has:Computer.html,Maths.html,English.html,results.html)
## 1.app.py
This Python script defines a Flask web application for calculating percentage and a quiz platform.It handles user authentication(login,logout,registration),rendering quiz pages(Computers,Maths,English),and checking quiz answers.
Imports various libraries including Flask,SQLite from CS50 Library and functions for password hashing and checking.A secret key has been set for session management.It has SQLite database table named users which stores id,username,password_hash.The routes are:
* a.index route ("/")
Renders the calculate.html page if a user is logged in otherwise it redirects to the login.html page.
* b.login route ("/login")
Clears the session and checks if the username and password provided by the user matches the records in the database(project.db).If the request is successful ,it sets the user_id in the session and redirects to the index page,otherwise to the /login.
* c.logout route ("/logout")
Clears the session and redirects to the "/".
* d.register route ("/register)
Validates the username,password,confimation, hashes the password and inserts the user into the database "users".If "POST" request is received, it extracts username,password,confirmation from the form.Then,validates if the username is provided or not.If not,flashes a message indicating the issue(same for password,confirmation).If the validation passes the checks, the password is hashed using generate_password_hash().Then it inserts the new user's data into the database.If successful the user is redirected to ("/").If username already exists, it flashes a message.
* e.calculate route ("/calculate")
Retrives the grades data submitted through a "POST" request.After converting the grades to floating-point numbers, it computes the total_marks by summing up all the grades.If there is any grade provided,it calculates the percentage by dividing the total_marks/100 multiplied by the number of grades.This value is multiplied by 100 to get the percentage.After all this, the route renders "/calculate.html"
* f.quizzes routes ("/Computers.html", "/Maths.html", "/English.html")
Renders the quiz pages for Computers.html, Maths.html and English.html.
* g.check_answers ("/quizzes/<quiz_name>")
Checks the user's submitted answers for a specific quiz and calculates the score.It compares the submitted answers with the correct_answers and sets the score to +1 if being matched.It renders the results.html page which displays the score with a background image(thisiscs50.jpg).
## 2.index.html
It is written within the {%block title%} section, which contains the HTML markup for the main content of the page.It includes heading(h1) and subheading(h2).Additionally, a link to the("/login") is provided.
## 3.layout.html
Serves as a template for login,register.It includes a title and a navigation bar with links for resgitering, logging in,a section to dispaly flash messages(which uses {%if...else%} condition) and also a main section where the content is inserted using the {%block main%}.The styling is done by using Bootstrap and CSS file style.css
## 4.register.html
It has the code for registering username.The form has been created for the user to input for username,password and confirmation with their respective palceholders.This form will submit data to /register through the "POST" method.The styling has been done using Bootstrap and style.css.Lastly, the overall code is written within the Jinja tag.
## 5.login.html
It has the code for login page.The form is in{%block main%}section,contains the input fields for inserting username,password, with their respective placeholders.This form will send the data to /login through the "POST" method.The styling is done by Bootstrap and style.css.A quote of Guru Raviadss Ji(source:Amritbani Satguru Ravidass Ji) has been added for style.
## 6.calculate.html
Includes the links for login and 3 quizes links.The form has two input fields where the user can input the subject name and Marks Obtained and by clicking on the submit button the overall percentage is displayed.The code block is written within the {%block main%}that defines the main content.Jinja's{%if...endif%}is used for displaying the percentage on the screen.Javascript is used for the user to Add Subjects(for checking 2+ subjects).
## 7.Computers.html,Maths.html,English.html
Computer.html presents quiz.Some of the questions here have been taken from the CS50 Lecture 10 quiz.The content includes link to "/login" and "/calculate".Each question is presented with its respective choices as radio buttons.The form concludes with a submit button and uses "POST" method for submission.After submitting, it directs the user to results.html where the score is displayed.The other two have the same concept as with the Computers.html. It has though questions from my maths book of school,Google,LRN Exam Paper 2021.
## 9.results.html
Uses Jinja syntax{%if...endif %}for displaying the score alsongside with an image thisiscs50.jpg.

