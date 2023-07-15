# Import Packages
import matplotlib.pyplot as plt
import numpy as np
import csv
from pathlib import Path
import matplotlib as mpl


#### PRESET FOR SERIF ######## CANT HANDLE ÅÄÖ, trick is using $\mathrm{ö}$
fpath = Path(mpl.get_data_path(), "fonts/ttf/cmr10.ttf")
# Look up name un /usr/share/matplotlib/mpl-data/fonts, don't use actual name!
plt.rc('font', **{'size' : 12, 'sans-serif': ['cmr10']})
mpl.rcParams["mathtext.fontset"] = "cm"
plt.rc('axes', unicode_minus=False)


x = [1, 2, 3, 4]
b = [1.16, 2.16, 3.16, 4.16]
y = []
a = []
yError = []
aError = []
plt.grid()

# https://docs.google.com/spreadsheets/d/1ykOrQHeAmM8dNtyoMR6hmHkaLMbebs19JLQCFC3wrN4/edit?usp=sharing
with open('python/data/limonene_test.csv','r') as data:
    plots = csv.reader(data, delimiter=',')
    for row in plots:
            yval = float(row[1])
            y.append(yval)
            yError.append(float(row[2]))
            aval = float(row[6])
            a.append(aval)
            aError.append(float(row[7]))
    data.close()
plt.title("")

plt.xlabel("Sample")
plt.ylabel(r'g Limonene Absorbed per g Absorbent $(g_{limonene}/g_{dry}$)')

plt.xlim(0.5, 4.75)
plt.ylim(0, 0.35)
plt.xticks([1.15, 2.15, 3.15, 4.15], ['R1', 'R2', 'R3', 'R4'])
# plt.yticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5],
     #      ['0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5'])


plt.bar(x, y, color='#51a5b2', label="Extruded Filaments", yerr=yError, ecolor='black', capsize=10, zorder=2, width=0.3, align='center', alpha=0.8)
plt.bar(b, a, color='#800000', label="Hot-Pressed Sheets", yerr=aError, ecolor='black', capsize=10, zorder=2, width=0.3, align='edge', alpha=0.8)

plt.legend()
# plt.errorbar(1, avg1, yerr=0.05, ecolor='#92adbf', elinewidth=2, capsize=4, capthick=2, fmt='none', zorder=1)
# plt.errorbar(4, avg2, yerr=0.03, ecolor='#92adbf', elinewidth=2, capsize=4, capthick=2, fmt='none', zorder=1)
# plt.errorbar(7, avg3, yerr=0.02, ecolor='#92adbf', elinewidth=2, capsize=4, capthick=2, fmt='none', zorder=1)
# plt.errorbar(10, avg4, yerr=0.06, ecolor='#92adbf', elinewidth=2, capsize=4, capthick=2, fmt='none', zorder=1)

# plt.bar(x, y, color='#728d9f')

plt.savefig('python/output/limonene_absorbtion.svg', format='svg',dpi=1200,bbox_inches='tight')
plt.show()