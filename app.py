import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import datetime as datetime

st.set_page_config(layout="wide")

st.sidebar.header("About")
st.sidebar.markdown("The Uber data analysis created with streamlit allows to visualize in an interactive way")
st.sidebar.markdown("""
                    Details of the dataset:
                    The dataset contains information about the Datetime, Latitude, Longitude and Base of each uber ride that happened in the month of July 2014 at New York City, USA
                    Date/Time : The date and time of the Uber pickup
                    Lat : The latitude of the Uber pickup
                    Lon : The longitude of the Uber pickup
                    Base : The TLC base company code affiliated with the Uber pickup

                    The Base codes are for the following Uber bases:
                    B02512 : Unter
                    B02598 : Hinter
                    B02617 : Weiter
                    B02682 : Schmecken
                    B02764 : Danach-NY
                    """)

st.sidebar.header("Resources")
st.sidebar.markdown(
    """
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Geopy](https://geopy.readthedocs.io/en/stable/)
- [Folium](https://python-visualization.github.io/folium/latest/)

"""
)


#Define functions

#load data

def load_data():
    df_apr = pd.read_csv('uber-raw-data-apr14.csv')
    df_may = pd.read_csv('uber-raw-data-may14.csv')
    df_jun = pd.read_csv('uber-raw-data-jun14.csv')
    df_jul = pd.read_csv('uber-raw-data-jul14.csv')
    df_aug = pd.read_csv('uber-raw-data-aug14.csv')
    df_sep = pd.read_csv('uber-raw-data-sep14.csv')



st.title('Data analysis: Uber Rides from :')
st.write('Welcome to an interactive analysis for an Uber dataset')

st.header(body='Slider')

slider_value = st.slider('Select a value',0,100,20,10)
st.write(f'You has selected {slider_value}')

st.header('Checkbox')

checbox_value = st.checkbox('Check me')
if checbox_value:
    st.write('Checkbox cheked')
else:
    st.write('Checkbox not cheked')
    
st.header('Interactive text input')

user_text = st.text_input('Enter text:')
if user_text:
    st.write(f'(You has entered: {user_text})')

