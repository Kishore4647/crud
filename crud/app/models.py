from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to='receipe')
    receipe_view_count = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.receipe_name
