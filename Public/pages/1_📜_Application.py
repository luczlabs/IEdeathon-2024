# Packages
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


# Imported
from data import text, colors, get_image, donation_methods


# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['Application Page']


# Functions
def donate_button():
    ss.donate = True


# Title
st.caption('APPLICATION PAGE')
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">Ready to </span>
        <span style=" font-size:75px ; color:{main_color} ; font-weight:bold; ">dive </span>
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">in?</span>
    </div>""",
    unsafe_allow_html=True
)
add_vertical_space(2)


col1, col2 = st.columns(2)
### alternatively, we can also do tabs bc the forms will get squished (also, maybe put a banner for each tab if ever)
# Project Blue Member
with col1:
    st.subheader(section_text['member']['title'])
    st.write(section_text['member']['description'])
    st.divider()
    st.write(section_text['member']['steps'])


# Project Blue Ambassador
with col2:
    st.subheader(section_text['ambassador']['title'])
    st.write(section_text['ambassador']['description'])
    st.divider()
    st.write(section_text['ambassador']['steps'])

# Donate
st.divider()
st.caption('DONATE TODAY')
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