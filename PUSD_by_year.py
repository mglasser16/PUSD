#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = 'C:/Users/pjsch/Documents/Melodie/PUSD/Form_response.csv'
#replace file path for your own computer.
#For python to read this code, you must reverse the \ to /

DF = pd.read_csv(filepath)

DF['What year did you graduate?'].fillna(0, inplace=True)
print (DF)
#%%
dict = {}



for i in range(len(DF)):
    if DF.iloc[i,2] != "No":
        dict[DF.iloc[i,3]] = dict.get(DF.iloc[i,3],0) + 1
print(dict)

del dict[0.0]

print(dict)

# %%

keys = dict.keys()

values = dict.values()


plt.bar(keys, values)
# Set the limit
plt.xlim(min(keys),max(keys))

# %%
