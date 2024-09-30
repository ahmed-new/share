from django.db import models
from django .contrib.auth.models import User
from django.urls import reverse
from datetime import datetime , date
from ckeditor.fields import RichTextField

class Category ( models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name 
    
    def get_absolute_url (self):
        return reverse('home')


class Post(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.CharField(max_length=100 , default='coding')
    body= RichTextField(blank=True , null= True)
    header_img= models.ImageField(null=True , blank=True , upload_to='image/')
    date=models.DateField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='posts_likes')

    def __str__(self):
        return self.title +' | '+ str(self.author)
    
    def get_absolute_url (self):
        return reverse('home')
    
    def total_likes(self):
        return self.likes.count()
    
class Profile(models.Model):
    user=models.OneToOneField(User,null=True , on_delete=models.CASCADE)
    bio= models.TextField()
    profile_pic=models.ImageField(null=True , blank=True , upload_to='image/profile')
    website=models.CharField(max_length=200,null=True , blank=True )
    facebook=models.CharField(max_length=200,null=True , blank=True)
    twitter=models.CharField(max_length=200,null=True , blank=True)
    instagram=models.CharField(max_length=200,null=True , blank=True)

    def get_absolute_url (self):
        return reverse('home')

    def __str__(self):
        return str(self.user) 
    
class Comment (models.Model):
    post= models.ForeignKey(Post ,related_name='comments', on_delete= models.CASCADE)
    name=models.CharField(max_length=100)
    body= models.TextField()
    date_added= models.DateField(auto_now_add=True)


def __str__(self):
    return '%s - %s' % (self.Post.title, self.name)
