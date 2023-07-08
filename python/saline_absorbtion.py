# Import Packages
import matplotlib.pyplot as plt
import numpy as np
import csv

x = [0, 1, 5, 10, 30]
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []

aErr = []
bErr = []
cErr = []
dErr = []
eErr = []
fErr = []
gErr = []
hErr = []

plt.grid()

# https://docs.google.com/spreadsheets/d/1ykOrQHeAmM8dNtyoMR6hmHkaLMbebs19JLQCFC3wrN4/edit?usp=sharing
with open('python/data/saline_absorbtion.csv','r') as data:
    plots = csv.reader(data, delimiter=',')
    counter = 0;
    for row in plots:
        series = chr(counter + 96)
        if counter > 0:
            exec(series + '.append(float(row[3]))')
            exec(series + '.append(float(row[4]))')
            exec(series + '.append(float(row[5]))')
            exec(series + '.append(float(row[6]))')
            exec(series + '.append(float(row[7]))')
            exec(series + 'Err.append(0)')
            exec(series + 'Err.append(float(row[8]))')
            exec(series + 'Err.append(float(row[9]))')
            exec(series + 'Err.append(float(row[10]))')
            exec(series + 'Err.append(float(row[11]))')
        counter += 1
    data.close()
plt.title("")
plt.xlim(0, 30.5)
plt.xlabel(r'Time in Solution $(min)$')
plt.ylabel(r'Saline Absorbed $(g)$')

# plt.xlim(0.5, 4.75)
plt.xticks([0, 1, 5, 10, 30], ['0', '1', '5', '10', '30'])
plt.ylim(0, 1.25)
# plt.yticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5],
     #      ['0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5'])

plt.plot(x, a, color='firebrick', marker='o', linewidth=2, markersize=4, label="R1 Sheet", zorder=2, alpha=0.8 )
plt.plot(x, b, color='gold', marker='o', linewidth=2, markersize=4, label="R2 Sheet", zorder=2, alpha=0.8 )
plt.plot(x, c, color='green', marker='o', linewidth=2, markersize=4, label="R3 Sheet", zorder=2, alpha=0.8 )
plt.plot(x, d, color='lightseagreen', marker='o', linewidth=2, markersize=4, label="R4 Sheet", zorder=2, alpha=0.8 )
plt.plot(x, e, color='red', marker='o', linewidth=2, markersize=4, label="R1 Filament", zorder=2, alpha=0.8 )
plt.plot(x, f, color='yellow', marker='o', linewidth=2, markersize=4, label="R2 Filament", zorder=2, alpha=0.8 )
plt.plot(x, g, color='lime', marker='o', linewidth=2, markersize=4, label="R3 Filament", zorder=2, alpha=0.8 )
plt.plot(x, h, color='aqua', marker='o', linewidth=2, markersize=4, label="R4 Filament", zorder=2, alpha=0.8 )



plt.errorbar(x, a, yerr=aErr, color='black', zorder=3, alpha=0.3, capsize=4, capthick=2, fmt='none' )
plt.errorbar(x, b, yerr=bErr, color='black', zorder=3, alpha=0.3, capsize=4, capthick=2, fmt='none' )
plt.errorbar(x, c, yerr=cErr, color='black', zorder=3, alpha=0.3, capsize=4, capthick=2, fmt='none'  )
plt.errorbar(x, d, yerr=dErr, color='black', zorder=3, alpha=0.3, capsize=4, capthick=2, fmt='none'  )
plt.errorbar(x, e, yerr=eErr, color='black', zorder=3, alpha=0.3, capsize=4, capthick=2, fmt='none'  )
plt.errorbar(x, f, yerr=fErr, color='black', zorder=3, alpha=0.3, capsize=4, capthick=2, fmt='none'  )
plt.errorbar(x, g, yerr=gErr, color='black', zorder=3, alpha=0.3, capsize=4, capthick=2, fmt='none'  )
plt.errorbar(x, h, yerr=hErr, color='black', zorder=3, alpha=0.3, capsize=4, capthick=2, fmt='none' )

plt.legend()
# plt.errorbar(1, avg1, yerr=0.05, ecolor='#92adbf', elinewidth=2, capsize=4, capthick=2, fmt='none', zorder=1)
# plt.errorbar(4, avg2, yerr=0.03, ecolor='#92adbf', elinewidth=2, capsize=4, capthick=2, fmt='none', zorder=1)
# plt.errorbar(7, avg3, yerr=0.02, ecolor='#92adbf', elinewidth=2, capsize=4, capthick=2, fmt='none', zorder=1)
# plt.errorbar(10, avg4, yerr=0.06, ecolor='#92adbf', elinewidth=2, capsize=4, capthick=2, fmt='none', zorder=1)

# plt.bar(x, y, color='#728d9f')

plt.savefig('python/output/centrifuge_retention_all.svg', format='svg',dpi=1200,bbox_inches='tight')
plt.show()

plt.clf()

sheets = []
filaments = []
sheets.append((a[0] + b[0] + c[0] + d[0])/4)
sheets.append((a[1] + b[1] + c[1] + d[1])/4)
sheets.append((a[2] + b[2] + c[2] + d[2])/4)
sheets.append((a[3] + b[3] + c[3] + d[3])/4)
sheets.append((a[4] + b[4] + c[4] + d[4])/4)

filaments.append((e[0] + f[0] + g[0] + h[0])/4)
filaments.append((e[1] + f[1] + g[1] + h[1])/4)
filaments.append((e[2] + f[2] + g[2] + h[2])/4)
filaments.append((e[3] + f[3] + g[3] + h[3])/4)
filaments.append((e[4] + f[4] + g[4] + h[4])/4)

plt.plot(x, filaments, color='#35424a', label="Average of Extruded Filaments", marker='o', linewidth=2, markersize=4, zorder=2)
plt.plot(x, sheets, color='#b30000', label="Average of Hot-Pressed Sheets", marker='o', linewidth=2, markersize=4, zorder=2)
plt.legend()
plt.xlim(0, 30.5)
plt.xlabel(r'Time in Solution $(min)$')
plt.ylabel(r'Saline Absorbed $(g)$')

plt.xticks([0, 1, 5, 10, 30], ['0', '1', '5', '10', '30'])
plt.ylim(0, 1.25)


plt.savefig('python/output/centrifuge_retention_sheets_v_filaments.svg', format='svg',dpi=1200,bbox_inches='tight')
plt.show()

plt.clf()
plt.plot(x, f, color='gold', marker='o', linewidth=2, markersize=4, label="R2 Filament", zorder=2, alpha=0.8 )
plt.plot(x, e, color='red', marker='o', linewidth=2, markersize=4, label="R1 Filament", zorder=2, alpha=0.8 )
plt.plot(x, a, color='firebrick', marker='o', linewidth=2, markersize=4, label="R1 Sheet", zorder=2, alpha=0.8 )
plt.plot(x, b, color='goldenrod', marker='o', linewidth=2, markersize=4, label="R2 Sheet", zorder=2, alpha=0.8 )

plt.errorbar(x, a, yerr=aErr, color='black', zorder=3, alpha=0.25, capsize=4, capthick=2, fmt='none' )
plt.errorbar(x, b, yerr=bErr, color='black', zorder=3, alpha=0.25, capsize=4, capthick=2, fmt='none' )
plt.errorbar(x, e, yerr=eErr, color='black', zorder=3, alpha=0.25, capsize=4, capthick=2, fmt='none'  )
plt.errorbar(x, f, yerr=fErr, color='black', zorder=3, alpha=0.25, capsize=4, capthick=2, fmt='none'  )
plt.xlim(0, 30.5)
plt.xlabel(r'Time in Solution $(min)$')
plt.ylabel(r'Saline Absorbed $(g)$')

# plt.xlim(0.5, 4.75)
plt.xticks([0, 1, 5, 10, 30], ['0', '1', '5', '10', '30'])
plt.ylim(0, 1.25)

plt.grid()

plt.legend(loc='lower right')
plt.savefig('python/output/centrifuge_retention_r1r2.svg', format='svg',dpi=1200,bbox_inches='tight')
plt.show()



plt.plot(x, c, color='green', marker='o', linewidth=2, markersize=4, label="R3 Sheet", zorder=2, alpha=0.8 )
plt.plot(x, d, color='lightseagreen', marker='o', linewidth=2, markersize=4, label="R4 Sheet", zorder=2, alpha=0.8 )
plt.plot(x, g, color='lime', marker='o', linewidth=2, markersize=4, label="R3 Filament", zorder=2, alpha=0.8 )
plt.plot(x, h, color='aqua', marker='o', linewidth=2, markersize=4, label="R4 Filament", zorder=2, alpha=0.8 )

plt.errorbar(x, c, yerr=cErr, color='black', zorder=3, alpha=0.3, capsize=4, capthick=2, fmt='none'  )
plt.errorbar(x, d, yerr=dErr, color='black', zorder=3, alpha=0.3, capsize=4, capthick=2, fmt='none'  )
plt.errorbar(x, g, yerr=gErr, color='black', zorder=3, alpha=0.3, capsize=4, capthick=2, fmt='none'  )
plt.errorbar(x, h, yerr=hErr, color='black', zorder=3, alpha=0.3, capsize=4, capthick=2, fmt='none' )
plt.xlim(0, 30.5)
plt.xlabel(r'Time in Solution $(min)$')
plt.ylabel(r'Saline Absorbed $(g)$')

# plt.xlim(0.5, 4.75)
plt.xticks([0, 1, 5, 10, 30], ['0', '1', '5', '10', '30'])
plt.ylim(0, 1.25)

plt.grid()

plt.legend(loc='lower right')
plt.savefig('python/output/centrifuge_retention_r3r4.svg', format='svg',dpi=1200,bbox_inches='tight')
plt.show()






