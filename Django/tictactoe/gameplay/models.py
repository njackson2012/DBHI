from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    firstPlayer = models.ForeignKey(User, related_name="gamesFirstPlayer", on_delete=models.CASCADE)
    secondPlayer = models.ForeignKey(User, related_name="gamesSecondPlayer", on_delete=models.CASCADE)
    startTime = models.DateTimeField(auto_now_add=True)
    lastActive = models.DateTimeField(auto_now=True)

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    byFirstPlayer = models.BooleanField()

    game=models.ForeignKey(Game, on_delete=models.CASCADE)