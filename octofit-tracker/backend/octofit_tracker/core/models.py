
from djongo import models

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)

class Activity(models.Model):
	user = models.CharField(max_length=100)
	type = models.CharField(max_length=100)
	duration = models.IntegerField()
	team = models.CharField(max_length=100)

class Leaderboard(models.Model):
	team = models.CharField(max_length=100)
	points = models.IntegerField()

class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
