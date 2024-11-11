import streamlit as st

from streamlit_option_menu import option_menu

import account,Home,about,admin

st.set_page_config(
    page_title="Pavement Assessment",
    page_icon="🛣️",
    layout="wide",
    initial_sidebar_state="expanded",
)

if 'username' not in st.session_state:
    st.session_state.username = ''

class MultiApp:
    def _init_(self):
        self.apps=[]
    def add_app(self,title,func):
        self.apps.append({
            "title":title,
            "function":func  
       })
    def run():

        with st.sidebar:
            app = option_menu(
                menu_title='Pavement Assessment',
                options=['Home','Admin','User login','About'],
                icons=['house-fill','person-circle','people-fill','info-circle'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container":{"padding":"5!important","background-color":"black"},
                    "icon":{"color":"white","font-size":"23px"},
                    "nav-link":{"color":"white","font-size":"20px","text-align":"left","margin":"0px"},
                    "nav-link-selected":{"background-color" :"#000080"},
                }
            )
        if app=='Home':
            home1.app()
        if app=='Admin':
            admin.app()
        if app=='User login':
            account.app()
        if app=='About':
            about.app()
    run()
