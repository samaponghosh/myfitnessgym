from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('read/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('upload_blog/', views.uploadPost, name='upload'),
    path('delete_blog/<slug:slug>/', views.deleteBlog),
]
