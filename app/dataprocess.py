import pandas as pd
import calendar


def getdata(filepath):
    df = pd.read_csv(filepath)
    return df

def cleandata(data):
    data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
    data["Year"] = data["Date"].dt.year
    data["Month"] = [calendar.month_name[x] for x in data["Date"].dt.month]
    return data
