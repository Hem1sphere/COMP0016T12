from django.contrib import admin
from .models import User, Developer, Clinician, Admin

# Register your models here.
admin.site.register(User)
admin.site.register(Developer)
admin.site.register(Clinician)
admin.site.register(Admin)