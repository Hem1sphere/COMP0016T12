from django.db import models
from users.models import Developer
from challenges.models import Challenge


# Create your models here.
class Solution(models.Model):
    developer = models.OneToOneField(Developer, on_delete=models.CASCADE)  # person who solved the person
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)  # challenge the solution is targeting
    description = models.TextField(default="")
    solution_data = models.FileField()
