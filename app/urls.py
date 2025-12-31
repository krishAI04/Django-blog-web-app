from django.urls import path
from app import views

urlpatterns = [
    path('', views.signin,name='signin'),
    path("signup/", views.signup,name='signup'),
    path('home/', views.home,name='home'),
    path('new_post/', views.new_post,name='new_post'),
    path('my_posts/', views.my_posts,name='my_posts'),
    path('post/<int:post_id>/', views.post_detail,name='blog_detail'),
    path('edit_post/<int:post_id>/', views.edit_post,name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post,name='delete_post'),
    path('signout/', views.signout,name='signout'), 
    path('search/',views.search_home,name = 'search_home'),
    path('my_posts/search/',views.search_my_post,name = 'search_my_post'),
    
] 