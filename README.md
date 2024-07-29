My project name is Online_Library_System.

Table of Contents: 
Overview, 
Features, 
Requirements, 
Screenshot, 
Usage, 
Add Author, 
Add Book, 
Add Borrow Record, 
View Lists, 
Export to Excel, 
Contributing, 
FAQs, 
Overview: 
The Online Library System is a web-based application built with Django to manage a library's operations. Users can manage authors, books, and borrowing records easily through a user-friendly interface.

Features: 
Add Author: Create new author profiles.
Add Book: Add new books to the library and assign them to authors.
Add Borrow Record: Record borrow details of books by borrowers.
View Lists: View lists of authors, books, and borrow records.
Export Excel: Export the list of borrow records to an Excel sheet.

Requirements:
Python 3.12.0 or higher, 
Django 4.2.7 or higher, 
SQLite (default database), 
openpyxl 3.1.5

Screenshot:
Add Author: 
![AddAuthor](https://github.com/user-attachments/assets/d6cb9260-85af-44b2-b762-3b2c525df8b8)

Author's List's: 
![AuthorsList](https://github.com/user-attachments/assets/bc50a9bc-49cc-4c9e-a253-ff045fc00b86)

Add Book: 
![AddBook](https://github.com/user-attachments/assets/f52d904b-5111-4515-8013-ab037a8aeb62)

![AddBook1](https://github.com/user-attachments/assets/27efc7bd-433d-46e8-b612-a9ba3529da15)

Book's List's: 
![BookLists](https://github.com/user-attachments/assets/355fdaa0-7347-4e50-bfac-84a9a1cdb1a1)

Add Borrow Record: 
![AddBorrowRecord](https://github.com/user-attachments/assets/4aa8beb2-3cb3-48d5-895a-59e62300253b)

![AddBorrowRecord1](https://github.com/user-attachments/assets/abf1d186-fc5d-4e2b-8ad8-2228004b70f5)

Borrow Record List's: 
![BorrowRecordLists](https://github.com/user-attachments/assets/ab2c454e-72e1-4e50-b8cb-82018adcb585)

Export to Excel: 
Export to Excel Sheet's Author List's: 
![ExportToExcelSheetsAuthorLists](https://github.com/user-attachments/assets/82135de2-253c-470c-8bfc-c632c4738148)

Export to Excel Sheet's Book List's: 
![ExportToExcelSheetsBookLists](https://github.com/user-attachments/assets/f36ed035-93e5-400e-a194-cdab9cb0891f)

Export to Excel Sheet's Borrow Record List's: 
![ExportToExcelSheetsBorrowRecordLists](https://github.com/user-attachments/assets/5fa4ac1f-0291-458f-a23f-7d664ec43483)

Export to Excel Sheet's Author, Book, Borrow Record List's: 
![ExportToExcelSheetAuthor,Book,BorrowRecord](https://github.com/user-attachments/assets/ea24f555-f1b6-4d2e-a943-5e2ed45b3008)
![ExportToExcelSheetAuthor,Book,BorrowRecord1](https://github.com/user-attachments/assets/42591f42-02b5-4776-ae49-1f01336d5954)

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

Django Pagination Concept:
-> I have use django pagination concept in our project, All view lists, Like Author Lists, Book Lists, Borrow Record Lists.

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
