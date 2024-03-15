from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post,Author

# Create your views here.

# Function based view(Old way)

# def post_list(request):
#    posts = Post.objects.all()
#    return render(request, 'post_list.html', {'posts': posts})


# Class based view(New way)

#class PostListView(ListView):
 #   model = Post
   # template_name = 'post_list.html'
   # context_object_name = 'posts'
    
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

# Custome class based view
# views.py


class CreatePostView(CreateView):
    model = Post
    fields = ['title', 'content']  # Fields to be displayed in the form for creating a new post
    template_name = 'create_post.html'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)

