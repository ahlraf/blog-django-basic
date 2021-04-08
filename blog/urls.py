from django.urls import path

from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('',BlogListView.as_view(),name='home'),
]

# primary key for post entry represented as integer <int:pk>
# django automatically adds auto-incrementing primary key to db models
# under the hood added id as pk
