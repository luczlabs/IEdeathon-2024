import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_gsheets import GSheetsConnection
from st_pages import Page, Section,show_pages, add_page_title
from streamlit_extras.switch_page_button import switch_page


# Imported
from data import text, colors, get_image


# Variables
ss = st.session_state
main_color = colors['main']


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

            # store member info from database
            member_id = st.session_state['password']
            member_info = df[df['Member ID'] == member_id].to_dict('records')
            st.session_state['member_info'] = member_info
            
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
show_pages(
    [
        Page('Home.py', 'Log-in', '👤'),
        Page('menu_pages/dashboard.py', 'Project Blue Dashboard', '📊'),
        Page('menu_pages/reports.py', 'Project Reports', '📄'),
        Page('menu_pages/members.py', 'Members', '✋'),
        Page('menu_pages/exit.py', 'Exit Process', '👋')
    ]

)

switch_page('project blue dashboard')
hide_pages(['log-in'])



