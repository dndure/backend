from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required    
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from pytube import YouTube


# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def generate_blog_post(request):
    # placeholder response — replace with your real logic later
    return JsonResponse({"message": "Blog post generation endpoint working"})

def generate_blog(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            yt_link = data['yt_link']
            title = data.get('title')
            content = data.get('content')
        except (json.JSONDecodeError, KeyError) as e:
            return JsonResponse({"error": "Invalid request data"}, status=400)  


        # Get yt title
        title = get_youtube_title(yt_link)
        

        # Get transcript from yt_link

        # Use OpenAI API to generate blog post based on title and content

        # Save blog post to database

        # Return blog post as a response

        # Here you would typically call your AI model to generate a blog post
        # For now, we'll just return a placeholder response
        generated_blog_post = f"Generated blog post based on title: {title} and content: {content}"

        return JsonResponse({"generated_blog_post": generated_blog_post})
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)  

def get_youtube_title(yt_link):
    try:
        yt = YouTube(yt_link)
        return yt.title
    except Exception as e:
        print(f"Error fetching YouTube title: {e}")
        return None  

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')    

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                return redirect('/')
            except Exception as e:
                print(f"SIGNUP ERROR: {e}")  # <-- temporary debug line
                return render(request, 'signup.html', {'error': 'An error occurred during signup. Please try again.'})
        else:
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})
    return render(request, 'signup.html')

def user_logout(request):
    # placeholder response — replace with your real logic later
    logout(request)
    return redirect('/')    