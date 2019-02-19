from django.db import models
from users.models import Developer
from challenges.models import Challenge
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Solution(models.Model):
    title = models.CharField(max_length=100, default="")
    date_created = models.DateTimeField(default=timezone.now)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="creator")  # person who solved the person
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)  # challenge the solution is targeting
    description = models.TextField(default="")
    accuracy = models.FloatField(default=0.0)
    solution_data = models.FileField()

    def __str__(self):
        return f'Solution: {self.title}'

    def get_absolute_url(self):
        return reverse('solutions_detail', kwargs={'pk': self.pk})
