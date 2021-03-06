from django.shortcuts import render
from .models import Contact, Category, Post


def landing(request):
    from .forms import contactform
    form = contactform()
    if request.method == "POST":
        save_form = contactform(request.POST)
        if save_form.is_valid():
            save_form.save()
    else:
        member_email = request.GET.get('email')
        if member_email:
            member = Contact(email=member_email)
            member.save()
    context = {
    }
    return render(request, "landingPage.html")

def posts(request,category):
    title = category
    posts = Post.objects.filter(category__title=title)
    print(len(posts))
    context = {
        "posts" : posts ,
        "title" : title,
    }
    return render(request, "posts.html",context)

def post(request,title):
    from django.db.models import Q
    from django.shortcuts import get_object_or_404
    post = get_object_or_404(Post, title=title)
    posts = Post.objects.filter(category__title=post.category.title)
    context = {
        "post" : post,
        "posts": posts,
    }
    return render(request, "text-course.html", context)

def search(request):
    from django.db.models import Q
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(content__contains=query))
    context = {
       "posts" : posts ,
    } 
    return render(request, "posts.html",context)
