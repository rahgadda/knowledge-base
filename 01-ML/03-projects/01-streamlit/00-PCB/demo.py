import streamlit as st
from streamlit_option_menu import option_menu
import lib.page_settings as page_settings

# -- Page Settings
page_settings.initialLoad("Telangana Pollution Control Board","Welcome to PCB Command Center!!!")

# -- Main Menu  
selected = page_settings.menu(["Dashboard",'Transactions','Setup'],['speedometer','activity', 'gear'])

if selected=="Dashboard":
    st.header("Hello")