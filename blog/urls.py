from django.urls import path

from blog.views import PostListView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<slug>', PostDetailView.as_view(), name='post-detail'),
]