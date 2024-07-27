My project name is Online_Library_System.

Usage:

Add Author : 
-> Click on "Add Author" in the navigation menu.
-> Fill in the author's name, email, and bio.
-> Click "Add Author" to save the author.
-> All field's are required in this form.

Add Book : 
-> Click on "Add Book" in the navigation menu.
-> Fill in the book's title, genre, published date, and select an author.
-> Click "Add Book" to save the book.
-> All field's are required in this form.

Add Borrow Record : 
-> Click on "Add Borrow Record" in the navigation menu.
-> Select a book, fill in the borrower's name, borrow date, and return date.
-> Click "Add Borrow Record" to save the record.
-> All field's are required in this form.

View Lists:

-> Authors List: Click on "Authors List" to view all authors.

-> Books List: Click on "Books List" to view all books.

-> Borrow Records List: Click on "Borrow Records List" to view all borrow records.

Export to Excel:
-> Click on "Export Excel Sheet" to download the borrow records as an Excel file.

Back-end Validations:
-> I have use proper Backend validations and error handling error message is showing up in this project.

Contributing
-> If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

->I have used Python in the back-end of my project and I have used Django framework and I have used Django's default database Sqlite3 and in the front-end I have used HTML, Boostrap in my project. I have used this technology in my project.

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
