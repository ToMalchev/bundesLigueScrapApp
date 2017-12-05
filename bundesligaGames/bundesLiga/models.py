from django.db import models

class TeamRanks(models.Model):
    name = models.CharField(max_length=50)
    win = models.IntegerField()
    loss = models.IntegerField()
    draws = models.IntegerField()
    points = models.IntegerField()
    def __str__(self):
        return self.position

class Match(models.Model):
     team1 = models.CharField(max_length=50)
     team2 = models.CharField(max_length=50)
     goals_team1 = models.IntegerField()
     goals_team2 = models.IntegerField()
     date = models.CharField(max_length=100)
     match_i = models.IntegerField()
     def __str__(self):
         return self.team1, ' : ', self.team2