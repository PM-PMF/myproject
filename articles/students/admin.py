from django.contrib import admin

# Register your models here.admin
from .models import Student,Article
admin.site.register(Student)
admin.site.register(Article)