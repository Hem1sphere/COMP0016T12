from django.db import models
from users.models import Developer, Clinician


# Create your models here.
class Challenge(models.Model):
    clinician = models.ForeignKey(Clinician, on_delete=models.CASCADE, related_name="creator")  # clinician who created the challenge
    developers = models.ManyToManyField(Developer, blank=True)  # developerS who indicated interest
    description = models.TextField(default="")
    data = models.FileField(blank=True)

    def get_developers(self):
        return ",".join([str(d) for d in self.developers.all()])

    def __str__(self):
        return f'Challenge: {self.description}'

