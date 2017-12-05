import requests
#from bs4 import BeautifulSoup
import json
from bundesligaGames.celery import app
from .models import TeamRanks, Match


@app.task #(bind=True)
def scrape():
    
     teams = requests.get('https://www.openligadb.de/api/getavailableteams/bl1/2017')
    matches = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/2017')
    
    dict_matches = json.loads(matches.text)
    dict_teams = json.loads(teams.text)
    
    d_t = [t['TeamName'] for t in dict_teams]
    length1 = len(d_t)
    
    point_v = [0]*length1
    win_t = [0]*length1
    loss_t = [0]*length1
    equal_t = [0]*length1
    
    #goals for team1 and team2
#    points_t1 = 0
#    points_t2 = 0
    
    for match in dict_matches:
        date_match = match['MatchDateTime']
        team1 = match['Team1']['TeamName']
        team2 = match['Team2']['TeamName']
        idMatch = match['MatchID']
        points_t1 = 0
        points_t2 = 0
        
        
        if match['MatchIsFinished'] == True:
            for res in match['MatchResults']:
                points_t1 = res['PointsTeam1']
                points_t2 = res['PointsTeam2']
            count1 = 0
        
            for team in dict_teams:
            
                if team['TeamName'] == team1:
                    if points_t1 > points_t2:
                        point_v[count1] += 3
                        win_t[count1] += 1
                    elif points_t1 == points_t2:
                        point_v[count1] += 1
                        equal_t[count1] += 1
                    elif points_t1 < points_t2:
                        point_v[count1] += 0
                        loss_t[count1] += 1
                elif team['TeamName'] == team2:
                    if points_t2 > points_t1:
                        point_v[count1] += 3
                        win_t[count1] += 1
                    elif points_t2 == points_t1:
                        point_v[count1] += 1
                        equal_t[count1] += 1 
                    elif points_t2 < points_t1:
                        point_v[count1] += 0
                        loss_t[count1] += 1
                count1 += 1
        try:
            match = Match.objects.get(match_i=idMatch)
            check1 = False
            if match.goals_team1 != points_t1:
                match.goals_team1 = points_t1
                check1 = True
            if match.goals_team2 != points_t2:
                match.goals_team2 = points_t2
                check1 = True
            if match.date != date_match:
                match.date = date_match
                check1 = True
            if check1:
                match.save()
        except Exception as e:
                match = Match(team1=team1, team2=team2, goals_team1=points_t1, goals_team2=points_t2, date = date_match, match_i = idMatch)
                match.save()
        
        for teamName, points, win, loss, equal in zip(d_t, point_v, win_t, loss_t, equal_t):
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
                if TeamRank.draws != equal:
                    TeamRank.draws = equal
                    check1 = True
                if check1:
                    TeamRank.save()
            except TeamRanks.DoesNotExist:
                TeamRank = TeamRanks(name=teamName, points=points, win=win, loss=loss, draws=equal)
                TeamRank.save()
        #Creates a new match
# if __name__ == '__main__':
#     scrape()

    
    
    
    
    
    
    

    
