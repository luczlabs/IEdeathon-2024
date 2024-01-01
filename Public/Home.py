import streamlit as st
import pandas as pd

st.title('Landing Page')

# Information about the organization
st.header('Information')

# Member benefits
st.header('What\'s in it for you?')

# Call to action
donate = st.button('Donate now', type='primary')
apply = st.button('Apply now', type='primary')

# Sponsors and partners
st.header('Our Sponsors')
# st.image()
