#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Script to analyze CMIP6 sources csv.

INPUT:
Readin data from cmip6-sources_13_01_2025.csv

OUTPUT:
Bar chart plots of downloads by sources

Author: Robert Junod
Updated: 02/27/2024
"""

# =============================================================================
#                                 IMPORT MODULES
# =============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =============================================================================
#                                 FUNCTIONS
# =============================================================================
def read_in(file):
    ''' Function to read and process data '''
    # Read in file
    df = pd.read_csv(file)
    
    # Add total by TB column
    df['total_size_TB'] = df.loc[:,'total_size_GB'] / 1024.
    df = df.loc[df['total_size_TB'] >= 1]
    # Add downloads by TB column
    df['downloads_per_tb'] = (df.loc[:,'number_of_downloads']
                               / df.loc[:,'total_size_TB'])
    
    df.sort_values('downloads_per_tb',ascending=False)

    # Subset to only include data with over 5000 downloads
    df = df.loc[df['number_of_downloads'] > 5000]
    return df


def plot_bar(df):
    ''' Function to plot bar charts'''
    try:
        # First bin the data 
        bins = np.linspace(0, df['total_size_TB'].max(), num=6)  # 6 bins
        df['size_bin'] = pd.cut(
            df['total_size_TB'],
            bins=bins,
            labels=[
                f"{int(b.left)}-{int(b.right)}TB"
                for b in pd.interval_range(start=0, end=bins[-1], freq=bins[1])])
        df_sorted = df.sort_values('number_of_downloads')
        
        # Plot Bar Chart of Downloads by Model and Size Bin
        grouped_model = df_sorted.groupby(
            ['source_id_name',
             'size_bin'])['number_of_downloads'].sum().unstack(fill_value=0)
        grouped_model['total'] = grouped_model.sum(axis=1)
        grouped_model = grouped_model.sort_values(
            by='total', ascending=False).drop(columns=['total'])

        fig, ax = plt.subplots()
        grouped_model.iloc[0:20].plot(
            kind='bar', stacked=True, figsize=(12, 6), colormap='viridis',
            xlabel="Climate Model",
            ylabel="Total Downloads (millions)",
            title="Bar Chart of Downloads by Model and Size Bin",
            ax=ax,
            )
        xlabels = ax.get_xticklabels()
        yticks = ax.get_yticks()
        ax.set_yticks(yticks)
        ax.set_yticklabels([f"{tick * 1e-6:.0f}M" for tick in yticks])
        ax.set_xticklabels(xlabels,rotation=30, ha='right')
        ax.legend(title="Total Size (TB)", loc='upper right')
        plt.savefig('barchart_model_size.png')

        # Plot Bar Chart of Downloads per TB by Model and Size Bin
        grouped_per_TB = df_sorted.groupby(
            ['source_id_name',
             'size_bin'])['downloads_per_tb'].sum().unstack(fill_value=0)
        grouped_per_TB['total'] = grouped_per_TB.sum(axis=1)
        grouped_per_TB = grouped_per_TB.sort_values(
            by='total', ascending=False).drop(columns=['total'])

        fig, ax = plt.subplots()
        grouped_per_TB.iloc[0:20].plot(
            kind='bar', stacked=True, figsize=(12, 6), colormap='viridis',
            xlabel="Climate Model",
            ylabel="Downloads per TB",
            title="Bar Chart of Downloads per TB by Model and Size Bin",
            ax=ax,
            )
        xlabels = ax.get_xticklabels()
        ax.set_xticklabels(xlabels,rotation=30, ha='right')
        ax.legend(title="Total Size (TB)", loc='upper right')
        plt.savefig('barchart_model_per_TB.png')

        return 'SUCCESS'
    except:
        return 'FAIL'


# =============================================================================
#                                 MAIN
# =============================================================================

if __name__ == "__main__":

    # Point to file location
    FILE_IN = 'cmip6-sources_13_01_2025.csv'

    # Readin Data
    DF = read_in(FILE_IN)

    #Plot Data
    print(plot_bar(DF))