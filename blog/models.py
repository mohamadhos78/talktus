from django.db import models
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=64,null=False,blank=False)
    image = models.FileField(upload_to="post_media/",null=True, blank=True)
    Urlimage = models.URLField(null=False, blank=True)
    video = models.FileField(upload_to="post_media/",null=True, blank=True)
    Urlvideo = models.URLField(null=False, blank=True)
    category = models.ForeignKey("Category",on_delete=models.CASCADE,related_name="posts")
    content = HTMLField(null=False, blank=True)
    date = models.DateTimeField(auto_now_add=True,blank=False,null=False)
    description = models.CharField(max_length=512, null=False, blank=True)


    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.category.title

class Category(models.Model):
    image = models.ImageField(upload_to="category_cover" ,null=False)
    Urlimage = models.URLField(null=False, blank=True)
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=512, null=False, blank=False)
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=32,null=True,blank=True)
    email = models.CharField(max_length=32,null=False)
    message = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "ContactUs"
        verbose_name_plural = "ContactUs"
    

    