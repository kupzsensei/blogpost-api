from django.db import models
from post.models import Post
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    note = models.TextField()
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments' , blank=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} commented in a post {self.post} 2 minutes ago"