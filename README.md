I have ensured that the code here is original and not copied from any external source and the code here is my own code.

My project name is Online_Library_System.

I have used Python in the back-end of my project and I have used Django framework and I have used Django's default database Sqlite3 and in the front-end I have used HTML, Boostrap in my project. I have used this technology in my project.

I have use proper Backend validations and error handling error message is showing up in this project.

First of all we have to install Python and Django in our laptop or system.

To install python, we have to click on link https://python.org/ on our browser and then download it from there.

After that we have to install Django by typing command prompt or write the command pip install Django.

Step 1: Set Up Django Project

1. Install Django: pip install django
    
2. Create a Django project:django-admin startproject online_library_system
cd online_library

3. Create an app: python manage.py startapp online_library_system_app
 
4. Add the app to INSTALLED_APPS in settings.py:
5. INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'online_library_system_app', <------App name
]

Step 2: Define Models
Edit models.py in the online_library_system_app to define the required models.

Step 3: Create and Apply Migrations
python manage.py makemigrations library
python manage.py migrate

Step 4: Register Models in Admin
Edit admin.py in the online_library_system_app to register the models.

Step 5: Create Views and Templates for Admin Interface
For simplicity, we will use Django's built-in admin interface to manage the models. For the custom export functionality, we will create a custom admin action.

1. Create Custom Admin Action to export data to an Excel sheet. First, install openpyxl to handle Excel files:

2. pip install openpyxl

3. Define the export action in admin.py:

Step 6: Run the Server

Start the Django development server to test the application:

python manage.py runserver

Then we have to create the project by typing django-admin startProject Online_Library_System from the command prompt.

Then after the project is installed, we will go to the comment prompt and type cd online_library_system and go inside this project.

->cd online_library_system

Then we have to create an app. The commands for the app are python manage.py startapp online_library_system.

Then we have to add the app in the settings.py file. which is the name of our app.

I have created a templates folder inside the app and created some files in it.

like file name is index.html, add_author.html, add_book.html, add_borrow_record.html, author_list.html, book_list.html, borrow_list.html files are there.

I have used Django Form Validation in my application, so that user cannot submit empty form, every single field has to be filled then form will be submitted. If the user has left any field blank, he will get a message or a notification will be generated where the pure field is filled. It is important that my application has a good user interface.

I have used CSRF token in my forms, so that my application remains secure and user information also remains secure, my forms are in other HTML files in templates folder.

I have used CSS to design my application, I have used both External CSS and Internal CSS in my application so that my application user interface remains good.
I have used CSS to design my application, I have used both External CSS and Internal CSS in my application so that my application user interface remains good.
