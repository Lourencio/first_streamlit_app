import streamlit as st
import pandas as pd
import requests as rq
import snowflake.connector
from urllib.error import URLError

st.title('My Parents New Healthy Diner')
st.header(' Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Load datas
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list  = my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can the fruit they want to include
st.multiselect("Pick some fruits:", list(my_fruit_list.index))

#Display the table on the page
st.dataframe(my_fruit_list)

#Connect to snowflake
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("select * from fruit_load_list")
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")

#my_data_row = my_cur.fetchone() apenas uma linha
my_data_row = my_cur.fetchall() 

st.header("The fruit load list contains")
st.dataframe(my_data_row)


st.header('Fruitvice Fruit Advice!')
try:
  fruit_choice = st.text_iuput('What fruit wold you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    fruityvice_response = rq.get("https://fruityvice.com/api/fruit" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    st.dataframe(fruityvice_normalized)
except URLError as e:
  st.error()

#fasdfas
