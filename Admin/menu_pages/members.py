# Packages
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import pandas as pd


# Imported
from data import text, colors, get_image


# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['Membership Status']
member_info = st.session_state.member_info[0]


# Title
st.caption('MEMBERSHIP TIERS PAGE')
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">Ahoy, </span>
        <span style=" font-size:75px ; color:{main_color} ; font-weight:bold; ">{member_info['First Name']} </span>
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">!🌊</span>
    </div>""",
    unsafe_allow_html=True
)
add_vertical_space(2)

# CONTENT
st.write(section_text['Message'])
tiers = pd.read_csv('tiers - Sheet1.csv',)

with st.container(border=True):
    st.subheader('Tiers')

    for index, tier in tiers.iterrows():
        with st.expander(tier['Membership Tier Names']):
            st.write(tier['Description'])
            st.write(tier['Rubrics'])
            
# VIEW YOUR TIER
def tiername(meetings, involved, led):
    res = "Explorer Starfish"

    meetings = int(meetings[:-1]) if meetings[-1] == '%' else int(meetings)

    if meetings >=95 and involved >=9 and led >=4:
        res = "Sentinel Whale"
    elif meetings >=90 and involved >=7 and led >=3:
        res = "Defender Dolphin"
    elif meetings >=75 and involved >=5 and led >=2:
        res = "Guardian Crab"
    elif meetings >=50 and involved >=3 and led >=1:
        res = "Steward Jellyfish"
    else:
        res = "Explorer Starfish"
    return res

tier = st.button('View Your Tier', type='primary')
# Check if the button is clicked
if tier:
    # Call the function when the button is clicked
    result = tiername(
        member_info['Attendance Rating'],
        member_info['No. of Projects Involved'],
        member_info['No. of Projects Led']
    )
    st.write(f"""🌊 Project Blue Distinction Unlocked! 🌟 \n\n As a **{result}**, you're making waves in environmental conservation with Project Blue! 🌍✨\n\nYour Project Blue score sets you apart, propelling you to the next level of distinction.
Show your commitment to a sustainable future by sharing this badge. 🎉 Let's inspire others to join the movement! 💙 \n\n #ProjectBlue \n #SustainabilityChampion \n\n Thank you for being a vital part of our ocean-saving community! 🐬🌊""")
    st.divider()
    st.subheader("**Share this to your friends!**")
    if result == "Explorer Starfish":
        st.image(get_image("Member Status_Shareable T1.png"))
    if result == "Steward Jellyfish":
        st.image(get_image("Member Status_Shareable T2.png"))
    if result == "Guardian Crab":
        st.image(get_image("Member Status_Shareable T3.png"))
    if result == "Defender Dolphin":
        st.image(get_image("Member Status_Shareable T4.png"))
    if result == "Sentinel Whale":
        st.image(get_image("Member Status_Shareable T5.png"))
    
    