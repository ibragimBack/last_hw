from django.urls import path
from book_forum.views import create_book_forum_view, book_list_view, book_detail_view, delete_book_forum_view, edit_book_forum_view

urlpatterns = [
    path('book_list/', book_list_view),
    path('book_list/<int:id>', book_detail_view),
    path('book_list/<int:id>/delete/', delete_book_forum_view),
    path('book_list/<int:id>/update/', edit_book_forum_view),
    path('create_book/', create_book_forum_view),
]