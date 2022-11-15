from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Javi's Project, PseudoTrust!

With the power of ML, we can help you find out if another profile is trustworthy or not below:
"""

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)
trust_button = st.button("Investigate Profile!")
st.write(trust_button)
