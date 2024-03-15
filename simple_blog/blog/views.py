from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Author

# Create your views here.

# Function based view(Old way)

# def post_list(request):
#    posts = Post.objects.all()
#    return render(request, 'post_list.html', {'posts': posts})


# Class based view(New way)