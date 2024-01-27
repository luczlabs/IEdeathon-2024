# Packages
import streamlit as st
import pandas as pd
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page


# Imported
from data import logo_imglink, landing_page_impact, text, colors, get_image, donation_methods


# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['Landing Page']


# Functions
def donate_button():
    ss.donate = True


# Initialize
st.set_page_config(page_title='Project Blue', page_icon='💙', layout="centered", initial_sidebar_state="auto", menu_items=None)


# Title
st.image(logo_imglink, width=100)
add_vertical_space(1)
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
add_vertical_space(2)


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
with st.container(border=True):
    add_vertical_space(1)
    row_1 = ['ABSCBN.png', 'GMANews.png', 'CNN.PNG', 'PTV.png', 'DailyGuardian.png']
    row_1_links = [
        'https://web.facebook.com/abscbnNEWS/posts/10159569761440168',
        'https://www.gmanetwork.com/news/lifestyle/hobbiesandactivities/789641/dlsu-student-designs-boat-made-of-plastic-bottles/story/',
        'https://www.youtube.com/watch?v=TIiKjqgRzQU',
        'https://www.youtube.com/watch?v=XSs7Pe4WGUw&feature=youtu.be',
        'https://web.facebook.com/237494442937195/posts/4475275605825703/?d=n&_rdc=1&_rdr'
    ]
    row_2 = ['DLSU.png', 'News5.png', 'Spot.png', 'TheWorldNews.png']
    row_2_links = [
        'https://web.facebook.com/127612997282544/posts/4203833589660444/?d=n&_rdc=1&_rdr',
        'https://web.facebook.com/163550757135020/posts/2559727597517312/?d=n&_rdc=1&_rdr',
        'https://www.spot.ph/newsfeatures/the-latest-news-features/86315/plastic-bottle-boat-made-in-ilocos-sur-a833-20210527',
        'https://theworldnews.net/ph-news/this-plastic-bottle-boat-can-take-four-people-out-to-the-sea'
    ]
    col1, col2, col3, col4, col5 = st.columns(5)
    for ind, col in enumerate([col1, col2, col3, col4, col5]):
        with col:
            st.markdown(f"""<a href="{row_1_links[ind]}">
                <img src="{get_image(f'Landing Page_Feature {row_1[ind]}')}" 
                width="100%" height="100%"></a>""", unsafe_allow_html=True)
    add_vertical_space(2)

    col1, col2, col3, col4 = st.columns(4)
    for ind,col in enumerate([col1, col2, col3, col4]):
        with col:
            st.markdown(f"""<a href="{row_2_links[ind]}">
                <img src="{get_image(f'Landing Page_Feature {row_2[ind]}')}" 
                width="90%" height="90%"></a>""", unsafe_allow_html=True)
    add_vertical_space(2)

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


# Apply
st.caption('APPLY TODAY')
with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        st.write(section_text['apply'])
        apply = st.button('Apply now')
        if apply:
            switch_page('application')
    with col2:
        st.image(get_image('About Us_Awards - ASEAN Youth Eco-Champions.jpg'))
add_vertical_space(2)


# Donate
st.caption('DONATE TODAY')
with st.container(border=True):
    st.write(text['donate_description'])
    donate = st.button('Donate now', type='primary', on_click=donate_button)
if 'donate' not in ss:
    ss.donate = False
if ss.donate:
    def donate():
        with st.container(border=True):
            col1, col2= st.columns([0.4,0.6], gap='medium')
            with col1:
                option = st.radio('Choose your donation method', donation_methods.keys())
                done_donate = st.button('Done donating')
            with col2:
                add_vertical_space(2)
                st.image(get_image(f'Landing Page_Donation {option}{donation_methods[option][2]}'), width=100)
                st.subheader(donation_methods[option][0])
                st.write(donation_methods[option][1])
            if done_donate:
                st.balloons()
                st.write(text['donate_done'])
                st.text_input('Your name')

    donate()

add_vertical_space(2)
        

# Sponsors and partners
st.caption('OUR SPONSORS')
with st.container(border=True):
    st.image(get_image('Landing Page_Partners and Sponsors.png'))
