from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('college/', views.find_college, name="find_college"),
    path('college/choose/', views.choose_college, name="choose_college"),
    path('search/lecture/', views.search_lecture, name="search_lecture"),
    path('search/home/', views.search_home, name="search_home"),
    path('lecture/detail/<str:lecture_id>/', views.lecture_detail, name="lecture_detail")
]
