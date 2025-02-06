from django.db import models
from django.contrib.auth.models import User 

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, unique=True)
    content = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # One note belongs to one user.
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

