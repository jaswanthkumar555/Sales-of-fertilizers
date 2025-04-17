import pandas as pd
df = pd.read_csv(r"C:\Users\msuse\Downloads\6011_source_data.csv")
print("Column names and data types")
print(df.info())
print("missing values \n",df.isnull().sum())
#Statistics: mean,median, and standard deviationprint("median: ")
print(df['MonthCode'].median())
print(f"Standard deviation: ",df['MonthCode'].std().round(1))

State_unique = df['srcStateName'].unique()
print(f"State_unique: {State_unique}\n")
#shape of no of row and columns
print("shape of the dataset: ",df.shape)
#printing the first 5 rows
print("\nthis are the first 5 rows: ",df.head(5))
#printing the last 5 rows
print("\n those are the last 5 rows",df.tail(5))
#printing max and min values
print("\nmaximum amount: ",df["Sales of fertilizers for state wise in each month"].max())
print("\nminimum amount: ",df["Sales of fertilizers for state wise in each month"].min())

import matplotlib.pyplot as plt
#counts unique values
State_count = df['srcStateName'].value_counts()
print(f"count of unique values: {State_count}")
#bar plot
State_count.plot(kind='bar', title="count of State column",color='orange')
plt.ylabel("count")
plt.show()

#scatter plot YearCode vs Different seasons
plt.scatter(df["YearCode"], df["Different seasons"], color ='blue')
plt.title("yearCode vs Different seasons using scatter plot")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()
#line plot for state
plt.plot(df["srcStateName"].value_counts().head(20),marker='s', linestyle='dotted')
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("line plot for state")
plt.yscale("log")
plt.show()
#histogram plot for state
plt.figure(figsize=(8,6))
df["srcStateName"].value_counts().plot.hist(bins=20, color='red', edgecolor='black')
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Histogram plot for state")
plt.xscale("log")
plt.yscale("log")
plt.show()

#pie chart for Fertilizer sales
plt.figure(figsize=(8,5))
df["Fertilizer sales"].value_counts().plot.pie(colors=['lightgreen', 'orange','blue','brown','black'])
plt.title("pie chart for Fertilizer sales")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.show()

#seaborn for data
import seaborn as sns
import matplotlib.pyplot as plt

#creating lineplot using seaborn
#sample data(select one state)
state_data = df[df["srcStateName"]=="Himachal Pradesh"]
sns.lineplot(data =state_data, marker = "o" )
plt.title("line plot using seaborn")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.xscale("log")
plt.yscale("log")
plt.xticks(rotation = 45)
plt.show()

#bar plot

sns.barplot(df["Fertilizer sales"].value_counts().dropna(), color='blue')
plt.title("fertilize sales availabillity")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.show()

#histogram
plt.figure(figsize=(8,5))
sns.histplot(df["srcStateName"].value_counts().dropna(),bins=30,kde=True, color ="orange")
#kde kernal desity estimation which provides smoother curve
plt.title("state column using histogram")
plt.xlabel("x label")
plt.ylabel("y label")
plt.xscale("log")
plt.yscale("log")
plt.xticks(rotation=50)
plt.show()


#heatmap
matrix = df.select_dtypes(include=['number']).corr()

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Heatmap of Temperature Values")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.xticks(rotation = 30)
plt.show()

#scatterplot (seaborn)
plt.figure(figsize=(8,6))
sns.scatterplot(y=df["Availability of fertilizers for state wise in each month"], x=df["YearCode"], alpha=0.6,legend=True)
plt.title("state vs years")
plt.xlabel("years")
plt.ylabel("state names")
plt.xscale("log")
plt.yscale("log")
plt.show()

#boxplot (seaborn)
plt.figure(figsize=(8, 6))
sns.boxplot(x="Availability of fertilizers for state wise in each month", y="Fertilizer sales", hue = "Fertilizer sales", data=df)
plt.title(" Availability of fertilizers for state wise in each month(Box Plot) vs sales")
plt.xlabel("x label")
plt.ylabel("Fertilizer sales")
plt.xticks(rotation = 30)
plt.xscale("log")
plt.yscale("log")
plt.show()



