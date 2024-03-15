from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'), # This is the URL pattern for the Function based view
    #path('', views.PostListView.as_view(), name='PostListView'), # This is the URL pattern for the Class based view
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'), 
    path('create/', views.CreatePostView.as_view(), name='create_post'),

]