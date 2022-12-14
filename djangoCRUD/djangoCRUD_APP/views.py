from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CreatePostsForm,EditPost
from .models import Articles
from django.core.exceptions import ObjectDoesNotExist



def index(request):
    CreateForm = CreatePostsForm()
    if request.method == "POST":
        CreateForm = CreatePostsForm(request.POST)
        if CreateForm.is_valid():
            title = CreateForm.cleaned_data["title"]
            url = CreateForm.cleaned_data["url"]
            content = CreateForm.cleaned_data["content"]
            published = CreateForm.cleaned_data["published"]
            category = CreateForm.cleaned_data["category"]
            if published == True:
                published = "Опубликовано"
                Articles.objects.create(title=title, url=url, content=content, published=published, category=category)
                return redirect('http://127.0.0.1:8000/news')
    return render(request,"index.html",{"form":CreateForm})

def news(request):
    news=Articles.objects.all()
    return render(request,"news.html",{"news":news})

def edit(request,id):
    try:
        post = Articles.objects.get(id=id)
        if request.method == "POST":
            post.title = request.POST.get("title")
            post.url = request.POST.get("url")
            post.content = request.POST.get("content")
            post.published = request.POST.get("published")
            if post.published == 'on':
                post.published = "Опубликовано"
            else:
                post.published = "Не опубликовано"
            post.category = request.POST.get("category")
            post.save()
            return redirect('http://127.0.0.1:8000/news')
        else:
            return render(request,'edit.html',{"post":post})
    except Articles.DoesNotExist:
        return HttpResponse("<h2>Не найден</h2>")
def delete(request,id):
    try:
        post = Articles.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect("http://127.0.0.1:8000/news")
    except Articles.DoesNotExist:
        return HttpResponse("<h2>Не найден</h2>")

