import numpy as np
import matplotlib.pyplot as plt
sf_high_temp = np.array([55, 52, 53, 46, 52, 51, 55, 55, 52, 55, 57, 55, 55, 43, 42,
39, 34, 39, 39, 39, 45, 52, 35, 36, 45, 30, 30, 34, 37, 21, 25])
sf_low_temp = np.array([23, 28, 28, 36, 33, 32, 32, 30, 32, 28, 30, 32, 30, 25,
23, 25, 26, 19, 21, 21, 32, 28, 18, 14, 25, 10, 3, 12, 9, 10, 8])
day = 1.0 + np.arange(len(sf_high_temp))
plt.plot(day, sf_high_temp, 'bo-', label='high')
plt.plot(day, sf_low_temp,'r^-',label='low')
plt.xlim(1,31)
(1.0, 31.0)
plt. legend()
plt.xlabel('day in December 2014')
plt.ylabel('temperature in F')
plt.title('Daily High/Low Temps in City for December 2014')
plt.grid()
plt.fill_between(day,sf_high_temp, color='m', alpha=0.3)
plt.fill_between(day,sf_low_temp, color='w')
plt.show()
