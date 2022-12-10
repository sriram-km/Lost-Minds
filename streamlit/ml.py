import streamlit as st
import pandas as pd
from bokeh.plotting import figure
import numpy as np
import plotly.express as px

st.header("Analytics")
print("sample file is there in Analytics/data")
# st.video("/Users/cosmos/Desktop/hack-concode/Analytics/header.mp4")

uploaded_file = st.file_uploader("Choose a file")

#OR

#uploaded_file = "Analytics/data/weblog.csv"

if uploaded_file is not None:
     st.markdown("""---""")

     try:
          data = pd.read_csv(uploaded_file)
     except:
          data = pd.read_csv(uploaded_file,squeeze=True)
          
     st.write(data)
     
     try:
          st.markdown("""---""")

          st.write("Most Popular Methods by the Users")
          st.bar_chart(data['Methods'].value_counts())
          
          st.markdown("""---""")

          st.write("Most Popular URLs by the Users")
          st.bar_chart(data['URL_new'].value_counts().head(40))
          
          st.markdown("""---""")

          st.write("Most Popular Months of Logins")
          st.bar_chart(data['month'].value_counts().head(40))
          
          st.markdown("""---""")

          st.write("Most Popular Days of Logins")
          st.bar_chart(data['day'].value_counts().head(40))
          
          st.markdown("""---""")

          st.write("Most Popular statuses for the Users")
          st.bar_chart(data['Status'].value_counts().head(40))
          
          st.markdown("""---""")     
     except:
          st.write("Clean The Data...")
     
     
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
