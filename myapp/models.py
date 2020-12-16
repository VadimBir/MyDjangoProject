from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Password(models.Model):
    authorName = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True) #temp NULL need to be the ones auth ed
    nameTag = models.CharField(max_length=64)
    passwordStr = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.nameTag + ' | ' + str(self.authorName)

    def get_absolute_url(self):
        return reverse('password-info', args=(str(self.id)))
