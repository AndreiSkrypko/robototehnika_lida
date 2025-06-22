from rest_framework import serializers
from .models import ForumPost

class ForumPostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = ForumPost
        fields = ['id', 'title', 'content', 'created_at', 'author', 'author_username']
        read_only_fields = ['author', 'created_at']