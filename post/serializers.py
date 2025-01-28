from rest_framework import serializers
from .models import Post
from comment.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True , read_only=True)
    class Meta: 
        model = Post
        # fields = '__all__'
        fields = ['id' , 'note' ,'like', 'created_at', 'updated_at', 'user','comments' ]
        