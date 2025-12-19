import pandas as pd
import pytest
from app.dataprocess import getdata, cleandata

@pytest.fixture()
def countryname():
    return "Australia"

@pytest.fixture()
def dataloc():
    return "./data/AQI.csv"

@pytest.fixture()
def loaddata():
    df = pd.read_csv("./data/AQI.csv")
    return df

def test_getdata(dataloc):
    filepath = dataloc
    df = getdata(filepath)
    assert type(df) == pd.core.frame.DataFrame

def test_cleandata(loaddata):
    data_cleaned = cleandata(loaddata)
    data_cols = data_cleaned.columns
    check_year_col = "Year" in data_cols
    check_month_col = "Month" in data_cols
    dateformat_ = pd._libs.tslibs.timestamps.Timestamp
    assert type(data_cleaned["Date"].iloc[0]) == dateformat_
    assert check_year_col == True
    assert check_month_col == True