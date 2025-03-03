import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing data from a CSV file
myData = pd.read_csv('./Data/data.csv')
print(myData.tail())
print(myData.head())