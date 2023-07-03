#Filter out campaigns with clicks greater than 12, using loop.

import pandas as pd 

data1 = pd.read_excel(r'C:\Users\Anele Ngcobo\Desktop\Basic2AdvancedPythonII\CampaignData\output2.xlsx',sheet_name="X3")
data2= pd.read_excel(r'C:\Users\Anele Ngcobo\Desktop\Basic2AdvancedPythonII\CampaignData\output3.xlsx',sheet_name="X3")

lst = []
for r in range(len(data1)):
    if data1.iloc[r,3] > 12:
       lst.append(data1.loc[r])
print(lst)

newdata=pd.DataFrame(lst)
print(newdata)

    
    