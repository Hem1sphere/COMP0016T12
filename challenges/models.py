from django.db import models
from django.utils import timezone
from users.models import Developer, Clinician
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Challenge(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    award = models.DecimalField(verbose_name= ('Award in GBP'), max_digits=10, decimal_places=2, default=0)
    clinician = models.ForeignKey(Clinician, on_delete=models.CASCADE, related_name="creator")  # clinician who created the challenge
    developers = models.ManyToManyField(Developer, blank=True)  # developerS who indicated interest
    description = RichTextUploadingField()
    evaluation = RichTextUploadingField()
    timeline = RichTextUploadingField()
    rule = RichTextUploadingField()
    data = models.FileField(blank=True)

    def get_developers(self):
        return ",".join([str(d) for d in self.developers.all()])

    def __str__(self):
        return f'Challenge: {self.title}'

    def get_absolute_url(self):
        return reverse('challenges_detail', kwargs={'pk': self.pk})
