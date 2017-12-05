from django.shortcuts import render
import json
import requests
from .models import TeamRanks, Match

def ranking(request):
    teams = ''
    try:
        teams = TeamRanks.objects.all().order_by('-points')
    except Exception as e:
        teams = ['There are no objects in the DB']

    return render(request, 'bundesLiga/rankingBundesliga.html', {'teams': teams})

def viewAllMatches(request):
    matches = ''
    try:
        matches = Match.objects.all()
    except Exception as e:
        matches = ['There are no objects in the DB']


    return render(request, 'bundesLiga/matchesBundesliga.html', {'matches': matches})

def viewThisWeekendMatches(request):
    matches_this_w  = ''
    try:
        matches_this_w = Match.objects.filter(date__iregex=r'2017-12-(09|10)T+.')
    except Exception as e:
        matches_this_w = ['There are no objects in the DB']

    return render(request, 'bundesLiga/matchesBundesliga.html', {'matches': matches_this_w})

def searchTeam(request):

    team = ''
    try:    
        if request.method == 'POST':
            team_name = request.POST.get('team_name')
            team = TeamRanks.objects.filter(name=team_name)
    except Exception as e:
        team = ['There is no team with that name in the BundesLiga']

    return render(request, 'bundesLiga/searchTeam.html', {'teams': team})
