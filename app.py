import streamlit as st
import os

st.title("main page")

folder_image = "./pages/space_jet"
files = os.listdir(folder_image)
for file in files:
    st.image(f"{folder_image}/{file}", width=300, caption=file)
    st.text(file)

