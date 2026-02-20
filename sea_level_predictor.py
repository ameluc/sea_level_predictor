"""
 ===============================================================
 sea_level_predictor.py
 ===============================================================

 This module file is meant to help us visualise, compute
 & predict based on available data.

 Author : Améluc Ahognidjè <ameluc.ahognidje@protonmail.com>
 Date : 2026-02-20
 Version : 1.0.0
"""

import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd
from scipy.stats import linregress
# import seaborn as sns

PATH = "./epa-sea-level.csv"

def draw_plot():
    """
     This function draws the visualisation
     to help us predict the data.

     Returns
     -------
         A visualisation figure
    """

    df = pd.read_csv(PATH)
    df["Year"] = df["Year"].astype("int16")
    df_new_trend = df[df["Year"] >= 2000]
    year_range_old = pd.Series(range(1880, 2051))
    year_range_new = pd.Series(range(2000, 2051))
    result_old_trend = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )
    result_new_trend = linregress(
        df_new_trend["Year"],
        df_new_trend["CSIRO Adjusted Sea Level"]
    )
    old_trend = result_old_trend.intercept + result_old_trend.slope * year_range_old
    new_trend = result_new_trend.intercept + result_new_trend.slope * year_range_new

    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.plot(year_range_old, old_trend)
    plt.plot(year_range_new, new_trend)
    plt.savefig("sea_level_plot.png")

    return plt.gca()

# def draw_plot():
#     """
#      This function draws the visualisation
#      to help us predict the data.

#      Returns
#      -------
#          A visualisation figure
#     """

#     df = pd.read_csv(PATH)
#     df["Year"] = df["Year"].astype("int16")
#     df_new_only = df[df["Year"] >= 2000]
#     large_years = np.arange(1880, 2051)
#     new_years = np.arange(2000, 2051)
#     res_old_trend = linregress(
#         df["Year"],
#         df["CSIRO Adjusted Sea Level"]
#     )
#     res_new_trend = linregress(
#         df_new_only["Year"],
#         df_new_only["CSIRO Adjusted Sea Level"]
#     )
#     old_trend = res_old_trend.intercept + res_old_trend.slope * large_years
#     new_trend = res_new_trend.intercept + res_new_trend.slope * new_years

#     fig, ax = plt.subplots(figsize=(12, 6))

#     ax.spines["top"].set_linewidth(0.2)
#     ax.spines["bottom"].set_linewidth(0.5)
#     ax.spines["left"].set_linewidth(0.5)
#     ax.spines["right"].set_linewidth(0.2)
#     ax.set_title("Rise in Sea Level")
#     ax.set_xlabel("Year")
#     ax.set_ylabel("Sea Level (inches)")
#     sns.scatterplot(
#         df,
#         x="Year",
#         y="CSIRO Adjusted Sea Level"
#     )
#     sns.lineplot(
#         x=large_years,
#         y=old_trend,
#         color="#ff0000",
#         linewidth=0.5
#     )
#     sns.lineplot(
#         x=new_years,
#         y=new_trend,
#         color="#00ff00",
#         linewidth=0.5
#     )
#     fig.savefig("sea_level_plot.png")

#     return fig
