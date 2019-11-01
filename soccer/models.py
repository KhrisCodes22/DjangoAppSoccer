from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=100)
    top_scorer = models.CharField(max_length=100)
    Wins = models.IntegerField(null=True)
    awayWins = models.IntegerField(null=True)
    homeWins = models.IntegerField(null=True)
    Draws = models.IntegerField(null=True)
    awayDraws = models.IntegerField(null=True)
    homeDraws = models.IntegerField(null=True)
    Losses = models.IntegerField(null=True)
    awayLosses = models.IntegerField(null=True)
    homeLosses = models.IntegerField(null=True)
    Points = models.IntegerField(null=True)
    awayPoints = models.IntegerField(null=True)
    homePoints = models.IntegerField(null=True)
    GoalsFor = models.IntegerField(null=True)
    awayGF = models.IntegerField(null=True)
    homeGF = models.IntegerField(null=True)
    GoalsAgainst = models.IntegerField(null=True)
    awayGA = models.IntegerField(null=True)
    homeGA = models.IntegerField(null=True)
    GoalDifference = models.IntegerField(null=True)
    awayGD = models.IntegerField(null=True)
    homeGD = models.IntegerField(null=True)
    def __str__(self):
        return self.name

class Game(models.Model):
    away_team_name = models.ForeignKey(
        'Team', related_name="awayTeamName", on_delete=models.CASCADE)
    home_team_name = models.ForeignKey(
        'Team', related_name="homeTeamName", on_delete=models.CASCADE)
    game_date = models.DateTimeField(null=True)
    home_goals = models.IntegerField(null=True)
    away_goals = models.IntegerField(null=True)
    away_team_odds = models.FloatField(null=True)
    home_team_odds = models.FloatField(null=True)
    tie_odds = models.FloatField(null=True)
    isCompleted = models.BooleanField(default=False)
    week = models.IntegerField()
    def __str__(self):
        return "{} at home playing {}".format(self.home_team_name, self.away_team_name)


class Player(models.Model):
    playerName = models.CharField(max_length=100, primary_key=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    goals = models.IntegerField(null=True)
    assists = models.IntegerField(null=True)
    gamesPlayed = models.IntegerField(null=True)
    yellowCards = models.IntegerField(null=True)
    redCards = models.IntegerField(null=True)
    position = models.CharField(max_length=10)
    injured = models.BooleanField(null=True)

    def __str__(self):
        return self.playerName


class GoalEvent(models.Model):
    minuteScored = models.IntegerField(null=True)
    gameID = models.IntegerField(null = False)
    goalScorer = models.CharField(max_length=40)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)