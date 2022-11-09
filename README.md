
# Django Ecommerce Website Task 

This is django based Website in which I used HTML, CSS, Javascript for the front-end and django for the server side.
In this project mySQLite database is used.
In this project signup and login authentications are used and all the possible validations have been handled.
Some advance concepts like sessions have been implemented while making this project.
The website is responsive in every device and achieved this by using bootstrap in the project. 







## Pages in the Website

### 1) Home Page
This is the landing page of the website in which all the products have been displayed. User can also filter the products by choosing specific category.
Our Home screen will contain navigation bar and below that there is the list of products. The reference screenshot is given below:


![Screenshot (111)](https://user-images.githubusercontent.com/84591165/200869726-81e14f59-3bc4-47fa-aa5a-637265a27a1f.png)


### 2) Signup Page
User can register himself by providing his first name, last name, email, password and mobile number. All types of validations have been added in all the fields for example if user input password which is less than 8, existing email or mobile then in all these cases we show error message on the signup screen. After successful signup process we navigate user to the login page. The refernce screenshot of the signup page is given below:


![Screenshot (112)](https://user-images.githubusercontent.com/84591165/200870440-6a995263-de64-4e0c-a152-bcadd66ec709.png)


### 3) Login Page 
User can login into the website by providing his email address and password. Validation are also added to the fields. If the user is registered in our database with the entered email address and correct associated password, we navigate the user to landing page otherwise we will display the error on the longin page. The reference screenshot the login page is given below.


![Screenshot (113)](https://user-images.githubusercontent.com/84591165/200870844-c8e6bf58-48ff-478b-b5c2-f39525117b4c.png)

### 4) Contact Us Page
When user navigate to this page he can know our address, email and mobile number. Along with this dropping a message functionality is also implemented in this page with for now I have not integrated it with database. The reference screenshot of this page is given below:


![Screenshot (114)](https://user-images.githubusercontent.com/84591165/200872917-d4fb0284-aac2-490c-95c2-b5d1c02f3805.png)

## Features included

1. Authentication
2. Session Management
3. Responsive
4. Filter Products

## Commands
python manage.py runserver




