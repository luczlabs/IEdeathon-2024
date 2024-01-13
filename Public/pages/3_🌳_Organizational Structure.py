# Packages
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


# Imported
from data import text, colors, get_image, organization_structure


# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['Organizational Structure Page']


# 2 rows of all committees clickable images, go to header anchor 
st.header("Section 1")
st.markdown("[Section 1](#section-1)", unsafe_allow_html=True)