from django.shortcuts import render
from django.views.generic import ListView, DetailView

# detailview: provides context object called either
# object or the lowercased name of the model (post)
# expects either primary key or slug passed as identifier


from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
