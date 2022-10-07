import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    df_line = df.copy()
    df_line.set_index('date', inplace=True)
    fig, ax = plt.subplots(figsize=(25, 15))
    plt.plot(df_line, color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(["2016-07-01","2017-01-01","2017-07-01","2018-01-01","2018-07-01","2019-01-01", "2019-07-01", "2020-01-01"], labels=["2016-07","2017-01","2017-07","2018-01","2018-07","2019-01", "2019-07", "2020-01"])

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
    


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar["date"] = pd.to_datetime(df_bar["date"])
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month
    df_bar.drop(['date'], axis=1, inplace=True)
    add = pd.DataFrame({'value':[0,0,0,0],
                        'year' :[2016,2016,2016,2016],
                        'month':[1,2,3,4]
                      })
    df_bar = df_bar.append(add,ignore_index=True)

    n_by_state = df_bar.groupby(["year","month"])['value'].mean()
    n_by_state= pd.DataFrame(n_by_state)
    #n_by_state.loc[2016]['value']
    # Draw bar plot
    jan = list(n_by_state.loc[(2016,1):(2019,12):12]['value'])
    feb = list(n_by_state.loc[(2016,2):(2019,12):12]['value'])
    mar = list(n_by_state.loc[(2016,3):(2019,12):12]['value'])
    apr = list(n_by_state.loc[(2016,4):(2019,12):12]['value'])
    may = list(n_by_state.loc[(2016,5):(2019,12):12]['value'])
    jun = list(n_by_state.loc[(2016,6):(2019,12):12]['value'])
    jul = list(n_by_state.loc[(2016,7):(2019,12):12]['value'])
    aug = list(n_by_state.loc[(2016,8):(2019,12):12]['value'])
    sep = list(n_by_state.loc[(2016,9):(2019,12):12]['value'])
    oct = list(n_by_state.loc[(2016,10):(2019,12):12]['value'])
    nov = list(n_by_state.loc[(2016,11):(2019,12):12]['value'])
    dec = list(n_by_state.loc[(2016,12):(2019,12):12]['value'])
    years = ['2016', '2017', '2018', '2019']
    xpos = np.arange(len(years))
    barWidth = 0.05
    fig, ax = plt.subplots(figsize=(23, 19))
    def bar(name, i, m):
      plt.bar(xpos+i, name, width=barWidth, label=m)  
    bar(jan, 0*barWidth, 'January')
    bar(feb, 1*barWidth, 'February')
    bar(mar, 2*barWidth, 'March')
    bar(apr, 3*barWidth, 'April')
    bar(may, 4*barWidth, 'May')
    bar(jun, 5*barWidth, 'June')
    bar(jul, 6*barWidth, 'July')
    bar(aug, 7*barWidth, 'August')
    bar(sep, 8*barWidth, 'September')
    bar(oct, 9*barWidth, 'October')
    bar(nov, 10*barWidth, 'November')
    bar(dec, 11*barWidth, 'December')
    plt.xticks(xpos+0.275, years, rotation=90, fontsize=30)
    plt.yticks(fontsize=30)
    plt.tick_params(length=7)
    plt.xlabel('Years', fontsize=30)
    plt.ylabel('Average Page Views', fontsize=30)
    plt.legend(title='Months', fontsize=30, title_fontsize=30)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    """df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]"""
  
    df_box["date"] = pd.to_datetime(df_box["date"])
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.month
    df_box.drop(['date'], axis=1, inplace=True)
    add = pd.DataFrame({'value':[0,0,0,0],
                        'year' :[2016,2016,2016,2016],
                        'month':[1,2,3,4]
                      })
    df_box = df_box.append(add,ignore_index=True)
  
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(figsize=(20, 10))
    plt.subplot(1,2,1)
    box1 = sns.boxplot(x=df_box.year, y=df_box.value)
    box1.set(xlabel ="Year", ylabel = "Page Views", title ='Year-wise Box Plot (Trend)', yticks=[0, 20000,40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000])
    plt.subplot(1,2,2)
    box2 = sns.boxplot(x=df_box.month, y=df_box.value)
    box2.set(xlabel ="Month", ylabel = "Page Views", title ='Month-wise Box Plot (Seasonality)', yticks=[0, 20000,40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000])
    box2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
