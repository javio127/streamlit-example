from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Javi's Project, PseudoTrust!

With the power of ML, we can help you find out if another profile is trustworthy or not below:
"""

num_followers = st.slider("Number of Followers", 1, 5000, 2000)
inf_score = st.slider("Influence Score", 1, 7000, 9)
num_posts = st.slider("Posts", 1, 1500, 9)
engagement_rate = st.slider("Engagement Rate", 1, 100, 9)
total_likes = st.slider("Total Likes", 1, 4000, 9)

trust_button = st.button("Investigate Profile!")
st.write(trust_button)

st.header("ANSWER: DO NOT TRUST")
