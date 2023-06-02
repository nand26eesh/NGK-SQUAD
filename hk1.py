import pandas as pd
import seaborn as snb
import matplotlib.pyplot as plt
import numpy as np
import io
import seaborn as sb


df=pd.read_csv("hackathon1.csv")


a=pd.unique(df['Product Name'])
print (a)
len(a)
c=np.array(a)

n=[]
g=[]
k=[]
k1=[]
for i in c:
  df1=df[df['Product Name']== i]
  n.append(df1["Profit%"].mean())
  g.append(df1["Supplied"].mean())
  k.append(df1["Customer Demand"].mean())
  k1.append(i)
df2=pd.DataFrame({'profit%':n,'supply':g,'customer':k,'Key':k1},index=c)
row1=df2.iloc[1:10]
row1
i=0
j=10
while j<=len(c):
    row1=df2.iloc[i:j]
    ax=row1.plot(x="Key", y=["profit%", "supply","customer"], kind="bar")
    for container in ax.containers:
      ax.bar_label(container)
    i+=10
    j+=10
row1=df2.iloc[i:len(df2.index)]
ax=row1.plot(x="Key", y=["profit%", "supply","customer"], kind="bar")
for container in ax.containers:
    ax.bar_label(container)




