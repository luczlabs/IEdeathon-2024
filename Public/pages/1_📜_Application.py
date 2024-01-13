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


tab1, tab2 = st.tabs(['Project Blue Member', 'Project Blue Ambassador'])
# Project Blue Member
with tab1:
    st.subheader(section_text['member']['title'])
    st.write(f"*{section_text['member']['description']}*")
    
    add_vertical_space(1)

    member_steps = section_text['member']['steps'].split('\n')
    st.write(f'**{member_steps[0]}**')
    
    html_str = """
                <!DOCTYPE html> 
        <html> 
        <body> 
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSfXZhCYRvAk-rUY6GHKd-EpRKiRh3HwcD88v7BarVTQuRCSiw/viewform?embedded=true" width="640" height="382" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
        </body> 
        </html> 
        """
    st.markdown(html_str, unsafe_allow_html=True)
    st.divider()

    for i in range(1,len(member_steps)):
        st.write(f'{member_steps[i]}')




# Project Blue Ambassador
with tab2:
    st.subheader(section_text['ambassador']['title'])
    st.write(f"*{section_text['ambassador']['description']}*")

    add_vertical_space(1)

    ambassador_steps = section_text['ambassador']['steps'].split('\n')
    st.write(f'**{ambassador_steps[0]}**')
    
    html_str = """
                <!DOCTYPE html> 
        <html> 
        <body> 
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSfvjcuSym_svJmteg2YJwXT5ZEqCc-BlNM4wPKSk590zf2kyQ/viewform?embedded=true" width="640" height="382" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
        </body> 
        </html> 
        """
    st.markdown(html_str, unsafe_allow_html=True)
    st.divider()

    for i in range(1,len(ambassador_steps)):
        st.write(f'{ambassador_steps[i]}')


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