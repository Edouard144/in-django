from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Post
import json


def hello(request):
    return HttpResponse('Hello Django!')


def get_post(request, id):
    post = Post.objects.get(id=id)
    return JsonResponse({
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'is_published': post.is_published,
    })


def get_all_posts(request):
    posts = Post.objects.all()
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
            content=data['content']
        )
        return JsonResponse({'id': post.id}, status=201)