#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:56:39 2025

@author: alexandre
"""




import streamlit as st
from st_files_connection import FilesConnection
import streamlit.components.v1 as components






st.set_page_config(layout='wide', page_title='Titre page')


@st.cache_data()


#carte
def get_map():
    conn = st.connection('gcs', type=FilesConnection)
    with conn.open("schema_vff/index.html", 'r') as map_file:
        map_html = map_file.read()
    return map_html




map_html = get_map()



page_bg_img = f"""
<style>
    @import url('https://fonts.googleapis.com/css?family=Montserrat')

    h1 {{
        margin-top: -100px;
        font-family: 'Montserrat';
        color: white;
        }}
    [data-testid="stAppViewContainer"] {{
        background: rgb(0,140,149);
        }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
        }}
    iframe {{
        flex-grow: 1; /* Allow the iframe to grow and take available space */
        width: 100%;
        min-height: 80vh;
}}
    :has(iframe) {{
        display: flex;
        flex-direction: column;
        height: 100%; /* Ensure the container takes up the full height of its parent */
}}
</style>
"""



st.markdown(page_bg_img, unsafe_allow_html=True)





with st.container():  
    st.title('Carte titre test')
    components.html(map_html)















