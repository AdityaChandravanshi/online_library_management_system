from django import forms
from .models import Author, Book, BorrowRecord

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("This field is required.")
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("This field is required.")
        if '@' not in email or '.' not in email:
            raise forms.ValidationError("Enter a valid email address.")
        return email
    
    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if not bio:
            raise forms.ValidationError("This field is required.")
        return bio
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'published_date', 'author']
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("This field is required.")
        return title

    def clean_genre(self):
        genre = self.cleaned_data.get('genre')
        if not genre:
            raise forms.ValidationError("This field is required.")
        return genre

    def clean_published_date(self):
        published_date = self.cleaned_data.get('published_date')
        if not published_date:
            raise forms.ValidationError("This field is required.")
        return published_date

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author:
            raise forms.ValidationError("This field is required.")
        return author

class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['user_name', 'book', 'borrow_date', 'return_date']

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        if not user_name:
            raise forms.ValidationError("This field is required.")
        return user_name
    
    def clean_book(self):
        book = self.cleaned_data.get('book')
        if not book:
            raise forms.ValidationError("This field is required.")
        return book

    def clean_borrow_date(self):
        borrow_date = self.cleaned_data.get('borrow_date')
        if not borrow_date:
            raise forms.ValidationError("This field is required.")
        return borrow_date

    def clean_return_date(self):
        return_date = self.cleaned_data.get('return_date')
        borrow_date = self.cleaned_data.get('borrow_date')
        if return_date and return_date < borrow_date:
            raise forms.ValidationError("Return date cannot be earlier than borrow date.")
        return return_date