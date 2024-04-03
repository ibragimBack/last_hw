from django.urls import path
from book_forum.views import CreateBookView, BookDetailView, DeleteBookView, UpdateBookView, \
    SearchBookView, CommentCreateView, EveryDayListView, MysticListView, RomanticListView, \
    DetectiveListView


urlpatterns = [
    path('book_list/<int:id>', BookDetailView.as_view()),
    path('book_list/<int:id>/delete/', DeleteBookView.as_view()),
    path('book_list/<int:id>/update/', UpdateBookView.as_view()),
    path('create_book/', CreateBookView.as_view()),
    path('search/', SearchBookView.as_view(), name='search'),
    path('create_comment/', CommentCreateView.as_view()),
    path('everyday_genre/', EveryDayListView.as_view()),
    path('mystic_genre/', MysticListView.as_view()),
    path('romantic_genre/', RomanticListView.as_view()),
    path('detective_genre/', DetectiveListView.as_view()),
]
