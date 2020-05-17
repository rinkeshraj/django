from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class match(models.Model):
   first_name = models.CharField(max_length = 10)
   last_name = models.CharField(max_length=10)
   username = models.CharField(User,max_length=20)
   email = models.EmailField(max_length=30)

   class Meta:
         pass
   
   def __str__(self):
        return self.User