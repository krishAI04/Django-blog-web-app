from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from app.models import BlogPost
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password= password)
        if user :
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('signin')
        
    return render(request, 'login.html')

def signup(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_pss = request.POST.get('confirm_password')

        if password == confirm_pss:
            same = True
            user = User.objects.create_user(username=username, password=password)
            user.save
            messages.success(request, 'Account created Successfully')
            return redirect('home')
        else:
            messages.error(request,"Password doesn't match")
    return render(request, 'signup.html')

@login_required
def home(request):
    blog = BlogPost.objects.all()
    return render(request, 'home.html', {'blogs': blog})

@login_required
def new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user

        post = BlogPost(title=title,content = content, author = author)
        post.save()
        messages.success(request,"Blog Created Successfully!")
        return redirect('new_post')

    return render(request, 'new_post.html')

@login_required
def my_posts(request):
    post = BlogPost.objects.filter(author=request.user)
    return render(request, 'my_post.html', {'post': post})

@login_required
def edit_post(request, post_id):
    blog = BlogPost.objects.get(id=post_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        blog.title = title
        blog.content = content
        blog.save()
        messages.success(request, "Blog Updated Successfully!")
        return redirect('my_posts')

    return render(request, 'edit_post.html', {'blog': blog})

@login_required
def delete_post(request, post_id):
    blog = BlogPost.objects.get(id = post_id)
    blog.delete()
    return redirect('my_posts')

@login_required
def post_detail(request, post_id):
    blog = BlogPost.objects.get(id=post_id)
    return render(request, 'blog_detail.html', {'blog': blog})

@login_required
def signout(request):
    logout(request)
    return redirect('signin') 

@login_required    
def search_home(request):
    query = request.GET.get('q')
    blogs = BlogPost.objects.filter(title__icontains=query)
    return render(request, 'home.html', {'blogs': blogs, 'query': query})
    
@login_required   
def search_my_post(request):
    query = request.GET.get('q')
    blogs = BlogPost.objects.filter(title__icontains=query, author=request.user)
    return render(request, 'my_post.html', {'post': blogs , 'query': query})