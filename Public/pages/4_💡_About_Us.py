# Packages
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


# Imported
from data import text, colors, get_image, awards, contact


# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['About Us Page']


# Title
st.caption('ABOUT US PAGE')
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">About </span>
        <span style=" font-size:75px ; color:{main_color} ; font-weight:bold; ">Us</span>
    </div>""",
    unsafe_allow_html=True
)
add_vertical_space(2)


# Row 1
col1, col2 = st.columns([0.6,0.4])
with col1:
    with st.container(border=True):
        st.subheader('Mission')
        st.write(section_text['Mission'])
with col2:
    with st.container(border=True):
        st.subheader('Vision')
        st.write(section_text['Vision'])


# Row 2
with st.container(border=True):
    st.subheader('Partners and Sponsors')
    st.write(section_text['Partners and Sponsors'])


# Row 3
with st.container(border=True):
    st.subheader('Awards')
    for award, data in awards.items():
        with st.expander(award):
            st.image(get_image(data['Picture']))
            st.write(data['Description'])


# Row 4
with st.container(border=True):
    st.subheader('History')
    st.image(get_image(section_text['Founder Photo']), width=300)
    st.subheader(section_text['Founder'])
    st.write(section_text['Founding Date'])
    st.write(section_text['History'])
