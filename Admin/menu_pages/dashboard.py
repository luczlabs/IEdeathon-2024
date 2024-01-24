import streamlit as st
import pandas as pd
import math
import plotly.express as px
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_gsheets import GSheetsConnection
from data import colors, get_image

main_color = colors['main']

def read_gsheet(url):
    url = url.replace(' ','%20')    
    df = conn.read(spreadsheet=url)
    return df 

conn = st.connection("gsheets", type=GSheetsConnection)

# Member Masterlist 2024
url_1 = "https://docs.google.com/spreadsheets/d/1W818H_EO4ChWBsnbhZYnajeCxnsaLi2s0JWGIgbh13s/edit?usp=sharing"
df_24 = read_gsheet(url_1)

# Member Masterlist 2023
url_2 = "https://docs.google.com/spreadsheets/d/1GvjsnI3tmwQf9lHakQ2FQbEZ6zFBS0soFcSQkMgdIls/edit?usp=sharing"
df_23 = read_gsheet(url_2)

# Member Masterlist 2022
url_3 = "https://docs.google.com/spreadsheets/d/1cGkh4xTxXC7vegVB8J8mY_fd7hH6aCLtoXt4v-ozHQs/edit?usp=sharing"
df_22 = read_gsheet(url_3)

# Projects
url_4 = "https://docs.google.com/spreadsheets/d/1c5XYFt_964zfgaE5-O3ln6NZ0ud-LCEGsuiZKRt_kOw/edit?usp=sharing"
df_prj = read_gsheet(url_4)

# Members Dataframe
data = {'Year': ['2024', '2023', '2022'],'No. of Members': [f'{df_24.shape[0]} members', f'{df_23.shape[0]} members', f'{df_22.shape[0]} members']}
df_members = pd.DataFrame(data)

# Title
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:60px ; color:{main_color} ; font-weight:bold; ">Project Blue </span>
        <span style=" font-size:60px ; color:#31333F ; font-weight:bold; ">Dashboard</span>
    </div>""",
    unsafe_allow_html=True
)
add_vertical_space(2)

# Member Details
col_1, col_2 = st.columns([1.1,2])

#Growth Rate and Title
with col_1:
    #with st.container(border=True):
    st.markdown(f'<p style="margin-left: 20px; margin-top:5px; margin-bottom:10px; font-size:52px;"><strong>Members</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="margin-left:20px; margin-top:-35px; font-size:40px; color:{main_color};"><strong>Overview 👥</p>', unsafe_allow_html=True)



with col_2:
    with st.container(border=True): 
        col_1_1, col_2_2 = st.columns([1.5,1])
        with col_1_1:
            growth_num = ((df_24.shape[0]-df_23.shape[0])/df_23.shape[0]*100)
            st.markdown(f'<p style="margin-bottom: -50px; color:{main_color}; font-size:20px; "><strong>  Membership Growth Rate</p>', unsafe_allow_html=True)
            st.title(f"{math.ceil(growth_num)}%")
            if growth_num > 0:
                st.markdown(f'<p style="margin-top:-20px; color: #2E8B57; font-size:14px;">↑ increase from 2023</p>', unsafe_allow_html=True)
       
        with col_2_2:
            html_string = df_members.style \
                .hide_index() \
                .hide_columns() \
                .set_table_styles([{'selector': 'td, th', 'props': [('font-size', '13px'), ('text-align', 'center'), ('border', '1px solid #dddddd')]}]) \
                .set_properties(**{'background-color': '#f2f2f2'}, subset=pd.IndexSlice[:, ['Year']]) \
                .render()
            st.markdown(f'<p style=margin-top:-12px;">{html_string}</p>', unsafe_allow_html=True)

#Location and Age

col_3, col_4 = st.columns([1,1])

#Location
with col_3:
    with st.container(border=True):
        df_24['Count'] = 1 
        df_24_grouped = df_24.groupby(['Region', 'City']).agg({'Count': 'sum'}).reset_index()
        custom_colors = ['#0A2647','#144272','#164D76','#205295','#2C74B3','#0077B6']
        fig_loc = px.sunburst(df_24_grouped, path=['Region', 'City'], values='Count', color_discrete_sequence=custom_colors)
        fig_loc.update_layout(width=375, height=375)
        fig_loc.update_layout(margin=dict(t=15))
        st.markdown(f'<p style="margin-bottom: -20px; color:{main_color}; font-size:20px; text-align:center;"><strong>Geographical Distribution</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="margin-top:3px; margin-bottom:-20px; color: #000000; font-size:13px; text-align:center;"><em>This chart displays the geographic distribution of our members across different regions and cities.</em></p>', unsafe_allow_html=True)
        st.plotly_chart(fig_loc, use_container_width=True)
        st.markdown(f'<p style="margin-top:-90px; margin-bottom:-50px; color: #000000; font-size:15px; text-align:center;">Explore the data by clicking on <br>specific regions within the chart.</p>', unsafe_allow_html=True)
        st.write(df_24_grouped)
#Age
with col_4:
    with st.container(border=True):
        df_24['Count'] = 1 
        df_24_grouped = df_24.groupby(['Age']).agg({'Count': 'sum'}).reset_index()
        fig_age = px.pie(df_24_grouped, values='Count', names='Age', color_discrete_sequence=custom_colors)
        fig_age.update_traces(textinfo='percent+label', pull=[0.1, 0.1, 0.1, 0.1], showlegend=True)
        fig_age.update_layout(width=375, height=375)
        fig_age.update_layout(margin=dict(t=15))
        fig_age.update_layout(
        legend=dict(
            orientation='h',
            y=-0.1,  # Adjust the y-coordinate to control the position of the legend
            x=0.5,
            xanchor='center'
        )
    )
        st.markdown(f'<p style="margin-bottom: -20px; color:{main_color}; font-size:20px; text-align:center;"><strong>Age Distribution</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="margin-top:3px; margin-bottom:-15px; color: #000000; font-size:13px; text-align:center;"><em>This chart displays the age distribution of our members.</em></p>', unsafe_allow_html=True)
        st.plotly_chart(fig_age, use_container_width=True)

add_vertical_space(3)

# Member Engagement
#with st.container(border=True):
st.markdown(f'<p style="margin-bottom:3px; margin-top:-12px; font-size:45px; text-align:center; color:{main_color}"><strong>Member Engagement</p>', unsafe_allow_html=True)
col_5, col_6 = st.columns([1,1])

# Attendance
with col_5:
    with st.container(border=True):
        df_24['Attendance Rating']=pd.to_numeric(df_24['Attendance Rating'].str.rstrip('%'))
        df_24_attend = int(round(df_24['Attendance Rating'].mean()))
        st.markdown(f'<p style="margin-bottom: -5px; color:{main_color}; font-size:20px; text-align:center;"><strong>  Meeting Attendance</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="margin-top:0px; margin-bottom:-75px; color: #000000; font-size:11px; text-align:center;"><em>Average Rating of Attendance of Members during Meetings</em></p>', unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; margin-top: -15px; font-size:40px;'>{df_24_attend}%</h1>", unsafe_allow_html=True)

# Project Involvement
with col_6:
    with st.container(border=True):
        df_24_involved = int(round(df_24['No. of Projects Involved'].mean()))
        st.markdown(f'<p style="margin-bottom: -5px; color:{main_color}; font-size:20px; text-align:center;"><strong>Project Involvement</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="margin-top:0px; margin-bottom:-75px; color: #000000; font-size:11px; text-align:center;"><em>Average No. of Involvement of Members in Projects</em></p>', unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; margin-top:-15px; font-size:40px'>{df_24_involved} Involvements</h1>", unsafe_allow_html=True)

# Committee Distribution
with st.container(border=True):
    df_24['Members'] = 1 
    df_24_grouped = df_24.groupby(['Committee']).agg({'Members': 'sum'}).reset_index()
    df_24_grouped = df_24_grouped.sort_values(by='Members', ascending=False)
    fig_com = px.bar(df_24_grouped, x='Committee', y='Members')
    fig_com.update_layout(width=375, height=375)
    fig_com.update_layout(margin=dict(t=15))
    st.markdown(f'<p style="margin-bottom: -5px; color:{main_color}; font-size:20px; text-align:center;"><strong>Distribution of Members across Committees</p>', unsafe_allow_html=True)
    st.write(fig_com)
    st.write('May space sa right kasi iniisip ko pwede siya lagyan if anong number of members for each committee ung ideal compared sa existing and iindiacte if naabot or hindi')
add_vertical_space(3)
# Hours and Success Rating
st.markdown(f'<p style="margin-bottom:3px; margin-top:-12px; font-size:45px; text-align:center; color:{main_color}"><strong>Community Outreach</p>', unsafe_allow_html=True)
col_7, col_8 = st.columns([1,1])
with col_7:
    with st.container(border=True):
        df_prj_sum = int(df_prj['No. of Engagement Hours'].sum())
        st.markdown(f'<p style="margin-bottom: -5px; color:{main_color}; font-size:20px; text-align:center;"><strong>Total No. of Engagement Hours</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="margin-top:0px; margin-bottom:-75px; color: #000000; font-size:11px; text-align:center;"><em>Total Engagement Hours of the Organization to the Communities</em></p>', unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; margin-top:-15px; font-size:40px'>{df_prj_sum} Hours</h1>", unsafe_allow_html=True)

with col_8:
    with st.container(border=True):
        df_prj_sum = int((df_prj['Success Rating'].sum()/(df_prj.shape[0]*5))*100)
        st.markdown(f'<p style="margin-bottom: -5px; color:{main_color}; font-size:20px; text-align:center;"><strong>Overall Sucess Rating</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="margin-top:0px; margin-bottom:-75px; color: #000000; font-size:11px; text-align:center;"><em>Average Success Rating of All Projects</em></p>', unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; margin-top:-15px; font-size:40px'>{df_prj_sum}% Successful</h1>", unsafe_allow_html=True)
