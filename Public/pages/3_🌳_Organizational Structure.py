# Packages
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


# Imported
from data import text, colors, get_image, organization_structure


# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['Organizational Structure Page']


# Title
st.caption('APPLICATION PAGE')
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">Organizational </span>
        <span style=" font-size:75px ; color:{main_color} ; font-weight:bold; ">Structure</span>
    </div>""",
    unsafe_allow_html=True
)
st.write(section_text['description'])

add_vertical_space(2)


# Organizational structure
with st.container(border=True):
    org_struc = get_image('Organizational Structure.png')
    st.image(org_struc)

# 2 rows of all committees clickable images, go to header anchor 
# st.header("Section 1")
# st.markdown("[Section 1](#section-1)", unsafe_allow_html=True)

# Committees
for committee,data in organization_structure.items():
    with st.container(border=True):

        st.markdown(f'<h1 style="color:{main_color};font-size:36px;font-weight:600;">{committee}</h1>', unsafe_allow_html=True)
        st.write(f"*{data['Committee Description']}*!")
        st.write(data['Committee Invitation'])

        tab1, tab2 = st.tabs(['Positions', 'Testimonial'])
        with tab1:
            for pos, desc in data['Position Description'].items():
                st.write(f"**{pos}**: {desc}")
        with tab2:
            testimonial = data['Testimonial'].split('\n')
            st.write(f'**{testimonial[0].title()}**')
            st.write(f'*{testimonial[1].title()}*')
            st.write(testimonial[-1])