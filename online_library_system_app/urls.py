from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-book/', views.add_book, name='add_book'),
    path('add-borrow-record/', views.add_borrow_record, name='add_borrow_record'),
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='book_list'),
    path('borrow-records/', views.borrow_list, name='borrow_list'),
    path('export-excel-author/', views.export_to_excel_author, name='export_to_excel_author'),
    path('export-excel-book/', views.export_to_excel_book, name='export_to_excel_book'),
    path('export-excel-borrow-record/', views.export_to_excel_borrow_record, name='export_to_excel_borrow_record'),
    path('export-excel-author-book-borrow-record/', views.export_to_excel_author_book_borrow_record, name='export_to_excel_author_book_borrow_record'),
]