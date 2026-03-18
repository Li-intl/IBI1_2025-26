import matplotlib.pyplot as plt
import numpy
population={"UK":(66.7,69.2),"China":(1426,1410),"Italy":(59.4,58.9),"Brazil":(208.6,212.0),"USA":(331.6,340.1)}
percentchange={}
RATE={}
#RATE is a new dictionary, I will use it to compare the specific growth rate of each country.
for name,(p2020,p2024) in population.items():
    rate=(p2024-p2020)*100/p2020
    RATE[name]=rate
sortRATE=dict(sorted(RATE.items(),key=lambda x: x[1],reverse=True))
#I use sorted to compare the rate of diferent countries. it is in a dictionary so I use key=lambda x: x[1] to compare their values(rate) instead of comparing keys(countries' name) 
print(f"here are the growth rate of different countries in order: {sortRATE}")
most=max(sortRATE,key=sortRATE.get)
least=min(sortRATE,key=sortRATE.get)
print(f"{most} has the largest population,{least} has the minimum population")