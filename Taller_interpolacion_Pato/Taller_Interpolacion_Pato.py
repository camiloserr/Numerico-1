from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

#Taller ralizado por Camilo Serrano y Daniel Mendoza

# Pico-Cola
xiA = [190,230,290,360,400,540,570,600,800,900,1150,1230,1360,1430]

fiA = [730,750,785,860,870,815,805,810,830,825,740,690,650,625]

# Pico-Ala
xiB = [181.7,202.2,283.4,326.4,396.2,520.2,549.9,652.7]

fiB = [718,702.3,708.5,719.2,711.5,710,683,610.6]

# Ala-PuntaAla
xiC = [565.9,586.5,638.7,647.8,652.7]

fiC = [83.9,125.9,403,501.9,610.6]
# PuntaAla-Ala

xiD = [565.9,656,760.6,830.5,898.3,914.1]

fiD = [83.9,83.9,171.4,278.7,434.5,486.2]

# Ala-Cola
xiE = [914.1,947.3,983.2,1033.7,1088.7,1157.2,1199.5,1250.1,1292.3,1336.4,1376.3,1430]

fiE = [486.2,556.6,548.6,550.6,561.8,599.5,591,591.5,597,609.3,612,625]

f1 = interpolate.interp1d(xiA, fiA , kind='quadratic')
xnew1 = np.arange(min(xiA), max(xiA), 0.01)

f2 = interpolate.interp1d(xiB, fiB , kind='quadratic')
xnew2 = np.arange(min(xiB), max(xiB), 0.01)


f3 = interpolate.interp1d(xiC, fiC , kind='quadratic')
xnew3 = np.arange(min(xiC), max(xiC), 0.01)


f4 = interpolate.interp1d(xiD, fiD , kind='quadratic')
xnew4 = np.arange(min(xiD), max(xiD), 0.01)


f5 = interpolate.interp1d(xiE, fiE , kind='quadratic')
xnew5 = np.arange(min(xiE), max(xiE), 0.01)



axes = plt.gca()
axes.set_xlim([100,1500])
axes.set_ylim([50,1000])

plt.plot(xiA, fiA, '.', xnew1, f1(xnew1), '-',
xiB, fiB, '.', xnew2, f2(xnew2), '-',
xiC, fiC, '.', xnew3, f3(xnew3), '-',
xiD, fiD, '.', xnew4, f4(xnew4), '-',
xiE, fiE, '.', xnew5, f5(xnew5), '-')
plt.show()
