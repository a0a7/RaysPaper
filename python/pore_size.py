# Import Packages
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
# from scipy.stats import norm
import csv
import statistics
from pylab import rcParams
from pathlib import Path
import matplotlib as mpl


#### PRESET FOR SERIF ######## CANT HANDLE ÅÄÖ, trick is using $\mathrm{ö}$
fpath = Path(mpl.get_data_path(), "fonts/ttf/cmr10.ttf")
# Look up name un /usr/share/matplotlib/mpl-data/fonts, don't use actual name!
plt.rc('font', **{'size' : 21, 'sans-serif': ['cmr10']})
mpl.rcParams["mathtext.fontset"] = "cm"
plt.rc('axes', unicode_minus=False)
# fig.savefig('example_1.pdf', format='pdf', bbox_inches='tight')

a = []
b = []
c = []
d = []

with open('python/data/pore_sizes.csv','r') as data:
    plots = csv.reader(data, delimiter=',')
    for row in plots:
        a.append(float(row[1]))
        b.append(float(row[2]))
        c.append(float(row[3]))
        d.append(float(row[4]))
    data.close()
fig = plt.figure(figsize=(5, 4))
bin = np.linspace(0, 0.1, 14)
graph = np.linspace(0, 0.1, 50)
#plt.hist((a, b, c, d),  bins=bin, color=('firebrick', 'gold', 'green', 'lightseagreen'), label=('R1', 'R2', 'R3', 'R4'))
subplot = a
plt.hist(subplot, bins=bin, color='firebrick', label='R1')
plt.axvline(x=np.mean(subplot), color='black', linestyle='dashed', linewidth=2, label='Mean')
plt.axvline(x=statistics.median(subplot), color='black', linestyle='dotted', linewidth=2, label='Median')
plt.legend()
plt.xlabel("Pore Diameter (mm)")
plt.ylabel("Number of Pores")
plt.xlim(0, 0.1)
plt.savefig('python/output/pore_size_r1.svg', format='svg',dpi=1200,bbox_inches='tight')
plt.show()