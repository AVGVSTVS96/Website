import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Bassim's Website", page_icon=":wave:")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- Assets ----

animation = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_cmaqoazd.json")
animation2 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_8po4g2xf.json")
animation3 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_vu2p4il8.json")
animation4 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_DbCYKfCXBZ.json")

# ---- Header Section ----
with st.container():
    st.title(":earth_americas: Hi, I'm Bassim")
    st.subheader("I'm an IT Technician working at the NYC Bar Association")

with st.container():
    st.write("---")
    st.subheader("I'm learning how to write my first website!")
    st.write("This website is written with the help of Streamlit, a Python library that makes writing a website easy!")

# ---- What I Do ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            #### My IT skills include:
            - Network administration
            - Cybersecurity
            - Hardware installation
            - System maintenance
            - System troubleshooting
            """)
    with right_column:
        st_lottie(animation, height=200, key="work")

# ---- What I Study ----

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("""
        #### My Academic Interest Include:
        - History
        - Philosophy
        - Sociology
        - Political Science 
        - Computer Science
        """)
    with right_column:
        st_lottie(animation2, height=200, key="study")

#  ---- What I do for fun ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("""
        #### Some of my hobbies include:
        - Building first person view (FPV) drones
        - Creating 3D models
        - Making with 3D printers
        - Building computers
        - Cars and racing
        - Learning new things
        """)
    with right_column:
        st_lottie(animation3, height=200, key="fun")

# ---- Contact ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("""
        #### What I'm currently learning:
        - Programming with Python
        - Data Science with Pandas and Numpy
        - Frontend development with Streamlit 
        - Web scraping with BeautifulSoup
        """)
    with right_column:
        st_lottie(animation4, height=200, key="coding")