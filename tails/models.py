from django.db import models

# Create your models here.

# table will store as single user_name just like an arcade machine and everything else 
# that happens in the site/app will be associated with this user

class Person(models.Model):
    user_name = models.CharField(max_length=30)
    
    def __str__(self):
            return (self.user_name)