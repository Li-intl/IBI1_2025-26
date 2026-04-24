import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


dalys_data = pd.read_csv('dalys-rate-from-all-causes.csv')


print("\nthe first 10 year data of afgan:  ")
afghan_first_10 = dalys_data.iloc[0:10, 2:4] 
print(afghan_first_10)

max_daly_idx = afghan_first_10.iloc[:, 1].idxmax() # find out the max DALY
max_year_afghan = afghan_first_10.loc[max_daly_idx].iloc[0]
print(f"in the first 10 year in afghan, {max_year_afghan} year contains the maximum DALY")

# answer: The year reporting the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistan is [1998].



print("\nZimbabwe data record year:  ")
# when Entity is Zimbabwe, value = True
is_zimbabwe = dalys_data['Entity'] == 'Zimbabwe' 
zimbabwe_years = dalys_data.loc[is_zimbabwe, 'Year']
print(f"the first year: {zimbabwe_years.min()}, the last year: {zimbabwe_years.max()}")

# answer: For Zimbabwe, the first year recorded is [1990], and the last year recorded is [2019].


print("\n2019 countries with maximum and minmum DALYs")
#get 2019 data
recent_data = dalys_data.loc[dalys_data['Year'] == 2019, ["Entity", "DALYs"]]

max_idx_2019 = recent_data['DALYs'].idxmax()
min_idx_2019 = recent_data['DALYs'].idxmin()

max_country = recent_data.loc[max_idx_2019, 'Entity']
min_country = recent_data.loc[min_idx_2019, 'Entity']

print(f"2019 the country with the maximun DALYs: {max_country}")
print(f"2019 the country with the minimum DALYs: {min_country}")

# answer: In 2019, the country with the maximum DALYs is [Lesotho], and the country with the minimum DALYs is [Singapore].


target_country_data = dalys_data.loc[dalys_data['Entity'] == min_country]


plt.figure(figsize=(10, 6))
plt.plot(target_country_data['Year'], target_country_data['DALYs'], 'b-o') 

#all plots are clearly labelled
plt.title(f'Burden of Disease (DALYs) over time in {min_country}')
plt.xlabel('Year')
plt.ylabel('DALYs (Disability-Adjusted Life Years)')

plt.xticks(target_country_data['Year'], rotation=-90) 
plt.tight_layout() 
plt.show()



#question: What country or countries have recorded a DALYs less than 18,000 in a single year?
print("\nansweing question:  ")
low_dalys_countries = dalys_data.loc[dalys_data['DALYs'] < 18000, 'Entity'].unique()
print("Recorded DALYs < 18,000:")
print(low_dalys_countries)
#answer:['Iceland','Israel', 'Japan', 'Singapore', 'South Korea','Spain', 'Switzerland']