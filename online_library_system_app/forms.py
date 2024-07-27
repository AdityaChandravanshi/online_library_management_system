from django import forms
from .models import Author, Book, BorrowRecord
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date
import re

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('Name is required.')
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise ValidationError('Name can only contain letters and spaces.')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('Email is required.')
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValidationError('Enter a valid email address.')
        if Author.objects.filter(email=email).exists():
            raise ValidationError('An author with this email already exists, Please different email id fill this form.')
        return email

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if not bio:
            raise ValidationError('Bio is required.')
        return bio

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'published_date', 'author']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError('Title is required.')
        return title

    def clean_genre(self):
        genre = self.cleaned_data.get('genre')
        if not genre:
            raise ValidationError('Genre is required.')
        return genre
    
    def clean_published_date(self):
        published_date = self.cleaned_data.get('published_date')
        if not published_date:
            raise ValidationError('Published date is required.')
        try:
            # Convert published_date to string and then parse it
            published_date_str = str(published_date)
            if not parse_date(published_date_str):
                raise ValidationError('Enter a valid date in YYYY-MM-DD format.')
        except ValueError:
            raise ValidationError('Enter a valid date in YYYY-MM-DD format.')
        return published_date

class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['user_name', 'book', 'borrow_date', 'return_date']

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        if not user_name:
            raise ValidationError('User name is required.')
        if not re.match(r'^[A-Za-z\s]+$', user_name):
            raise ValidationError('User name can only contain letters and spaces.')
        return user_name

    def clean_borrow_date(self):
        borrow_date = self.cleaned_data.get('borrow_date')
        if not borrow_date:
            raise ValidationError('Borrow date is required.')
        try:
            # Convert borrow_date to string and then parse it
            borrow_date_str = str(borrow_date)
            if not parse_date(borrow_date_str):
                raise ValidationError('Enter a valid date in YYYY-MM-DD format.')
        except ValueError:
            raise ValidationError('Enter a valid date in YYYY-MM-DD format.')
        return borrow_date

    def clean_return_date(self):
        return_date = self.cleaned_data.get('return_date')
        if not return_date:
            raise ValidationError('Return date is required.')
        try:
            # Convert return_date to string and then parse it
            return_date_str = str(return_date)
            if not parse_date(return_date_str):
                raise ValidationError('Enter a valid date in YYYY-MM-DD format.')
        except ValueError:
            raise ValidationError('Enter a valid date in YYYY-MM-DD format.')
        return return_date
