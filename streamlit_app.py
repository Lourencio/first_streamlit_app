import streamlit as st
import pandas as pd
import snowflake.connector

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

my_data_row = my_cur.fetchone()
#st.text("Hello from Snowflake:")
st.header("The fruit load list contains")
st.dataframe(my_data_row)
