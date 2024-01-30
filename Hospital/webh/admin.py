from django.contrib import admin
from .models import *
#pass:- admin

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appiontment)