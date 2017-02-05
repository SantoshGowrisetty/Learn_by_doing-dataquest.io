## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for i, ship in enumerate(ships):
    print (ship)
    print (cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, row in enumerate(things):
    row.append(trees[i])
    

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled=[apple*2  for apple in apple_prices]
apple_prices_lowered=[apple-100 for apple in apple_prices]


## 5. Counting Female Names ##

name_counts={}
for row in legislators:
    if row[3]=="F" and int(row[7])>1940:
        name =row[1]
        if name in name_counts:
             name_counts[name] += 1
        else :
            name_counts[name]=1     
        
            


## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]


checks= [val  is not None and int(val)>30 for val in values]
            
        
    

## 8. Highest Female Name Count ##

max_value=None
for name in  name_counts:
    count=name_counts[name]
    if max_value == None or count >max_value:
        max_value=count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for platn,value in plant_types.items():
    print(platn)
    print(value)

## 10. Finding the Most Common Female Names ##

top_female_names = []
for name,count in name_counts.items():
    if count==2:
        top_female_names.append(name)

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts={}
highest_male_count=0
for leg in legislators:
    if leg[3]=="M" and int(leg[7])>1940:
        if leg[1]   in   male_name_counts:
            male_name_counts[leg[1]] +=1
        else :
            male_name_counts[leg[1]]=1
for male, cnt in male_name_counts.items():
    if cnt>highest_male_count:
        highest_male_count=cnt
for male, cnt in male_name_counts.items():       
    if cnt==highest_male_count:
        top_male_names.append(male)