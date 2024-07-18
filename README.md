My project name is Online_Library_System.
Step 1: Set Up Django Project
1. Install Django: pip install django
2. Create a Django project:django-admin startproject online_library
cd online_library
3. Create an app: python manage.py startapp library
I have used Python in the back-end of my project and I have used Django framework and I have used Django's default database Sqlite3 and in the front-end I have used HTML, Boostrap in my project. I have used this technology in my project.
First of all we have to install Python and Django in our laptop or system.
To install python, we have to click on https://python.org/ on our browser and then download it from there.
After that we have to install Django by typing comment prompt or write the command pip install Django.
Then we have to create the project by typing django-admin startProject Online_Library_System from the comment prompt.
Then after the project is installed, we will go to the comment prompt and type cd online_library_system and go inside this project.
->cd online_library_system
Then we have to create an app. The commands for the app are python manage.py startapp online_library_system.
Then we have to add the app in the settings.py file. which is the name of our app.
Example:- Like- Settings.py file
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'online_library_system_app', <------App name
]
