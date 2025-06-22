from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import ForumPost
from .serializers import ForumPostSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def forum_posts(request):
    if request.method == 'GET':
        posts = ForumPost.objects.all().order_by('-created_at')
        serializer = ForumPostSerializer(posts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ForumPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)