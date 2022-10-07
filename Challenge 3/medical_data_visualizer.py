import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column

df['overweight'] = df['weight'] / ((df['height']/100)**2)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['overweight'] = df['overweight'].apply(lambda x: 1 if x>25 else 0)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x==1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x==1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df1 = df[["cardio", "active", "alco", "cholesterol", "gluc", "overweight", "smoke"]]
    df_cat = pd.melt(df1, id_vars='cardio')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x="variable", col="cardio", hue="value", data=df_cat, kind="count").set_axis_labels("variable", "total").fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    #data cleaning - diastolic pressure is higher than systolic
    """
    df_heat = df
    df_heat = df_heat.drop(df_heat[(df_heat['ap_lo'] > df_heat['ap_hi'])].index)
    
    #data cleaning - height is less than the 2.5th percentile 
    df_heat = df_heat.drop(df_heat[df_heat['height'] < df_heat['height'].quantile(0.025)].index)
    
    #data cleaning - height is more than the 97.5th percentile 
    df_heat = df_heat.drop(df_heat[df_heat['height'] > df_heat['height'].quantile(0.975)].index)  
    
    #data cleaning - weight is less than the 2.5th percentile
    df_heat = df_heat.drop(df_heat[df_heat['weight'] < df_heat['weight'].quantile(0.025)].index)
    
    #data cleaning - weight is more than the 97.5th percentile
    df_heat = df_heat.drop(df_heat[df_heat['weight'] > df_heat['weight'].quantile(0.975)].index)
    #end"""
    df_heat = df[
               (df['ap_lo'] <= df['ap_hi'] ) &
               (df['height'] >= df['height'].quantile(0.025) ) &
               (df['height'] <= df['height'].quantile(0.975) ) &
               (df['weight'] >= df['weight'].quantile(0.025) ) &
               (df['weight'] <= df['weight'].quantile(0.975) )
               ]

    # Calculate the correlation matrix
    df_heat = df_heat[['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']]

    corr = df_heat.corr(method='pearson')
    #corr = corr.round(1)
  
    # Generate a mask for the upper triangle
    mask = np.triu(corr)
    #mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    #fig, ax = None
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, square=True, annot=True, fmt="0.1f", vmax=.32, cmap='gnuplot2', linewidths=1)
  
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
