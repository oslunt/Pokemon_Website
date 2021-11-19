from django.db import models
from django.db.models.fields import CharField

# Create your models here.

# By default pokemon are wild.
# When a user successfully catches a pokemon, wild_pokemon will be changed to false.
# the admin will have control over editing default pokemon in Wild_Pokemon

# a pokemon will be caught when the user guesses a number between the high_num and low_num

class Pokemon(models.Model):
    poke_id= models.IntegerField(primary_key=True)
    poke_name = models.CharField(max_length=30)
    poke_pic = models.ImageField(upload_to='uploads/')
    low_num = models.IntegerField()
    high_num = models.IntegerField()
    wild_pokemon = models.BooleanField(default=True) #if updated to false, pokemon has been caught

    def __str__(self):
        return (self.poke_name)
    





