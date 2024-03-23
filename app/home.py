import streamlit as st

st.set_page_config(
        page_title="good-practice",
        page_icon="app/static/plot.png",
        layout="wide",
    )

st.header("Research Software Good Practice")

import math
import plotly.express as px
import pandas as pd

df = px.data.gapminder().query("year==2007 and continent=='Asia'")
fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="lifeExp", \
                 size="pop", log_x=True, size_max=60)

fig.update_layout(
    height=800,width=1200,
    title_text='GDP and Life Expectancy (Asia, 2007)'
)
for idx in df.index:
    url="<a href='https://en.wikipedia.org/wiki/Demographics_of_"+df['country'][idx]+"' target='_blank'>"+df['country'][idx]+"</a>"
    fig.add_annotation(dict(x=math.log10(df['gdpPercap'][idx]),
                            y=df['lifeExp'][idx],
                            showarrow=False,
                            text=url,
                            xanchor='auto',
                            yanchor='auto'))
fig.show()