from django.contrib import admin
from .models import Post,Author

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio']
    
admin.site.register(Post, PostAdmin) # This is the model Post being registered with the admin site   
admin.site.register(Author, AuthorAdmin) # This is the model Author being registered with the admin site
