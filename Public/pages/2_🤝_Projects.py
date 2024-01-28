# Packages
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_gsheets import GSheetsConnection


# Imported
from data import text, colors, get_image


# Variables
ss = st.session_state
main_color = colors['main']
section_text = text['Projects Page']


# Title
st.caption('APPLICATION PAGE')
add_vertical_space(1)
st.markdown(f"""
    <div style="line-height:450%;">
        <span style=" font-size:75px ; color:#31333F ; font-weight:bold; ">Project </span>
        <span style=" font-size:75px ; color:{main_color} ; font-weight:bold; ">Accomplishment Report</span>
    </div>""",
    unsafe_allow_html=True
)
add_vertical_space(2)


# Google Sheets Connection
url = st.secrets['spreadsheet']
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url)


# Find min,max
df['Year'] = df['Date'].str.split().str.get(-1)
df['Year'] = df['Year'].astype(int)


# Filter
col1, col2 = st.columns(2)
with col1:
    start = st.number_input('Starting year', min_value=df['Year'].min(), max_value=df['Year'].max(), value=df['Year'].min())
    add_end = st.checkbox('Add ending year', value=True)
if add_end:
    with col2:
        end = st.number_input('Ending year', min_value=df['Year'].min(), max_value=df['Year'].max(), value=df['Year'].max())
else:
    end = start
year_filter = [year for year in range(start, end+1)]
filtered_df = df.query('Year in @year_filter')


# Display
st.divider()
for index, row in filtered_df.iterrows():
    with st.container(border=True):
        st.caption(row['Date'])
        st.subheader(row['Activity'])
        st.image(get_image(row['Images']))
        st.write(row['Description'])


