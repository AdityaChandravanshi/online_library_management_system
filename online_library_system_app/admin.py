# library/admin.py
import openpyxl
from django.http import HttpResponse
from django.contrib import admin
from .models import Author, Book, BorrowRecord

# Define the export action
def export_to_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=library_data.xlsx'

    wb = openpyxl.Workbook()
    ws = wb.active

    row_num = 1
    columns = ['Author Name', 'Author Email', 'Book Title', 'Book Genre', 'Published Date', 'Borrower', 'Borrow Date', 'Return Date']

    for col_num, column_title in enumerate(columns, 1):
        cell = ws.cell(row=row_num, column=col_num)
        cell.value = column_title

    for book in Book.objects.all():
        row_num += 1
        author = book.author
        borrow_records = BorrowRecord.objects.filter(book=book)
        if borrow_records.exists():
            for record in borrow_records:
                ws.append([
                    author.name, author.email, book.title, book.genre, book.published_date,
                    record.user_name, record.borrow_date, record.return_date
                ])
        else:
            ws.append([
                author.name, author.email, book.title, book.genre, book.published_date,
                '', '', ''
            ])

    wb.save(response)
    return response

export_to_excel.short_description = "Export to Excel"

class BookAdmin(admin.ModelAdmin):
    actions = [export_to_excel]

# Unregister the Book model if it's already registered
if admin.site.is_registered(Book):
    admin.site.unregister(Book)

# Register models
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(BorrowRecord)
