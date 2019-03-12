from django.db import models
from django.utils import timezone
from users.models import Developer, Clinician
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Discussion(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField(default="")
    author = models.ForeignKey(Developer, on_delete=models.CASCADE)
    
    def get_dicussion_absolute_url(self):
        return reverse('discussion_detail', kwargs={'pk': self.pk}) 
  
    
    def __str__(self):
        return f'Discussion: {self.title}'


class Each_discussion(models.Model):
    date_commented = models.DateTimeField(default=timezone.now)
    comment = models.TextField(default="")
    commenter = models.ForeignKey(Developer, on_delete=models.CASCADE)
    

