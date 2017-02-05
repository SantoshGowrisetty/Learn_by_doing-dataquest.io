## 2. Introduction to the Data ##

import csv
f=open("nfl_suspensions_data.csv")
nfl_suspensions=list(csv.reader(f))
nfl_suspensions=nfl_suspensions[1:]
years={}
for row in nfl_suspensions:
    if row[5] in years:
        years[row[5]] +=1
    else:
        years[row[5]]=1
print (years)
        


## 3. Unique Values ##

teams=[]
games=[]
for row in nfl_suspensions:
    teams.append(row[1])
    games.append(row[2])
unique_teams=set(teams)
unique_games=set(games)
print(unique_teams)
print(unique_games)


## 4. Suspension Class ##

print (nfl_suspensions[2])
class Suspension:
     def __init__(self,nfl_lst):
        self.name=nfl_lst[0]
        self.team=nfl_lst[1]
        self.games=nfl_lst[2]
        self.year=nfl_lst[5]
third_row=nfl_suspensions[2]    
third_suspension=Suspension(third_row)
print(third_suspension.name)


## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year=int(row[5])
        except Exception:
            self.year=0
    def get_year(self):
        return self.year
missing_year=Suspension(nfl_suspensions[22])
twenty_third_year=missing_year.get_year()
        