import streamlit

streamlit.title('My Parent New Healthy')
streamlit.header('Breakfast Menu')
streamlit.text('🎂 Omega 3 & Blueberry ')
streamlit.text('🏵️ Hard-Boiled Fried ')

streamlit.title('Build Your Own fruits 🍎🍒🍉🍓🍊🥭🫒🥝')

import pandas
my_fruit_list =pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/data/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
