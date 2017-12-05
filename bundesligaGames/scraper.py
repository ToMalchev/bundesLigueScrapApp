#!/usr/bin/env python                                                                                                                                                                
import os
import sys
import django
import requests
#from bs4 import BeautifulSoup
import json


sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), 'bundesligaGames/')))
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), 'bundesligaGames/bundesligaGames/')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bundesligaGames.settings')
django.setup()

from django.core.exceptions import ObjectDoesNotExist
from bundesLiga.models import *

django.setup()

def scrape():
    
    teams = requests.get('https://www.openligadb.de/api/getavailableteams/bl1/2017')
    matches = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/2017')
    
    dict_matches = json.loads(matches.text)
    dict_teams = json.loads(teams.text)
    
    d_t = [t['TeamName'] for t in dict_teams]
    length1 = len(d_t)
    
    point_v = [0]*length1
    win = [0]*length1
    loss = [0]*length1
    equal = [0]*length1
    
        #goals for team1 and team2
#         points_t1 = 0
#         points_t2 = 0
    
    for match in dict_matches:
        date_match = match['MatchDateTime']
        team1 = match['Team1']['TeamName']
        team2 = match['Team2']['TeamName']
        match_id = match['MatchID']
        points_t1 = 0
        points_t2 = 0
        count1 = 0
        
        if match['MatchIsFinished'] == True:
            for res in match['MatchResults']:
                points_t1 = res['PointsTeam1']
                points_t2 = res['PointsTeam2']
            
        
            for team in dict_teams:
            
                if team['TeamName'] == team1:
                    if points_t1 > points_t2:
                        point_v[count1] += 3
                        win[count1] += 1
                    elif points_t1 == points_t2:
                        point_v[count1] += 1
                        equal[count1] += 1
                    elif points_t1 < points_t2:
                        point_v[count1] += 0
                        loss[count1] += 1
                elif team['TeamName'] == team2:
                    if points_t2 > points_t1:
                        point_v[count1] += 3
                        win[count1] += 1
                    elif points_t2 == points_t1:
                        point_v[count1] += 1
                        equal[count1] += 1 
                    elif points_t2 < points_t1:
                        point_v[count1] += 0
                        loss[count1] += 1
                count1 += 1
        try:
            Match = TeamRanks.objects.get(match_id=match_id)
            check1 = False
            if Match.goals_team1 != points_t1:
                Match.goals_team1 = points_t1
                check1 = True
            if Match.goals_team2 != points_t2:
                Match.goals_team2 = points_t2
                check1 = True
            if Match.date != date_match:
                Match.date = date_match
                check1 = True
            if check1:
                Match.save()
        except Match.DoesNotExist:
                Match = Match(team1=team1, team2=team2, goals_team1=points_t1, goals_team2=points_t2, date = date_match, match_id = match_id)
                Match.save()
        
        for teamName, points, win, loss, equal in zip(d_t, point_v, win,loss, equal):
            try:
                TeamRank = TeamRanks.objects.get(name=teamName)
                check1 = False
                if TeamRank.points != points:
                    TeamRank.points = points
                    check1 = True
                if TeamRank.win != win:
                    TeamRank.win = win
                    check1 = True
                if TeamRank.loss != loss:
                    TeamRank.loss = loss
                    check1 = True
                if TeamRank.equal != equal:
                    TeamRank.equal = equal
                    check1 = True
                if check1:
                    TeamRank.save()
            except TeamRanks.DoesNotExist:
                TeamRank = TeamRanks(name=teamName, points=points, win=win, loss=loss, equal=equal)
                TeamRank.save()
                
        #Creates a new match
if __name__ == '__main__':
    scrape()

    
    
    
    
    
    
    

    