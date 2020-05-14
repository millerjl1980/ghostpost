from django.shortcuts import render
from ghostpost.models import PostMessage
from ghostpost.forms import AddPostForm

# Create your views here.
def index(request):
    posts = PostMessage.objects.all().order_by('-id')
    note = "all Boasts and Roasts!"
    return render(request, 'index.html', {'posts': posts, 'note': note})

def boasts(request):
    posts = PostMessage.objects.filter(boast=True).order_by('-id')
    note = "all Boasts!"
    return render(request, 'index.html', {'posts': posts, 'note': note})
    
def roasts(request):
    posts = PostMessage.objects.filter(boast=False).order_by('-id')
    note = "all Roasts!"
    return render(request, 'index.html', {'posts': posts, 'note': note})

def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'addpost.html', {'form': form})


def up_view(request, post_id):
    post = PostMessage.objects.get(id=post_id)
    post.up_vote += 1
    post.save()
    # todo:  finish view

def down_view(request, post_id):
    post = PostMessage.objects.get(id=post_id)
    post.down_vote += 1
    post.save()
    # todo:  finish view