import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def process_file():
    data = pd.read_csv("data.csv")
    X = data.iloc[:, 0]
    Y = data.iloc[:, 1]
    plt.scatter(X, Y)
    plt.show()
    plt.close()

process_file()