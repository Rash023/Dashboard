from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum

from .models import Post
from django.shortcuts import render


# View for rendering the home page
def HomePage(request):
    return render(request, 'index.html')

# View for scheduling a new post
def Schedule_Post(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        # Set default values
        author = "John Doe"
        likes = 0
        shares = 0
        comments = 0

        # Get the count of existing posts
        post_count = Post.objects.count()

        # Increment post_id based on the count of existing posts
        post_id = post_count + 1

        # Save the post to the database
        post = Post.objects.create(
            post_id=post_id,
            author=author,
            title=title,
            description=description,
            likes=likes,
            shares=shares,
            comments=comments
        )
        return redirect('Home')  # Redirect to a success page
    return render(request, 'Post.html',{})

# View for displaying analytics
def Analytics(request):
    return render(request, 'Analytics.html')

# View for displaying comments
def Comments(request):
    return render(request, 'Comments.html')

# View for displaying reach
def Reach(request):
    return render(request, 'Reach.html')

# View for user login
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.success(request, ("There was an error logging in try again!"))
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})

# View for user registration
def register_user(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('Home')
    else:
        form = UserCreationForm()

    return render(request, 'authentication/register.html', {'form': form})
