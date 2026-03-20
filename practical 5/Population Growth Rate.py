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
#i think maybe use dictionary{sortRATE} I set before to pick up the "most" and "least" is better. but it happened some probelms when i was coding. so finally I use this "stupid" way (which I have used in "Heart Rate Analysis")
countries=[]
change_rates=[]
for country,changerate in sortRATE.items():
    countries.append(country)
    change_rates.append(changerate)
plt.figure(figsize=(10,10))
bars = plt.bar(countries, change_rates, color=['green' if r > 0 else 'red' for r in change_rates])


plt.title('Population Percentage Change (2020-2024)')
plt.xlabel('Country')
plt.ylabel('Percentage Change (%)')
plt.xticks(rotation=45)
plt.grid(axis='y',linestyle='--',alpha=0.7) 
#following 7 lines(32-38) are AI help generated, and I have learnt it.
for bar in bars:
    height=bar.get_height()
    va='bottom' if height > 0 else 'top'
    label=f"{height:.2f}%"
    plt.text(bar.get_x()+bar.get_width()/2.,height,label,
             ha='center', va=va, fontsize=10)
plt.tight_layout()
plt.show()