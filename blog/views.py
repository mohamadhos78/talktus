from django.shortcuts import render

def landing(request):
    return render(request, "landingPage.html")

def posts(request):
    return render(request, "posts.html")

def post(request):
    return render(request, "text-course.html")

def video_post(request):
    return render(request, "video-course.html")
