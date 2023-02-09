from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to='media/testimonial')
    
    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='media/gallery')
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Gallery'
    
class Contact(models.Model):
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    day = models.CharField(max_length=40, null=True, blank=True)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.day}: {self.opening_time} - {self.closing_time}"
    
    
class About_us(models.Model):
    title = models.TextField(max_length=200, null=True, blank=True)
    sub_title = models.TextField(max_length=300, null=True, blank=True)
    point1 = models.TextField(max_length=100, null=True, blank=True)
    point2 = models.TextField(max_length=100, null=True, blank=True)
    point3 = models.TextField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    picture = models.ImageField(upload_to='media/about_us')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'About Us'
        
class Event(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    picture = models.ImageField(upload_to='media/events', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Chef(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    designation  = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='media/chefs', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Social_link(models.Model):
    facebook_link = models.URLField(max_length=200, null=True, blank=True)
    twitter_link = models.URLField(max_length=200, null=True, blank=True)
    youtube_link = models.URLField(max_length=200, null=True, blank=True)
    instagram_link = models.URLField(max_length=200, null=True, blank=True)
    google_link = models.URLField(max_length=200, null=True, blank=True)

    