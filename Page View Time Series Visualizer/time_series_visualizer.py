import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
# Register pandas formatters and converters with matplotlib.

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=['date'],index_col='date')

# Clean data
df = df[
(df["value"] >= df["value"].quantile(0.025)) &
(df["value"] <= df["value"].quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20,8))
    ax = plt.plot(df.index ,df['value'],'r')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(['year','month'])['value'].mean()
    df_bar = df_bar.unstack()
    # Draw bar plot
    fig = df_bar.plot.bar(legend=True,figsize=(12,12),ylabel="Average Page Views",xlabel="Years").figure
    plt.legend(['January','February','March','April','May','June','July','August','September','October','November','December'])
  
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box ["month_num"] = df_box ["date"].dt.month
    df_box = df_box.sort_values("month_num")

    fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20,10))
    ax1 = plt.subplot(1,2,1)
    ax1 = plt.title("Year-wise Box Plot (Trend)")
    ax1 = sns.boxplot(x=df_box["year"],y=df_box["value"])
    ax1 = plt.xlabel("Year")
    ax1 = plt.ylabel("Page Views")

    ax2 = plt.subplot(1,2,2)
    ax2 = plt.title("Month-wise Box Plot (Seasonality)")
    ax2 = sns.boxplot(x=df_box["month"],y=df_box["value"])
    ax2 = plt.xlabel("Month")
    ax2 = plt.ylabel("Page Views")
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
