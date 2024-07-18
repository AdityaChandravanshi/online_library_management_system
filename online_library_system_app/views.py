from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.dateparse import parse_date
from .models import Author, Book, BorrowRecord
import openpyxl
from django.http import HttpResponse
from .forms import AuthorForm, BookForm, BorrowRecordForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def add_author(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        bio = request.POST['bio']
        author = Author.objects.create(name=name, email=email, bio=bio)
        return redirect('author_list')  
    return render(request, 'add_author.html')

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')  
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        genre = request.POST['genre']
        published_date = parse_date(request.POST['published_date'])
        author_id = request.POST['author']
        author = Author.objects.get(pk=author_id)
        book = Book.objects.create(title=title, genre=genre, published_date=published_date, author=author)
        return redirect('book_list')  
    authors = Author.objects.all()
    return render(request, 'add_book.html', {'authors': authors})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') 
    else:
        form = BookForm()
    authors = Author.objects.all()
    return render(request, 'add_book.html', {'form': form, 'authors': authors})

def add_borrow_record(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        book_id = request.POST['book']
        borrow_date = parse_date(request.POST['borrow_date'])
        return_date = parse_date(request.POST['return_date'])
        book = Book.objects.get(pk=book_id)
        borrow_record = BorrowRecord.objects.create(user_name=user_name, book=book, borrow_date=borrow_date, return_date=return_date)
        return redirect('borrow_list')  
    books = Book.objects.all()
    return render(request, 'add_borrow_record.html', {'books': books})

def add_borrow_record(request):
    if request.method == 'POST':
        form = BorrowRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrow_list')
    else:
        form = BorrowRecordForm()
    books = Book.objects.all()
    return render(request, 'add_borrow_record.html', {'form': form, 'books': books})

def author_list(request):
    authors = Author.objects.all().order_by('id')  
    paginator = Paginator(authors, 5) 
    page = request.GET.get('page')
    
    try:
        authors = paginator.page(page)
    except PageNotAnInteger:
        authors = paginator.page(1)
    except EmptyPage:
        authors = paginator.page(paginator.num_pages)
    
    context = {
        'authors': authors
    }
    
    return render(request, 'author_list.html', context)

def book_list(request):
    books = Book.objects.all().order_by('id')  
    paginator = Paginator(books, 5) 
    page = request.GET.get('page')
    
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    
    context = {
        'books': books
    }
    
    return render(request, 'book_list.html', context)

def borrow_list(request):
    records = BorrowRecord.objects.all().order_by('id')  
    paginator = Paginator(records, 5) 
    page = request.GET.get('page')
    
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)
    
    context = {
        'records': records
    }
    
    return render(request, 'borrow_list.html', context)

def export_to_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=library_data.xlsx'

    wb = openpyxl.Workbook()
    author_ws = wb.active
    author_ws.title = 'Authors'

    books_ws = wb.active
    books_ws.title = 'Books'

    borrow_ws = wb.active
    borrow_ws.title = 'Borrow Records'

    # Export Authors
    authors = Author.objects.all()
    author_ws.append(['ID', 'Name', 'Email', 'Bio'])
    for author in authors:
        author_ws.append([author.id, author.name, author.email, author.bio])

    # Export Books
    books = Book.objects.all()
    books_ws.append(['ID', 'Title', 'Genre', 'Published Date', 'Author'])
    for book in books:
        books_ws.append([book.id, book.title, book.genre, book.published_date, book.author.name])

    # Export Borrow Records
    borrow_records = BorrowRecord.objects.all()
    borrow_ws.append(['ID', 'User Name', 'Book', 'Borrow Date', 'Return Date'])
    for record in borrow_records:
        borrow_ws.append([record.id, record.user_name, record.book.title, record.borrow_date, record.return_date])

    wb.save(response)
    return response
