from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # return reverse('detail',args=(str(self.id))) #if you need to navigate detail page
        return reverse('home') #no need to specify id since we are navigating to home page


class Post(models.Model):
    title=models.CharField(max_length=200)
    title_tag=models.CharField(max_length=255) #need to add default="my first blog" if we add new attribute later adding a attribute 
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255,default='coding')

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('detail',args=(str(self.id))) #if you need to navigate detail page
        return reverse('home') #no need to specify id since we are navigating to home page
    
   
    
