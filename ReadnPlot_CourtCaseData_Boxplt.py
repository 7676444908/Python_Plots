#import library
import pandas as pd
import matplotlib.pyplot as plt

#add csv file to dataframe
df = pd.read_csv('LIMBS_Ministry_Wise_Court_Case_Data_2021.csv')

#create boxplot
boxplot = df.boxplot(figsize = (5,5))
plt.show()
plt.savefig('MinistryVsTotalNumberOfcases_Boxplt.png')
