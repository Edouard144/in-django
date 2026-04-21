import json
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


def hello(request):
    return HttpResponse('Hello Django!')


def get_post(request, id):
    post = get_object_or_404(Post, id=id)
    return JsonResponse({
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'is_published': post.is_published,
    })


def get_all_posts(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    posts_list = list(posts.values('id', 'title', 'content', 'is_published'))
    return JsonResponse({'posts': posts_list})


@csrf_exempt
def posts(request):
    if request.method == 'GET':
        all_posts = list(Post.objects.values('id', 'title', 'content'))
        return JsonResponse({'posts': all_posts})
    elif request.method == 'POST':
        data = json.loads(request.body)
        post = Post.objects.create(
            title=data['title'],
            content=data['content'],
            is_published=data.get('is_published', False)
        )
        return JsonResponse({'id': post.id, 'title': post.title}, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class PostsView(View):
    def get(self, request):
        all_posts = list(Post.objects.values('id', 'title', 'content'))
        return JsonResponse({'posts': all_posts})

    def post(self, request):
        data = json.loads(request.body)
        post = Post.objects.create(
            title=data['title'],
            content=data['content'],
            is_published=data.get('is_published', False)
        )
        return JsonResponse({'id': post.id}, status=201)


@login_required(login_url='login')
def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blog/create_post.html', {'form': form})

    elif request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('get-all-posts')

        else:
            return render(request, 'blog/create_post.html', {'form': form})


@login_required(login_url='login')
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'blog/create_post.html', {'form': form})

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('get-all-posts')

        else:
            return render(request, 'blog/create_post.html', {'form': form})


@login_required(login_url='login')
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('get-all-posts')

    return render(request, 'blog/confirm_delete.html', {'post': post})
