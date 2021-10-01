import matplotlib.pyplot as plt
import csv
  
x = []
y = []

# Opening the csvfile  
with open('LIMBS_Ministry_Wise_Court_Case_Data_2021.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter = ',')

# This skips the first row of the CSV file.
	next(plots)
#plots = csv.reader(csvfile, delimiter = ',')
    
	for row in plots:
		x.append(row[0])
		y.append(int(row[4]))
  
plt.bar(x, y, color = 'g', width = 0.72, label = "Cases")
plt.xlabel('S.No of Ministry')
plt.ylabel('Total Number of cases')
plt.title('Ministry Vs Total Number of cases')
plt.legend()
plt.show()
plt.show()
plt.savefig('MinistryVsTotalNumberOfcases_barplt.png')
