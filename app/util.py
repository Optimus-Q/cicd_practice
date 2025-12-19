import pandas as pd
import calendar
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


# heatmap
def getheatmapdata(data):
    col_months = [calendar.month_name[x] for x in range(1, 13)] 
    col_years = [2022, 2023, 2024, 2025]
    aqi_avg = []
    for cy in col_years:
        aqi_sub_yr = []
        for cm in col_months:
            month_df = data[(data["Year"]==cy) & (data["Month"]==cm)]
            if len(month_df)==0:
                aqi_sub_yr.append(0)
            else:
                aqi_sub_yr.append(month_df["AQI Value"].mean())
        aqi_avg.append(aqi_sub_yr)
    df_heatmap = pd.DataFrame(index=col_years,
                              data=aqi_avg,
                              columns=col_months)
    return df_heatmap

# get heatmap plot
def getheatmap(data):
    colors = [(1, 1, 1),(0, 1, 0), (1, 0, 0)] # w, g, r
    n_bins = 100
    cmap_name = "green_red"
    cm = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.heatmap(data, cmap=cm, annot=True, fmt=".2f", linewidths=.5, ax=ax)
    return fig

# get trend plot
def gettrendmap(data):
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.barplot(data=data, x="AQI", y="Year", orient="h", legend=True)
    plt.title("AQI Trend")
    return fig

# data analysis function
def getanalytics(name, data):
    data_chunk = data[data["Country"]==name].sort_values(by="Date", ascending=True)
    data_trend = data_chunk.groupby(["Year"]).agg(AQI=("AQI Value", "mean"))
    data_chunk = data_chunk[["Year", "Month", "AQI Value"]].sort_values(by="Year", ascending=True)
    data_heatmap = getheatmapdata(data_chunk)
    heatmap_plot_obj = getheatmap(data_heatmap)
    trend_plot_obj = gettrendmap(data_trend)
    return heatmap_plot_obj, trend_plot_obj