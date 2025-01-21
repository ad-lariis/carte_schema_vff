#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:56:39 2025

@author: alexandre
"""




import streamlit as st
from st_files_connection import FilesConnection
import streamlit.components.v1 as components
from PIL import Image
from pathlib import Path





path = Path.cwd()
path_image = path / 'res/logo_page_noir.jpg'
image = Image.open(path_image)


st.set_page_config(layout='wide', page_title='Offres services VFF', page_icon=image)


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
    .block-container {{
        padding-top: 0.5rem;
        }}
    body {{
        font-family: "Montserrat", serif;
        }}
    h1 {{
        font-family: "Montserrat", serif;
        color: white;
        font-size: 1.8em;
        }}
    [data-testid="stAppViewContainer"] {{
        background: rgb(0,140,149);
        }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
        }}
    iframe {{
        flex-grow: 1; 
        width: 100%;
        min-height: 80vh;
}}
    :has(iframe) {{
        display: flex;
        flex-direction: column;
        height: 100%; 
}}
</style>
"""



st.markdown(page_bg_img, unsafe_allow_html=True)




st.title('Offres de services destinées aux femmes victimes de violences')

with st.container():  
    components.html(map_html)















