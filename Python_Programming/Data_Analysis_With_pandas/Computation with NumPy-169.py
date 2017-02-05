## 2. Array Comparisons ##

import numpy as np
countries_canada=np.array([country=="Canada" for country in world_alcohol[:,2]])
years_1984= np.array([int(year)==1984 for year in world_alcohol[:,0]])

    


## 3. Selecting Elements ##

import numpy as np

country_is_algeria = np.array(world_alcohol[:,2]=="Algeria")
country_algeria=world_alcohol[world_alcohol[:,2]=="Algeria"]

## 4. Comparisons with Multiple Conditions ##

import numpy as np

is_algeria_and_1986=(world_alcohol[:,0]=="1986")&(world_alcohol[:,2]=="Algeria")
rows_with_algeria_and_1986=world_alcohol[is_algeria_and_1986]

## 5. Replacing Values ##

import numpy as np

is_world_alcohol_1986=np.array(world_alcohol[:,0]=="1986")
world_alcohol[is_world_alcohol_1986,0]="2014"

is_wine=np.array(world_alcohol[:,3]=="Wine")
world_alcohol[is_wine,3]="Grog"


## 6. Replacing Empty Strings ##

is_value_empty=(world_alcohol[:,4]=="")
world_alcohol[is_value_empty,4]="0"

## 7. Converting Data Types ##

alcohol_consumption=(world_alcohol[:,4]).astype(float)


## 8. Computing with NumPy ##

total_alcohol=alcohol_consumption.sum()
average_alcohol=alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

canada_1986=world_alcohol[(world_alcohol[:,0]=="1986")&(world_alcohol[:,2]=="Canada")]
canada_alcohol=canada_1986[:,4]
canada_alcohol[(canada_alcohol[0]=="")]="0"
canada_alcohol=canada_alcohol.astype(float)
total_canadian_drinking=canada_alcohol.sum()



## 10. Calculating Consumption for Each Country ##

totals = {}

for country in countries:
    totals[country]=world_alcohol[(world_alcohol[:,0]=="1989")&(world_alcohol[:,2]==country),4].astype(float).sum()


## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for key in totals:
    if totals[key]>highest_value:
        highest_value=totals[key]
        highest_key=key
  
        