from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts': posts, })

def detail(request, article_id):
    post_detail = get_object_or_404(Post, pk=article_id)
    images = post_detail.post_images


    return render(request, 'detail.html', {'post': post_detail, 'images':images})

