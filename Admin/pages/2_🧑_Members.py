# Packages
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# Imported
from data import text, colors, get_image, organization_structure

# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['Membership Status']

# Functions
def status_button():
    ss.status = True

# Title
st.caption('MEMBERSHIP STATUS PAGE')
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">Ahoy, </span>
        <span style=" font-size:75px ; color:{main_color} ; font-weight:bold; ">Val Allen </span>
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">!🌊</span>
    </div>""",
    unsafe_allow_html=True
)
add_vertical_space(2)


