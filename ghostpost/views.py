from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from ghostpost.models import PostMessage
from ghostpost.forms import AddPostForm
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    posts = PostMessage.objects.all().order_by('-sub_time')
    note = "all Boasts and Roasts!"
    return render(request, 'index.html', {'posts': posts, 'note': note})

def detail(request, post_id):
    post = get_object_or_404(PostMessage, pk=post_id)
    return render(request, 'detail.html', {'post': post})

def boasts(request):
    posts = PostMessage.objects.filter(boast=True).order_by('-sub_time')
    note = "all Boasts!"
    return render(request, 'index.html', {'posts': posts, 'note': note})
    
def roasts(request):
    posts = PostMessage.objects.filter(boast=False).order_by('-sub_time')
    note = "all Roasts!"
    return render(request, 'index.html', {'posts': posts, 'note': note})

def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            new_post.refresh_from_db()
            hidden_key = get_random_string(length=6)
            new_post.hidden_key = hidden_key
            new_post.save()
            return HttpResponseRedirect(reverse('manage_post', kwargs={'post_hk': hidden_key}))
    else:
        form = AddPostForm()
    return render(request, 'addpost.html', {'form': form})

def manage_post(request, post_hk):
     post = get_object_or_404(PostMessage, hidden_key=post_hk)
     return render(request, 'manage_post.html', {'post': post})

def delete_post(request, post_hk):
    post = PostMessage.objects.get(hidden_key=post_hk)
    post.delete()
    return HttpResponseRedirect(reverse('home'))


def up_view(request, post_id):
    post = PostMessage.objects.get(id=post_id)
    post.up_vote += 1
    post.save()
    return HttpResponseRedirect(reverse('detail', kwargs={'post_id': post_id}))

def down_view(request, post_id):
    post = PostMessage.objects.get(id=post_id)
    post.down_vote += 1
    post.save()
    return HttpResponseRedirect(reverse('detail', kwargs={'post_id': post_id}))

def ranked_view(request):
    posts = PostMessage.objects.all()
    for post in posts:
        score = post.vote_score
        post.score = score
        post.save()
    posts = posts.order_by('-score')
    note = "best Boasts and Roasts!"
    return render(request, 'index.html', {'posts': posts, 'note': note})
    
