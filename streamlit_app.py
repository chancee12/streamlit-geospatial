import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("About Chancee's Open Source Mapping Tools")
st.sidebar.info(
    """
    Explore Chancee's Open Source Mapping Tools in this web application. For more information, visit:
    - GitHub repository: <https://github.com/chancee/opensource-mapping-tools>
    """
)

st.sidebar.title("Contact Chancee")
st.sidebar.info(
    """
    Get in touch with Chancee through the following platforms:
    - [GitHub](https://github.com/chancee) | [Twitter](https://twitter.com/chancee) | [LinkedIn](https://www.linkedin.com/in/chancee)
    """
)

st.title("Open Source Mapping Tools by Chancee")

st.markdown(
    """
    Dive into a variety of interactive web apps developed by Chancee using open source mapping tools, featuring [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). 
    """
)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
