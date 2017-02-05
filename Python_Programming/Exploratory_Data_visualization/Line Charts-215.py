## 2. Introduction To The Data ##

import pandas as pd
unrate=pd.read_csv("unrate.csv")
unrate["DATE"]=pd.to_datetime(unrate["DATE"])
print(datetime)
print (unrate[0:12])

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt
plt.plot()
plt.show()

## 7. Adding Data ##

plt.plot(unrate["DATE"][0:12],unrate["VALUE"][0:12])
plt.show()