from django.db import models


# Create your models here.
class ContentBase(models.Model):
    content = models.TextField(max_length=500)
    votes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(ContentBase):
    colored = models.BooleanField(default=False)
    text_color = models.CharField(max_length=10, blank=True, null=True, default='#000000')
    background_color = models.CharField(max_length=10, blank=True, null=True, default='#ffffff')


class Comment(ContentBase):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
