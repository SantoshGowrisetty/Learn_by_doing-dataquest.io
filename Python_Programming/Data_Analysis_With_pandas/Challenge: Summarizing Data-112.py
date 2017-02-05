## 2. Introduction to the Data ##

import pandas as pd
all_ages=pd.read_csv("all-ages.csv")
recent_grads=pd.read_csv("recent-grads.csv")
print(all_ages[0:5])
print(recent_grads[0:5])

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique().tolist)

aa_cat_counts = dict()
rg_cat_counts = dict()

for major in all_ages['Major_category'].unique().tolist():
    major_rows=all_ages[all_ages["Major_category"]==major]
    aa_cat_counts[major]=major_rows["Total"].sum()
for major in recent_grads["Major_category"].unique().tolist():
    major_rows=recent_grads[recent_grads["Major_category"]==major]
    rg_cat_counts[major]=major_rows["Total"].sum()

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0
low_wage_percent=recent_grads["Low_wage_jobs"].sum()/recent_grads["Total"].sum() 
print(Low_wage_jobs)

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0


for major in majors:
    all_ages_uer=all_ages[all_ages["Major"]==major]["Unemployment_rate"].sum()
    recent_grad_uer=recent_grads[recent_grads["Major"]==major]["Unemployment_rate"].sum()
    if recent_grad_uer <all_ages_uer:
        rg_lower_count+=1
print (rg_lower_count)        
        