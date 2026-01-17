import streamlit as st
import pandas as pd
import numpy as np

# Create a DataFrame with random latitude and longitude data
df = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=["lat", "lon"]
)

# Display the map
st.map(df)