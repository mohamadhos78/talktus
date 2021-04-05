from django.shortcuts import render
from .models import Contact, Category, Post


def landing(request):
    from .forms import contactform
    form = contactform()
    categories = Category.objects.all()[:4]
    print("\n\n",len(categories),"\n\n")
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
        "categories" : categories ,
    }
    return render(request, "landingPage.html",context)

def posts(request,category):
    from django.core.paginator import Paginator
    from django.db.models import Q
    page = request.GET.get('page')

    categories = Category.objects.all()
    title = category
    posts = Post.objects.filter(category__title=title)
    
    paginator = Paginator(posts, 5)
    posts = paginator.get_page(page)
    context = {
        "posts" : posts ,
        "title" : title,
        "categories" : categories ,
    }
    return render(request, "posts.html",context)

def post(request,title):
    from django.db.models import Q
    from django.shortcuts import get_object_or_404
    post = get_object_or_404(Post, title=title)
    posts = Post.objects.filter(category__title=post.category.title)
    context = {
        "post" : post ,
        "posts" : posts ,
    }
    return render(request, "text-course.html", context)

def search(request):
    from django.core.paginator import Paginator
    from django.db.models import Q
    page = request.GET.get('page')

    categories = Category.objects.all()
    from django.db.models import Q
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(content__contains=query))
    title = query

    paginator = Paginator(posts, 5)
    posts = paginator.get_page(page)
    context = {
       "posts" : posts ,
       "categories" : categories ,
       "title" : title ,
    } 
    return render(request, "posts.html",context)

def last_posts(request):
    from django.core.paginator import Paginator
    from django.db.models import Q
    page = request.GET.get('page')

    categories = Category.objects.all()
    posts = Post.objects.all().order_by("-date")
    
    paginator = Paginator(posts, 5)
    posts = paginator.get_page(page)
    
    title = "آخرین‌ پست‌ها"
    context = {
        "posts" : posts ,
        "title" : title ,
        "categories" : categories ,
    }
    return render(request, "posts.html",context)