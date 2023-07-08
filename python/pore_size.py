# Import Packages
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from scipy.stats import norm
import csv
import statistics
from pylab import rcParams

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

mu_a, std_a = norm.fit(a)
mu_b, std_b = norm.fit(b)
mu_c, std_c = norm.fit(c)
mu_d, std_d = norm.fit(d)
fig = plt.figure(figsize=(10, 5))
bin = np.linspace(0, 0.1, 13)
graph = np.linspace(0, 0.1, 50)
plt.hist((a, b, c, d),  bins=bin, color=('firebrick', 'gold', 'green', 'lightseagreen'), label=('R1', 'R2', 'R3', 'R4'))

#plt.hist(a,  bins=bin, color='firebrick', rwidth=0.5, alpha=0.4, label='R1 Histogram')
#plt.hist(b,  bins=bin, color='gold', rwidth=0.5, alpha=0.4, label='R2 Histogram')
#plt.hist(c, bins=bin, color='green', rwidth=0.5, alpha=0.4, label='R3 Histogram')
#plt.hist(d, bins=bin, color='lightseagreen', rwidth=0.5, alpha=0.4, label='R4 Histogram')

p = [x-(x/1.5) for x in norm.pdf(graph, statistics.mean(a), statistics.stdev(a))]
q = [x-(x/1.5) for x in norm.pdf(graph, statistics.mean(b), statistics.stdev(b))]
r = [x-(x/1.5) for x in norm.pdf(graph, statistics.mean(c), statistics.stdev(c))]
s = [x-(x/1.5) for x in norm.pdf(graph, statistics.mean(d), statistics.stdev(d))]
#plt.plot(graph, p, 'firebrick', linewidth=2, label='R1 Gaussian Fit')
#plt.plot(graph, q, 'gold', linewidth=2, label='R2 Gaussian Fit')
#plt.plot(graph, r, 'green', linewidth=2, label='R3 Gaussian Fit')
#plt.plot(graph, s, 'lightseagreen', linewidth=2, label='R4 Gaussian Fit')
plt.legend()
plt.xlabel("Pore Diameter (mm)")
plt.ylabel("Number of Pores")
plt.xlim(0, 0.108)
#plt.plot(a, p, 'k', linewidth=2)
#plt.plot(b, q, 'k', linewidth=2)
#plt.plot(c, r, 'k', linewidth=2)
#plt.plot(d, s, 'k', linewidth=2)
# plt.title("Distribution of Size of Measured Pores in Samples of R1-R4 Extruded Filaments")

plt.savefig('python/output/pore_size_filaments.svg', format='svg',dpi=1200,bbox_inches='tight')
plt.show()