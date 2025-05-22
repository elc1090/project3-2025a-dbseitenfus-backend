from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True, default='')
    email = models.EmailField(unique=True, default='')
    password = models.CharField(max_length=128, default='')
    first_name = models.CharField(max_length=30, blank=True, default='')
    last_name = models.CharField(max_length=30, blank=True, default='')

    def __str__(self):
        return self.username
    

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default='')
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title