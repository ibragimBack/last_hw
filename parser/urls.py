from django.urls import path
from . import views

urlpatterns = [
    path('parser/', views.GetParsing.as_view()),
    path('house_list/', views.HouseListView.as_view()),
    path('news_list/', views.NewListView.as_view()),
]