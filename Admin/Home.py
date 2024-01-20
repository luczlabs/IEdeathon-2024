import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1W818H_EO4ChWBsnbhZYnajeCxnsaLi2s0JWGIgbh13s/edit#gid=2044290198"

url = url.replace(' ', '%20')

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheet=url)

st.title('Project Blue Dashboard')

st.write(df)

