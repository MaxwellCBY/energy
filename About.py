import streamlit as st
import pandas as pd
from PIL import Image
import time
# from openai import OpenAI
import os




cap1= "Depending on the level of access, you can view public information, member information, and agreement information."

cap2= "Public information includes basic details of a company, such as name, website, and types of products as metadata."

cap3= "Public information can be obtained through traditional search methods."

cap4= "Member public information includes case details of the company, such as its products, services, solutions, or quotations."

cap5= "1- Platform AI understands the question, 2- Platform AI sends the question to the member company's AI, 3- Member AI answers the question, 4- Platform AI summarizes the answer."

cap6= "Access to agreement information requires the company's authorization before you can continue to inquire about solutions or quotations."

cap7= "Once access is granted, you can continue to converse with the company's AI assistant to obtain more information."



st.title('Enterprise X')
# subheader
# Using markdown to format the subheader more neatly
st.markdown("""
### AI-CONSULTANT ACROSS ENTERPRISES""", unsafe_allow_html=True)


# go to the current directory
os.chdir(os.path.dirname(__file__))
# st.write("Welcome to the main page of our multi-page Streamlit app!")
# Load an image

with st.expander("Structure", expanded=False):
    image_path_1 = r'image\about\1.png'
    image_1 = Image.open(image_path_1)
    # show images
    st.image(image_1, caption=cap1)
    # st.markdown("<br><br>", unsafe_allow_html=True)  # Adds two line breaks


with st.expander("Public information", expanded=False):
    image_path_2 = r'image\about\2.png'
    image_2 = Image.open(image_path_2)
    st.image(image_2, caption=cap2)
    # st.markdown("<br><br>", unsafe_allow_html=True)  # Adds two line breaks


with st.expander("Public information Search", expanded=False):
    image_path_3 = r'image\about\3.png'
    image_3 = Image.open(image_path_3)
    st.image(image_3, caption=cap3)
    # st.markdown("<br><br>", unsafe_allow_html=True)  # Adds two line breaks


with st.expander("Member information", expanded=False):
    image_path_4 = r'image\about\4.png'
    image_4 = Image.open(image_path_4)
    st.image(image_4, caption=cap4)
    # st.markdown("<br><br>", unsafe_allow_html=True)  # Adds two line breaks


with st.expander("Member information Search", expanded=False):
    image_path_5 = r'image\about\5.png'
    image_5 = Image.open(image_path_5)
    st.image(image_5, caption=cap5)
    # st.markdown("<br><br>", unsafe_allow_html=True)  # Adds two line breaks

with st.expander("Protocol Public information", expanded=False):
    image_path_6 = r'image\about\6.png'
    image_6 = Image.open(image_path_6)
    st.image(image_6, caption=cap6)
    # st.markdown("<br><br>", unsafe_allow_html=True)  # Adds two line breaks

with st.expander("Authoritation", expanded=False):
    image_path_7 = r'image\about\7.png'
    image_7 = Image.open(image_path_7)
    st.image(image_7, caption=cap7)
    # st.markdown("<br><br>", unsafe_allow_html=True)  # Adds two line breaks




