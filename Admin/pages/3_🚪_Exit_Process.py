# Packages
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


# Imported
from data import colors, get_image, text


# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['Exit Process Page']


# Title
st.caption('EXIT PROCESS PAGE')
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">Exit </span>
        <span style=" font-size:75px ; color:{main_color} ; font-weight:bold; ">Process</span>
    </div>""",
    unsafe_allow_html=True
)
add_vertical_space(2)


# Content
name = 'Val Allen'
st.subheader(f'Hello {name},')
st.write(section_text['Intro'])

for step, data in section_text['Steps'].items():
    with st.container(border=True):
        st.write(f'**{step}**')
        st.write(data['Instruction'])
        if data['URL']:
            st.link_button('Access link here', data['URL'])

st.write(section_text['Outro'])