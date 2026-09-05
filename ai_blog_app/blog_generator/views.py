from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def generate_blog_post(request):
    # placeholder response — replace with your real logic later
    return JsonResponse({"message": "Blog post generation endpoint working"})


    