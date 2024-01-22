
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_gsheets import GSheetsConnection


# Imported
from data import text, colors, get_image


# Variables
ss = st.session_state
main_color = colors['main']
# section_text = text['']


# Google Sheets Connection
member_database = st.secrets['member_database']
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=member_database)


# Title
st.caption('ADMIN PAGE')
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">Project Blue </span>
        <span style=" font-size:75px ; color:{main_color} ; font-weight:bold; ">Admin</span>
    </div>""",
    unsafe_allow_html=True
)
add_vertical_space(2)


# User Authentication
def check_password():

    # Log-in
    def log_in():
        with st.form('Credentials'):
            st.text_input("Member ID", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)
 
    def password_entered():
        if df['Member ID'].eq(st.session_state['password']).any():
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    log_in()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False

if not check_password():
    st.stop()


# Welcome
member_id = st.session_state['password']