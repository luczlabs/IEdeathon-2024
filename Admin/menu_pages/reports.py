# Packages
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


# Imported
from data import text, colors, get_image


# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['Project Evaluation Report Page']


# Title
st.caption('PROJECT EVALUATION REPORT PAGE')
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">Project </span>
        <span style=" font-size:75px ; color:{main_color} ; font-weight:bold; ">Evaluation Report</span>
    </div>""",
    unsafe_allow_html=True
)
add_vertical_space(2)


# Content
st.write(section_text['Message'])

html_str = """
            <!DOCTYPE html> 
    <html> 
    <body> 
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeGAdALmhhfIyK-_tfEN9Ftsnkf27h7eyEzRZ36gSltVX1byA/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </body> 
    </html> 
    """
st.markdown(html_str, unsafe_allow_html=True)

add_vertical_space(1)

with st.container(border=True):
    st.subheader('Project Archive 👥')
    st.write("Delve into our Project Archive, a repository of past projects. Gain insights, lessons learned, and best practices from previous initiatives. This archive serves as a valuable knowledge base for future projects.")
    archive = st.button('View Project Archive', type='primary')