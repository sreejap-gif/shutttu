from django.db import models

class lovemessage(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class HomePage(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=255)
    main_message = models.TextField()
    background_image = models.ImageField(upload_to='home_bg/', blank=True, null=True)

    def _str_(self):
        return "Home Page Content 💕"

class OurStory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    story_date = models.DateField()
    image = models.ImageField(upload_to='story_images/', blank=True, null=True)

    class Meta:
        ordering = ['story_date']

    def _str_(self):
        return self.title
    
class Gallery(models.Model):
    caption = models.CharField(max_length=150)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.caption

class Reason(models.Model):
    reason_text = models.CharField(max_length=255)
    emoji = models.CharField(max_length=10, blank=True)

    def _str_(self):
        return self.reason_text

class Surprise(models.Model):
    password = models.CharField(max_length=50)
    surprise_title = models.CharField(max_length=150)
    surprise_message = models.TextField()
    background_music = models.FileField(upload_to='music/', blank=True, null=True)

    def _str_(self):
        return "Secret Surprise 💝"

