import streamlit as st

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
