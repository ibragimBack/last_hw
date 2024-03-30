from django.urls import path
from book_forum.views import CreateBookView, BookListView, BookDetailView, DeleteBookView, UpdateBookView, \
    SearchBookView, CommentCreateView


urlpatterns = [
    path('book_list/<int:id>', BookDetailView.as_view()),
    path('book_list/<int:id>/delete/', DeleteBookView.as_view()),
    path('book_list/<int:id>/update/', UpdateBookView.as_view()),
    path('create_book/', CreateBookView.as_view()),
    path('search/', SearchBookView.as_view(), name='search'),
    path('create_comment/', CommentCreateView.as_view()),
]
