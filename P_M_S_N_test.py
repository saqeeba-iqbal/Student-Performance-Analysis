import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
  #LOAD DATASET
df=pd.read_csv("archive/StudentsPerformance.csv")
  #EXPLORE DATA
print(df.head()) #shows first 5 rows 
print(df.columns)       # pandas → lists column names
print(df.info())        # pandas → shows data types, nulls, and memory usage
print(df.describe())    # pandas → shows summary statistics (mean, std, min, max)
  #AVERAGE SCORE BY GENDER
gender_scores=df.groupby("gender")[["reading score","writing score"]].mean()
print(gender_scores)
gender_scores.plot(kind="bar",title="Average score by gender",figsize=(8,5))
plt.ylabel("Average score")
plt.grid(True)
plt.show()
   #correlation between reading and writing
correlation=df["reading score"].corr(df["writing score"])
print("correlation",correlation)
plt.scatter(df["reading score"],df["writing score"],alpha=0.5)
plt.title("Reading vs writing")
plt.xlabel("reading score")
plt.ylabel("writing score")
plt.grid(True)
plt.show()
   #PLOT SCORE DISTRIBUION
sns.histplot(df["math score"],kde=True,color="skyblue")
plt.title("Distribution of math scores")
plt.ylabel("math scores")
plt.grid(True)
plt.show()
  #HIGH PERFORMANCE AND LOW PERFORMANCE
df["average"]=df[["reading score","writing score","math score"]].mean(axis=1)
high=df[df["average"]>=90]
print("high performer:",high)
low=df[df["average"]<=50]
print("low performer:",low)