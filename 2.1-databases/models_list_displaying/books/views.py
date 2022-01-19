from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def books_date_view(request, dt):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=dt)
    dates = sorted(set(Book.objects.all().values_list('pub_date')))

    current_idx_date = dates.index((dt.date(),))
    next_idx_date = current_idx_date + 1
    previous_idx_date = current_idx_date - 1

    if next_idx_date < len(dates):
        next_date = dates[next_idx_date][0].strftime('%Y-%m-%d')
    else:
        next_date = None
    if previous_idx_date >= 0:
        previous_date = dates[previous_idx_date][0].strftime('%Y-%m-%d')
    else:
        previous_date = None

    context = {'date': dt,
               'books': books,
               'next_date': next_date,
               'previous_date': previous_date}
    return render(request, template, context)
