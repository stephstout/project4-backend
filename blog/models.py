from django.db import models
class Post(models.Model):
    owner = models.ForeignKey('users.User', related_name="owned_posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    body = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name
