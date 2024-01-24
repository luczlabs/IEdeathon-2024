# Packages
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


# Imported
from data import text, colors, get_image


# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['Project Evaluation Report Page']


# Title
st.caption('EXIT PROCESS PAGE')
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">Project </span>
        <span style=" font-size:75px ; color:{main_color} ; font-weight:bold; ">Evaluation Report</span>
    </div>""",
    unsafe_allow_html=True
)
add_vertical_space(2)


# Content
st.write(section_text['Message'])