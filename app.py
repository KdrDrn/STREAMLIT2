import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")
st.title("Interact with Gapminder Data")

st.markdown("gapminder data")
gapminder = px.data.gapminder()
st.sidebar.dataframe(gapminder.head())

st.markdown("gapminder2007 data")
gapminder2007 = gapminder.query("year == 2007")
st.sidebar.dataframe(gapminder2007.head())

st.markdown("GDP vs LifeExp")
fig = px.scatter(gapminder2007, x="gdpPercap", y="lifeExp")
st.plotly_chart(fig)

st.markdown("GDP vs LifeExp By Continents")
fig = px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent")
st.plotly_chart(fig)


arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots(figsize=(5,3))
ax.hist(arr, bins=20)
st.pyplot(fig)


chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)