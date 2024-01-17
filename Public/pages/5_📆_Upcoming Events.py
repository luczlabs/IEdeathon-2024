# Packages
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from datetime import datetime


# Imported
from data import text, colors, get_image, upcoming_events


# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['Upcoming Events Page']


# Title
st.caption('UPCOMING EVENTS PAGE')
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">Upcoming </span>
        <span style=" font-size:75px ; color:{main_color} ; font-weight:bold; ">Events</span>
    </div>""",
    unsafe_allow_html=True
)
add_vertical_space(2)


# Events
for event, data in upcoming_events.items():
    with st.container(border=True):
        target_datetime = datetime.strptime(data['date'], "%B %d, %Y")
        current_datetime = datetime.now()
        time_difference = target_datetime - current_datetime
        
        st.caption(data['date'])
        st.subheader(event)
        st.write(data['description'])
        

