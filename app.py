import streamlit as st


st.set_page_config(layout="wide")

st.sidebar.header("About")
st.sidebar.markdown("The Uber data analysis created with streamlit allows to visualize in an interactive way")
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
