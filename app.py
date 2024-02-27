import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import datetime as datetime
import glob
import altair as alt
from datetime import datetime, time

st.set_page_config(layout="wide")

st.sidebar.header("About")
st.sidebar.markdown("The Uber data analysis created with streamlit allows to visualize in an interactive way")
st.sidebar.markdown("""
                    Details of the dataset:
                    The dataset contains information about the Datetime, Latitude, Longitude and Base of each uber ride that happened in the month of July 2014 at New York City, USA
                    
                    - Date/Time : The date and time of the Uber pickup
                    - Lat : The latitude of the Uber pickup
                    - Lon : The longitude of the Uber pickup
                    - Base : The TLC base company code affiliated with the Uber pickup

                    The Base codes are for the following Uber bases:
                    
                    - B02512 : Unter
                    - B02598 : Hinter
                    - B02617 : Weiter
                    - B02682 : Schmecken
                    - B02764 : Danach-NY
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
@st.cache_data
def load_df():
    df_paths = [name for name in glob.glob('Sources/*')]
    lst = []
    for df in df_paths:
        data = pd.read_csv(df)
        lst.append(data)
    return pd.concat(lst)


#Title
st.title('Data analysis: Uber Rides from :')
st.write('Welcome to an interactive analysis for an Uber dataset :sunglasses:')


#Slider
st.header('Slider')

st.subheader('Slider with value')
slider_value = st.slider('Select a value',0,100,20,10)
st.write(f'You has selected {slider_value}')

# Slider for time
st.subheader("Slider for time")
apointment = st.slider('Select your appointment', value=(time(11,30),time(12,45)))
st.write(f"You're scheduled for:{apointment}")

# Slider for datetime
st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="DD/MM/YY - hh:mm")
st.write("Start time:", start_time)

# Slider with range
st.subheader("Slider with range")
values = st.slider('Select a range of values', 0.0, 100.0,(25.0,75.0))
st.write(f'You have chosen this values:{values}')


#Checkbox
st.header('Checkbox')

checbox_value = st.checkbox('Check me')
if checbox_value:
    st.write('Checkbox cheked')
else:
    st.write('Checkbox not cheked')

#Interactive input   
st.header('Interactive text input')

user_text = st.text_input('Enter text:')
if user_text:
    st.write(f'(You has entered: {user_text})')

#Dataframe from Folder
st.header("Altair circle")

df = load_df()
st.write(df.head())

# Altair graph
@st.cache_data
def altair_df():
    df2 = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])
    return(alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']))
st.write(altair_df())

#Line graph
st.header("Line graph")
@st.cache_data
def chart_data():
    data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c']
    )
    return data
st.line_chart(chart_data())

#Select box
st.header('Select box')
option = st.selectbox('What is your favorite color?', ('Blue','Red','Green'))
st.write(f'Your favorite color is: {option}')

#Multiselect
st.header('Multiselect')
selections = st.multiselect('Cheose some options: ',['a','b','c','d','e'])
st.write(f'You have chosen: {selections}')