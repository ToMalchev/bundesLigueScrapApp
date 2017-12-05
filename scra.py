import requests
from bs4 import BeautifulSoup
import json

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
    points_t1 = 0
    points_t2 = 0
    
    for match in dict_matches:
        date_match = match['MatchDateTime']
        team1 = match['Team1']['TeamName']
        team2 = match['Team2']['TeamName']
#         points_t1 = 0
#         points_t2 = 0
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
    for i,j,z,v,t in zip(d_t, point_v, win,loss, equal):
        print(i,j,int(z),v,t)
        
        #Creates a new match
scrape()