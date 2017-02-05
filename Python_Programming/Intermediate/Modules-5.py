## 3. The Math Module ##

import math
a=math.sqrt(16)
b=math.ceil(111.3)
c=math.floor(89.9)

## 4. Variables Within Modules ##

import math

print(math.pi)
a=math.sqrt(math.pi)
b=math.ceil(math.pi)
c=math.floor(math.pi)

## 5. The CSV Module ##

import csv
nfl=list(csv.reader(open("nfl.csv")))


## 6. Counting How Many Times a Team Won ##

import csv

f=csv.reader(open("nfl.csv"))

nfl_list=list(f)
counter=0
for lst in nfl_list:
    if int(lst[0])>=2009 and int(lst[0])<=2013 and lst[2]=="New England Patriots":
        counter +=1
        
patriots_wins=counter


## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins(lst,winner):
    count=0
    for lstr in lst:
         if lstr[2]==winner:
           count+=1
    return count
cowboys_wins=nfl_wins(nfl,"Dallas Cowboys")
falcons_wins=nfl_wins(nfl,"Atlanta Falcons")

# Define your function here.

## 10. Working with Boolean Operators ##

a = 5
b = 10
# a == 5
result1 = True

# a < 5 or b > a
result2 = True

# a < 5 and b > a
result3 = False

# a == 5 or b == 5
result4 = True

# a > b or a == 10
result5 = False

## 11. Counting Wins in a Given Year ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins(team,year):
    count = 0
    for row in nfl:
        if int(row[0])==year and row[2] == team:
            count = count + 1
    return count

browns_2010_wins=nfl_wins("Cleveland Browns",2010)
eagles_2011_wins=nfl_wins("Philadelphia Eagles",2011)