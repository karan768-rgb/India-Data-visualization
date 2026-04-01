import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

dff = pd.read_csv('india_csv')

list_of_state = list(dff['State'].unique())
list_of_state.insert(0,'Overall India')

st.sidebar.title('India Data Viz')

selected_state = st.sidebar.selectbox('Select a state',list_of_state)
primary = st.sidebar.selectbox('Select Primary parameter',sorted(dff.columns[5:]))
secondary = st.sidebar.selectbox('Select secondary parameter',sorted(dff.columns[5:]))

plot = st.sidebar.button('Plot Graph')
if plot:
    if selected_state == 'Overall India':
        st.title(f"India's {primary.replace('_', ' ').title()} vs {secondary.replace('_', ' ').title()} Map")
    else:
        st.title(f"{selected_state}'s {primary.replace('_', ' ').title()} vs {secondary.replace('_', ' ').title()} Map")


    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(dff, lat='Latitude', lon='Longitude',size=primary , color=secondary, zoom=4, size_max=35,
                                mapbox_style='carto-positron', width=1200, height=700, color_continuous_scale='Turbo', hover_name='State' )

        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = dff[dff['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary, zoom=6, size_max=35,
                                mapbox_style='carto-positron', width=1200, height=700, hover_name='District',color_continuous_scale='Turbo' )

        st.plotly_chart(fig, use_container_width=True)