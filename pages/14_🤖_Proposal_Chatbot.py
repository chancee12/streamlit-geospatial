import streamlit as st
from page import main_page

def app():
    st.set_page_config(
        page_title="Chancee's Proposal AI Assistant Beta V.1.0.2",
        page_icon=":robot:",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "Chancee's AI Assistant is designed specifically to revise government contracting proposals the best way possible. Utilizing OpenAI API, it assists in restructuring sentences, clarifying ambiguities, eliminating redundancies, and enhancing the overall presentation."
        }
    )

    st.sidebar.info(
        """
        Chancee Vincent, Axim Geospatial Solutions Architect:
        [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6) | [GitHub](https://github.com/chancee12/)
        
        Axim Homepage:
        [Axim Geospatial](https://www.aximgeo.com/)  
        """
    )

    main_page()

if __name__ == "__main__":
    app()
