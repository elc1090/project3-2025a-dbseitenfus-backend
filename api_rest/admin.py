from django.contrib import admin

# Register your models here.
from .models import User, Document

admin.site.register(User)
admin.site.register(Document)
