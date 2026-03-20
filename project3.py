# Project 3: Data Analysis using NumPy, Pandas & Matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("----- NUMPY -----")

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

arr2 = np.arange(1, 10).reshape(3, 3)
print("2D Array:\n", arr2)

print("\n----- PANDAS -----")

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [85, 90, 78, 92, 88],
    "Age": [20, 21, 19, 22, 20]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)
print("\nHead:\n", df.head())
print("\nInfo:")
print(df.info())
print("\nDescribe:\n", df.describe())
print("\nStudents with Marks > 85:\n", df[df["Marks"] > 85])

df["Grade"] = ["B", "A", "C", "A", "B"]
print("\nUpdated DataFrame:\n", df)

print("\n----- MATPLOTLIB -----")

plt.figure()
plt.plot(df["Name"], df["Marks"])
plt.title("Marks Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("/mnt/data/line_chart.png")

plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Marks Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("/mnt/data/bar_chart.png")

plt.figure()
plt.scatter(df["Age"], df["Marks"])
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.savefig("/mnt/data/scatter_plot.png")

plt.figure()
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.savefig("/mnt/data/histogram.png")

print("\nGraphs saved as images.")
