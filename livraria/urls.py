from django.urls import path
from django.http import HttpResponse
from livraria.views import home, logout_user, register_user, book_detail, book_delete

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/',register_user, name='register'),
    path('book/<int:id>/', book_detail, name='book'),
    path('delete_book/<int:id>/', book_delete, name='delete_book')
]