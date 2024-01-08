# Packages
import streamlit as st
import pandas as pd
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.add_vertical_space import add_vertical_space


# Imported
from data import landing_page_impact, text, images, colors


# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['Landing Page']
section_images = images['Landing Page']


# Functions
def donate_button():
    ss.donate = True

# Initialize
st.set_page_config(page_title='Project Blue', page_icon='💙', layout="centered", initial_sidebar_state="auto", menu_items=None)


# Background
# background_image = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main \u007b
#     background-image: url('{section_images['background_image']}');
#     background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
#     background-position: center;  
#     background-repeat: ;
# \u007d
# </style>
# """

# st.markdown(background_image, unsafe_allow_html=True)


# Title
st.caption('THIS IS PROJECT BLUE')
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:100px ; color:#31333F ; font-weight:bold; ">More than </span>
        <br>
        <span style=" font-size:100px ; color:{main_color} ; font-weight:bold; ">cleanups</span>
        <span style=" font-size:100px ; color:#31333F ; font-weight:bold; ">.</span>
    </div>""",
    unsafe_allow_html=True
)
add_vertical_space(20)


# Information about the organization
st.write(f"{section_text['org_info']}")

col1, col2 = st.columns(2)
with col1:
    with st.expander(label='OUR STORY', expanded=False):
        st.write(section_text['org_background'])
with col2:
    with st.expander(label='OUR SLOGAN'):
        st.markdown(f"**:blue[MORE THAN CLEANUPS.]**\n\n{section_text['slogan_info']}")
    
add_vertical_space(2)

# Impact by numbers
st.caption('IMPACT BY NUMBERS')
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
row1, row2 = [col1, col2, col3], [col4, col5, col6]
for ind, col in enumerate(row1):
    col.metric(label=landing_page_impact[ind][0], value=landing_page_impact[ind][1], delta='Lorem Ipsum')
for ind, col in enumerate(row2):
    col.metric(label=landing_page_impact[ind+3][0], value=landing_page_impact[ind+3][1], delta='Lorem Ipsum')

style_metric_cards(border_left_color=main_color, border_radius_px=7, box_shadow=False)
add_vertical_space(1)


# Features
st.caption('AS FEATURED IN')
# to_be_added
add_vertical_space(2)


# Member benefits
st.caption('MEMBER BENEFITS')
col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.radio('What are you most excited about?', section_text['benefits'].keys(), key='benefit')
with col2:
    for k,v in section_text['benefits'][ss.benefit].items():
        with st.expander(k, expanded=False):
            st.write(v)

add_vertical_space(2)


# Donate
col1, col2 = st.columns(2)
with col1:

    # possibly photo?

    st.caption('DONATE')
    donate = st.button('Donate now', type='primary', on_click=donate_button)
    if 'donate' not in ss:
        ss.donate = False
    if ss.donate:
        with st.container(border=True):
            st.write('test')

            # donate details

with col2:
    st.caption('APPLY')

    # possibly photo

    apply = st.button('Apply now', type='primary')

add_vertical_space(2)


# Sponsors and partners
st.caption('OUR SPONSORS')
# st.image()
