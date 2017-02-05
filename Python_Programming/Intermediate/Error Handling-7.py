## 2. Sets ##

gender=[]

for row in legislators:
    gender.append(row[3])
    
gender=set(gender)

print(gender)

## 3. Exploring the Dataset ##

party=[]
for row in legislators:
    party.append(row[6])
    
party=set(party)
print (party)


## 4. Missing Values ##

for row in legislators:
    if row[3]=="":
        row[3]="M"
        
        
    


## 5. Parsing Birth Years ##

birth_years=[]
for row in legislators:
    parts=row[2].split("-")
    birth_years.append(parts[0])
        

## 6. Try/except Blocks ##

try:
    float("hello")
except Exception:
    print("Error converting to float..")


## 7. Exception Instances ##

try:
    int("")
except Exception as exc:
    print (type(exc))
    print (str(exc))

## 8. The Pass Keyword ##

converted_years = []
for yr in birth_years:
    year=yr
    try:
      year= int(year)
    except Exception:
        pass
    converted_years.append(year)
    

## 9. Convert Birth Years to Integers ##

for row in legislators:
    try:
        year=row[2].split("-")
        birth_year=int(year[0])
    except Exception:
        birth_year=0
    row.append(birth_year)    

## 10. Fill in Years Without a Value ##

last_value =1

for row in legislators:
    if row[7]==0:
        row[7]=last_value
    last_value=row[7]