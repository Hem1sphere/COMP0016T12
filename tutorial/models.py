from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from users.models import User


# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    prerequisites = RichTextUploadingField()
    description = RichTextUploadingField()
    data = models.FileField(blank=True)

