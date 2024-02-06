from django.urls import path
from .views import HomeView,articalDetailView,createPostView,editPostView,deletePostView

urlpatterns = [
    path('',HomeView.as_view(), name="home"),
    path('article/<int:pk>', articalDetailView.as_view(), name = 'article details'),
    path('createPost/',createPostView.as_view(), name='create_post'),
    path('article/edit/<int:pk>', editPostView.as_view(), name = 'update post' ),
    path('article/delete/<int:pk>', deletePostView.as_view(), name = 'delete post' ),
]