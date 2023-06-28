# Import Packages
import matplotlib.pyplot as plt
import numpy as np
import csv

x = [0, 1, 2, 3]
y = []
yError = []
plt.grid()

# https://docs.google.com/spreadsheets/d/1ykOrQHeAmM8dNtyoMR6hmHkaLMbebs19JLQCFC3wrN4/edit?usp=sharing
with open('python/data/caliper_scale.csv','r') as data:
    plots = csv.reader(data, delimiter=',')
    counter = 0
    for row in plots:
        if counter % 4 == 0 and counter != 0:
            xval = counter / 4 - 1
            yval = float(row[10])
            y.append(yval)
            plt.errorbar(xval, yval, yerr=float(row[11]), ecolor='#728d9f', elinewidth=2, capsize=4, capthick=2, fmt='none')
            yError.append(float(row[11]))
        counter += 1
    print("\n\n" + str(x))
    print("\n" + str(y))
    print("\n" + str(yError) + "\n\n")
    data.close()
plt.title("")

plt.xlabel("Sample")
plt.ylabel("Density (g/cm³)")

plt.ylim(0, 1.4)
plt.xticks([0, 1, 2, 3], ['R1', 'R2', 'R3', 'R4'])
plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3],
           ['0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3'])


plt.plot(x, y, color='#35424a', marker='o', linewidth=0, markersize=3, )
# plt.bar(x, y, color='#728d9f')

plt.savefig('python/output/average_density.svg', format='svg',dpi=1200,bbox_inches='tight')
plt.show()