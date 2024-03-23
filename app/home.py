import streamlit as st

st.set_page_config(
        page_title="good-practice",
        page_icon="app/static/good.png",
        layout="wide",
    )

st.header("Research Software Good Practice")
 
import plotly.express as px
import pandas as pd

colors = {}
colors['doc'] = 'hotpink'
colors['follow-along'] = 'dodgerblue'
colors['tools'] = 'limegreen'

df = pd.read_csv("app/data/resources.csv")

st.write("Start here ---- >")
fig = px.scatter(df, x="level", y="position", color="kind",size_max=600)

fig.update_layout(
    #height=800,width=1200,
    title_text='',
    showlegend=False
)
fig.update_yaxes( autorange="reversed",showgrid=False,showline=False,showticklabels=False,visible=False)
fig.update_xaxes( showgrid=False,showline=False,showticklabels=False,visible=False)

for idx in df.index:
    url='<a href="https://icr-rse-group.github.io/good-practice/'+ df['resource'][idx] + '" target="_blank" style="color:black"><span style="color:black">' + df['resource'][idx] + '</span></a>'    
    fig.add_annotation(dict(x=df['level'][idx],
                            y=df['position'][idx],
                            showarrow=False,
                            bordercolor="#c7c7c7",
                            borderwidth=2,
                            borderpad=4,
                            bgcolor=colors[df['kind'][idx]],
                            opacity=1,
                            font=dict(
                                family="Arial Black",
                                size=16,                                
                                color="black"
                                ),
                            text=url,
                            xanchor='auto',
                            yanchor='auto'))

fig.layout.template = 'plotly_dark'
fig.update_traces(marker=dict(size=10,
                              opacity=1,
                              symbol="square",
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

st.plotly_chart(fig, use_container_width=True)


#fig.show()