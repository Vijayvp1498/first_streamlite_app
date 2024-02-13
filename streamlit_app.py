import streamlit

streamlit.title('My Parent New Healthy')
streamlit.header('Breakfast Menu')
streamlit.text('🎂 Omega 3 & Blueberry ')
streamlit.text('🏵️ Hard-Boiled Fried ')

streamlit.title('Build Your Own fruits 🍎🍒🍉🍓🍊🥭🫒🥝')

import request
fruityvice_response=request.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
