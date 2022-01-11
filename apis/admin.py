from django.contrib import admin

# Register your models here.
from .models import StandardJob, Job5

admin.site.register([StandardJob, Job5])
