import matplotlib.pyplot as plt
import csv
from datetime import datetime

dates = []
numbers1 = []
numbers2 = []
numbers3 = []
numbers4 = []
numbers5 = []


# Read data from CSV
with open('grt_rates.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        dates.append(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f'))
        numbers1.append(float(row[1]))
        numbers2.append(float(row[2]))
        numbers3.append(float(row[3]))
        numbers4.append(float(row[4]))
        numbers5.append(float(row[5]))

# Plot all numbers on the same graph with different colors
plt.plot(dates, numbers1, label='Gold 24', color='red')
plt.plot(dates, numbers2, label='Gold 22', color='green')
plt.plot(dates, numbers3, label='Gold 18', color='orange')
plt.plot(dates, numbers4, label='Platinum', color='grey')
plt.plot(dates, numbers5, label='Silver', color='blue')

# Add labels, title, legend, and grid
plt.xlabel('Date')
plt.ylabel('Rates')
plt.title('Rates over time')
plt.legend()  # Show legend for the different lines
plt.grid(True)

# Display the graph
plt.show()