#Plotting the 1D:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("heart.csv")
dff = df[0:25]
df_Age = dff['age'].value_counts()
plt.pie(df_Age.values,labels=df_Age.index)
plt.title("Number of memebers based on their Age")
plt.show()
#Plotting the 2D:
df1 = df.iloc[25:,1]
df2 = df.iloc[25:,2]
day = 1.0+ np.arange(len(df2))
plt.plot(day,df2 ,'bo-',label = 'high')
plt.plot (day ,df1,' ' ,label = 'low')
plt.xlim (1,31)
plt.legend()
plt.grid()
plt.fill_between(day,df2,color = 'g',alpha = 0.3)
plt.fill_between (day,df1,color = 'b')
plt.show()
#Plotting the 3D:
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt. figure()
ax = fig.add_subplot(111, projection='3d')
xs = df.iloc[:,0]
ys = df.iloc[:,1]
zs = df.iloc[:,2]
xt =df.iloc[:,3]
yt =df.iloc[:,4]
zt =df.iloc[:,5]
ax.scatter(xs, ys, zs, c='g', marker='o')
ax.scatter(xt, yt, zt, c='r', marker='^')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_label('z Label')
plt.show()
