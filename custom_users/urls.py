from django.urls import path
from . import views
from book_forum.views import BookListView

app_name = 'person'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', views.AuthorizationView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('book_list/', BookListView.as_view(), name='book_list'),
]
