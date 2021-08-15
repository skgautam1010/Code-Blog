from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS=((0,'Draft'),
        (1,'Publish')
    )



class Post(models.Model):
    title=models.CharField(max_length=400,unique=True)
    slug=models.SlugField(max_length=300,unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')  #many to one relationship with post model 
    name = models.CharField(max_length=80)
    email = models.EmailField()
    age=models.IntegerField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering=['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body,self.name)

    

    
