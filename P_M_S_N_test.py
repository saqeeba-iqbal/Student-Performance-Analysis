# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
#     #LOAD DATASET
# df=pd.read_csv("archive/StudentsPerformance.csv")
# print(df)
#     #EXPLORE THE DATA
# print(df.head())
# print(df.columns)
# print(df.info())
# print(df.describe()) 
#     #COMPARE AVERAGE SCORE BY GENDER 
# gender_scores=df.groupby("gender")[["math score","reading score","writing score"]].mean()
# print(gender_scores)
# gender_scores.plot(kind="bar",title="Average score by Gender",figsize=(8,5))
# plt.ylabel("Average score")
# plt.grid(True)
# plt.show()
#    #CORRELATION BETTWEEN READING AND WRITTING
# correlation=df["reading score"].corr(df["writing score"])
# print("correaltion",correlation)
# plt.scatter(df["reading score"],df["writing score"],alpha=0.5)
# plt.xlabel("reading score")
# plt.ylabel("writing score")
# plt.grid(True)
# plt.show()
#    #PLOT SCORE DISTRIBUION
# sns.histplot(df["math score"],kde=True,color="skyblue")
# plt.title("Distribuion of matth score")
# plt.xlabel("math score")
# plt.grid(True)
# plt.show()
#    #Identifying high and low performing
# df["average"]=df[["math score","reading score","writing score"]].mean(axis=1)
# high=df[df["average"]>=90]
# print("high performers:",high)
# low=df[df["average"]<=50]
# print("low performers:",low)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
  #LOAD DATASET
df=pd.read_csv("archive/StudentsPerformance.csv")
  #EXPLORE DATA
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())
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