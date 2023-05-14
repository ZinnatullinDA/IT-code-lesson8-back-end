from django.urls import path, include
from . import views
from .views import BooksByAuthor


app_name = 'core'

urlpatterns = [
    path('', views.index),
    path('book_list/', views.book_list, name='book_list'),
    path('authors/', views.authors_list, name='authors_list'),
    path('books_by_author/<str:name>/', BooksByAuthor.as_view(), name='books_by_author'),

]