import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    res = linregress(x,y)
    xx = pd.Series([i for i in range(1880,2051)])
    plt.plot(xx, res.intercept + res.slope*xx, 'red')
    
    # Create second line of best fit
    new_df = df.loc[ df['Year']>=2000 ]
    new_x = new_df['Year']
    new_y = new_df["CSIRO Adjusted Sea Level"]
    res2 = linregress(new_x,new_y)
    xx2 = pd.Series([i for i in range(2000,2051)])
    plt.plot(xx2, res2.intercept + res2.slope*xx2, 'green')
  
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
