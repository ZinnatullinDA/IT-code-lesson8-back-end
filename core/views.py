from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Book, Author
#from core import models
def index(request):
    count = Book.objects.count()
    return render(request, 'index.html', {"count": count})
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

class BooksByAuthor(ListView):
    model = Book
    template_name = 'books_by_author.html'
    context_object_name = 'books'

    def get_queryset(self):
        self.author = get_object_or_404(Author, name=self.kwargs['name'])
        return Book.objects.filter(author=self.author)
