import streamlit as st
import pandas as pd
import numpy as np
from dataprocess import *
from util import *

# load data
aqi_df = getdata("./data/AQI.csv")
aqi_df = cleandata(aqi_df)

# list all countries from df
countries_list = aqi_df["Country"].unique().tolist()

# dropdown menu
countries_dropdown = st.selectbox("Select the country name", countries_list)

# streamlit - ui
st.title("AQI Status")
st.write(f"Selected country is: {countries_dropdown}")

# analytics
plot_heatmap, plot_trend = getanalytics(countries_dropdown, aqi_df)
st.pyplot(plot_heatmap)
st.pyplot(plot_trend)
