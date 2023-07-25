import streamlit as st
from pages import SEOChatbot

def main():
    st.set_page_config(layout="wide")

    st.sidebar.info(
    """
    - Hugging Face: <https://huggingface.co/Chancee12>
    - GitHub repository: <https://github.com/chancee12/>
    """
    )

    st.sidebar.title("Contact")
    st.sidebar.info(
        """
        Chancee Vincent, Axim Geospatial Solutions Architect:
        [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6) | [GitHub](https://github.com/chancee12/)
        
        Axim Homepage:
        [Axim Geospatial](https://www.aximgeo.com/) 
        """
    )

    SEOChatbot.app()

if __name__ == "__main__":
    main()
