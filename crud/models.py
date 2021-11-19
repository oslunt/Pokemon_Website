from django.db import models
from game.models import Pokemon
from tails.models import Person

# at the end of the game the user will be displayed with 
# the pokemon they caught and whether they caught them all
# it will display the pokemon they caught and the pokemon they didn't catch

# Create your models here.
class EndGame(models.Model):
    user_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    poke_caught = models.CharField(max_length=30) 
    poke_missed = models.CharField(max_length=30)
    poke_pic = models.ImageField(Pokemon, upload_to='uploads/')
    poke_id = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
