from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Post
from .serializers import PostSerializer
import logging

# Create logger for API views
logger = logging.getLogger('blog')


@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            logger.info(f"User {username} logged in successfully")
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email
            })

        logger.warning(f"Failed login attempt for username: {username}")
        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    except Exception as e:
        logger.error(f"Unexpected error in api_login: {str(e)}")
        return Response(
            {'error': 'Something went wrong'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
@permission_classes([AllowAny])
def api_get_all_posts(request):
    try:
        posts = Post.objects.filter(is_published=True).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.error(f"Unexpected error in api_get_all_posts: {str(e)}")
        return Response(
            {'error': 'Something went wrong'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
@permission_classes([AllowAny])
def api_get_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(
            {'error': 'Post not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        logger.error(f"Unexpected error fetching post {id}: {str(e)}")
        return Response(
            {'error': 'Something went wrong'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    serializer = PostSerializer(post)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_post(request):
    try:
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            logger.info(f"Post created by {request.user.username}: {serializer.data.get('title')}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Unexpected error in api_create_post: {str(e)}")
        return Response(
            {'error': 'Something went wrong'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def api_update_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f"Unexpected error fetching post {id} for update: {str(e)}")
        return Response(
            {'error': 'Something went wrong'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if post.author != request.user:
        return Response(
            {'error': 'You are not allowed to edit this post'},
            status=status.HTTP_403_FORBIDDEN
        )

    try:
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Post {id} updated by {request.user.username}")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Unexpected error updating post {id}: {str(e)}")
        return Response(
            {'error': 'Something went wrong'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f"Unexpected error fetching post {id} for delete: {str(e)}")
        return Response(
            {'error': 'Something went wrong'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if post.author != request.user:
        return Response(
            {'error': 'You are not allowed to delete this post'},
            status=status.HTTP_403_FORBIDDEN
        )

    try:
        post.delete()
        logger.info(f"Post {id} deleted by {request.user.username}")
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        logger.error(f"Unexpected error deleting post {id}: {str(e)}")
        return Response(
            {'error': 'Something went wrong'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
