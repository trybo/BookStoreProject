from django.urls import path
from .views import book_list

app_name = 'core'

urlpatterns = [
    path('', book_list, name='book-list')
]
