from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from pollingapp.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

