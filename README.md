# Social Media App using Django


## Features
This application supports below mentioned features
- New user registration, once user sign-ups he will redirected to settings page to update user profile.
- Exisiting user login and validation
- Logged-in user can create post by uploading image and caption, on upload user will be redirected to homepage and uploaded post will be visible in feed
- Logged-in user can update profile 
- Logged-in user can access and submit contact us form, on submit user will be redirected to messages page    where submitted contact us message will be visible
- Application also has a dedicated profile page for each user where all post made by that user will be visible
- Application allows user to like posts and like count will increase



## Getting started

To run this application python 3.9 or above is required 
- Clone the code to your local
- Create virtual enviornment using command "python -m venv venv"
- Now, activate virtual enviornment using "venv\Scripts\activate"
- Install the required libraries using "pip install -r requirements.txt"
- Once libraries are installed run command "python manage.py makemigrations"
- Run command to migrate "python manage.py migrate"
- To run Django locally use command "python manage.py runserver"
- Use username "Karthik" and password - "123" to login


## Tools Used
- Python 3.10
- Django 4.1.6
- Pillow 9.4.0
- Sqlite Database
