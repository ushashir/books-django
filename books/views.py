from django.http import HttpResponse
from django.views.generic import ListView
from .models import Book


def hello(request):
    return HttpResponse("Hello Books")


class BookListView(ListView): 
  model = Book
  template_name = 'book_list.html'