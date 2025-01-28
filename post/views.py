from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response

# Create your views here.
class PostView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request):
        data = Post.objects.all().order_by('-id')   
        serializer = PostSerializer(data , many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = PostSerializer(data={**data, "user": request.user.id })
        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True})
        return Response({"ok": False , "errors": serializer.errors})

    def patch(self,request):
        ...

    def delete(self,request):
        ...

class LikeView(APIView):
    def post(self, request):
        if request.user:
            try:
                post_instance = Post.objects.get(id=request.data['id'])
                post_instance.like.add(request.user)
            except Post.DoesNotExist:
                return Response({'detail': "invalid LIKE"})