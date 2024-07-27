from django.db import models
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date
import re

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    bio = models.TextField()

    def clean(self):
        if not re.match(r'^[A-Za-z\s]+$', self.name):
            raise ValidationError('Name can only contain letters and spaces.')
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email):
            raise ValidationError('Enter a valid email address.')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def clean(self):
        if not self.title:
            raise ValidationError('Title is required.')
        if not self.genre:
            raise ValidationError('Genre is required.')
        if not parse_date(str(self.published_date)):
            raise ValidationError('Enter a valid date in YYYY-MM-DD format.')

    def __str__(self):
        return self.title

class BorrowRecord(models.Model):
    user_name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()

    def clean(self):
        if not re.match(r'^[A-Za-z\s]+$', self.user_name):
            raise ValidationError('User name can only contain letters and spaces.')
        if not parse_date(str(self.borrow_date)):
            raise ValidationError('Enter a valid borrow date in YYYY-MM-DD format.')
        if not parse_date(str(self.return_date)):
            raise ValidationError('Enter a valid return date in YYYY-MM-DD format.')

    def __str__(self):
        return self.user_name