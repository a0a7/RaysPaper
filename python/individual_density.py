# Import Packages
import matplotlib.pyplot as plt
import numpy as np
import csv

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y = []
yError = []
plt.grid()

# https://docs.google.com/spreadsheets/d/1ykOrQHeAmM8dNtyoMR6hmHkaLMbebs19JLQCFC3wrN4/edit?usp=sharing
with open('python/data/caliper_scale.csv','r') as data:
    plots = csv.reader(data, delimiter=',')
    counter = 0
    for row in plots:
        if counter % 4 != 0 and counter != 0:
            yval = float(row[10])
            y.append(yval)
        counter += 1
    print("\n\n" + str(x))
    print("\n" + str(y))
    data.close()
plt.title("")

plt.xlabel("Sample")
plt.ylabel("Density (g/cm³)")

plt.xlim(-1, 12)
plt.ylim(0.3, 1.5)
plt.xticks([1, 4, 7, 10], ['R1', 'R2', 'R3', 'R4'])
plt.yticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5],
           ['0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5'])

avg1 = (y[0] + y[1] + y[2])/3
avg2 = (y[3] + y[4] + y[5])/3
avg3 = (y[6] + y[7] + y[8])/3
avg4 = (y[9] + y[10] + y[11])/3

plt.plot(x, y, color='#35424a', marker='o', linewidth=0, markersize=4, label="Single Sample Values")
plt.plot([0, 2], [avg1, avg1], color='#728d9f', linestyle='--', linewidth=2, label="Average Filament Values")
plt.plot([3, 5], [avg2, avg2], color='#728d9f', linestyle='--', linewidth=2)
plt.plot([6, 8], [avg3, avg3], color='#728d9f', linestyle='--', linewidth=2)
plt.plot([9, 11], [avg4, avg4], color='#728d9f', linestyle='--', linewidth=2)
plt.legend()
# plt.errorbar(1, avg1, yerr=0.05, ecolor='#92adbf', elinewidth=2, capsize=4, capthick=2, fmt='none', zorder=1)
# plt.errorbar(4, avg2, yerr=0.03, ecolor='#92adbf', elinewidth=2, capsize=4, capthick=2, fmt='none', zorder=1)
# plt.errorbar(7, avg3, yerr=0.02, ecolor='#92adbf', elinewidth=2, capsize=4, capthick=2, fmt='none', zorder=1)
# plt.errorbar(10, avg4, yerr=0.06, ecolor='#92adbf', elinewidth=2, capsize=4, capthick=2, fmt='none', zorder=1)

# plt.bar(x, y, color='#728d9f')

plt.savefig('python/output/individual_density.svg', format='svg',dpi=1200,bbox_inches='tight')
plt.show()