from django.contrib import admin
from django.urls import path
from mygym import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home),
    path('login_social/',views.loginn),
    path('signup_social/',views.signup),
    path('logout_social/',views.logoutt),
    path('upload/',views.upload),
    path('like-post/<str:id>/', views.likes, name='like-post'),
    path('#<str:id>/', views.home_post),
    path('explore/',views.explore),
    path('profile/<str:id_user>/', views.profile),
    path('delete/<str:id>/', views.delete),
    path('search-results/', views.search_results, name='search_results'),
    path('follow/', views.follow, name='follow'),
]
