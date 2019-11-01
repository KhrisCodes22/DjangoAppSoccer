from django.shortcuts import render, get_object_or_404
from .models import Team, Game, Player, GoalEvent
import re
from django.core import serializers
# Create your views here.
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist

# display home page to users
# to do this, grab all games and teams and show them to the user
def home(request, weekID="None"):
    teams = Team.objects.all()
    # default week is just the current week, found by adding up the total games played by the team
    if(weekID == "None"):
        totalGamesPlayed = teams[0].Wins + teams[0].Losses + teams[0].Draws
        week = totalGamesPlayed
        prevWeek = week - 1
        nextWeek = week + 1
        top10Scorers = Player.objects.all().order_by('goals')[:10]
        try:
            games = Game.objects.filter(week=week).order_by(
                'game_date')
            numGames = games.count()
        except ObjectDoesNotExist:
            errorMessage = "Our server cannot find games for this week!"
            return render(request,'soccerStuff/error.html', {'errorText': errorMessage})

        return render(request, 'soccerStuff/home.html', {'teams': teams, 'games': games, 'week': week,
                                                         'prevWeek': prevWeek, 'nextWeek': nextWeek, 'numGames': numGames, 'topScorers': top10Scorers})
    # if weekID is equal to something
    else:
        week = weekID
        prevWeek = week - 1
        nextWeek = week + 1
        top10Scorers = Player.objects.all().order_by('goals')[:10]
        try:
            games = Game.objects.filter(
                week=week).order_by("game_date")
            numGames = games.count()
        except ObjectDoesNotExist:
            return HttpResponseNotFound('Our server cannot find games for this week')
        return render(request, "soccerStuff/home.html", {'teams': teams, 'games': games, 'week': week, 'prevWeek': prevWeek,
                                                         'nextWeek': nextWeek, 'numGames': numGames, 'topScorers': top10Scorers})


# view a specific team
def team_detail(request, name):
    # get the team info, and get all players who play on that team.
    try:
        specificTeam = Team.objects.get(name=name)
        allPlayers = Player.objects.filter(team=name)
        return render(request, 'soccerStuff/team_detail.html', {'team': specificTeam, 'Players': allPlayers})
    except ObjectDoesNotExist:
        errorMessage = "We can't find the team you are looking for!"
        return render(request, 'soccerStuff/error.html', {'errorText': errorMessage})

# view a specific game

def game_detail(request, id):
    try:
        allGoals = GoalEvent.objects.filter(gameID=id).order_by("minuteScored")
        specificGame = Game.objects.get(id=id)
        homeTeam = re.sub("_", " ", specificGame.home_team_name.name)
        awayTeam = re.sub("_", " ", specificGame.away_team_name.name)
        location = specificGame.home_team_name.location
        gameString = str(specificGame.home_goals) + "-" + str(specificGame.away_goals)
        return render(request, 'soccerStuff/game_detail.html', {'game': specificGame, "homeTeam": homeTeam, "awayTeam": awayTeam, "goals": allGoals, 'gameString': gameString, 'location': location})
    #if no goals are scored
    except ObjectDoesNotExist:
        allGoals = GoalEvent.objects.none()
        try:
            #still try to see if a game does exist
            specificGame = Game.objects.get(id=id)
            homeTeam = re.sub(str(specificGame.home_team_name.name), "_", " ")
            awayTeam = re.sub(str(specificGame.away_team_name.name), "_", " ")
            gameString = "0-0"
            location = specificGame.home_team_name.location
            return render(request, 'soccerStuff/game_detail.html', {'game': specificGame, "homeTeam": homeTeam, "awayTeam": awayTeam, "goals": allGoals, 'gameString': gameString, 'location': location})
        #if no goals and game doesn't exist
        except ObjectDoesNotExist:
            errorMessage = "We can't find the game you are looking for"
            return render(request, "soccerStuff/error.html",{'errorText': errorMessage})