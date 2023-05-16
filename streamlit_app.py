import streamlit as st
import leafmap.foliumap as leafmap

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

st.sidebar.title("Support")
st.sidebar.write(
    """
    If you want to reward my work, I'd love a cup of coffee from you. Thanks!
    """
)
st.sidebar.markdown(
    "[buymeacoffee.com/chanceevins](https://www.buymeacoffee.com/chanceevins)",
    unsafe_allow_html=True
)


# Customize page title
st.title("Streamlit for Geospatial Applications")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org).
    """
)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
