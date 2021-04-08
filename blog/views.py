from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# detailview: provides context object called either
# object or the lowercased name of the model (post)
# expects either primary key or slug passed as identifier


from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    # context_object_name = 'all_posts_list'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    # context_object_name = 'indiv_post'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    # reverse_lazy wont execute
    # the URL redirect until view has finished deleting
