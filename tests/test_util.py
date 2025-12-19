import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import pytest
from app.dataprocess import cleandata
from app.util import getanalytics
import matplotlib.figure as mpl_fig

@pytest.fixture()
def countryname():
    return "Australia"

@pytest.fixture()
def loaddata():
    dataloc = "./data/AQI.csv"
    df = pd.read_csv("./data/AQI.csv")
    df = cleandata(df)
    return df

def test_getanalytics(countryname, loaddata):
    heatmap_obj, trend_obj = getanalytics(countryname, loaddata)
    assert isinstance(heatmap_obj, mpl_fig.Figure)
    assert isinstance(trend_obj, mpl_fig.Figure)