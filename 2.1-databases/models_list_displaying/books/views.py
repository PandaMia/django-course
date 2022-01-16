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
    context = {'books': books}
    return render(request, template, context)
