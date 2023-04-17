import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Chancee Vincent, Axim Geospatial Solutions Architect:
    [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6) | [GitHub](https://github.com/chancee12/)
    
    Axim Homepage:
    [Axim Geospatial](https://www.aximgeo.com/)
    
    Additional Thank You, Qiusheng Wu:
    [LinkedIn](https://www.linkedin.com/in/qiushengwu/)    
    """
)

st.sidebar.title("Support")
st.sidebar.write(
    """
    If you want to reward my work, I'd love a cup of coffee from you. Thanks!
    """
)
st.sidebar.markdown(
    "[buymeacoffee.com/giswqs](https://www.buymeacoffee.com/chanceevins)",
    unsafe_allow_html=True
)
st.title("Streamlit for Geospatial Applications")

st.markdown(
    """
    This multi-page web app demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and open-source mapping libraries, 
    such as [leafmap](https://leafmap.org), [geemap](https://geemap.org), [pydeck](https://deckgl.readthedocs.io), and [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter).
    This is an open-source project and you are very welcome to contribute your comments, questions, resources, and apps as 
    [pull requests](https://github.com/chancee12/streamlit-geospatial/pullss) to the [GitHub repository](https://github.com/chancee12/streamlit-geospatial).

    """
)

st.info("Click on the left sidebar menu to navigate to the different apps.")

st.subheader("Timelapse of Satellite Imagery")
st.markdown(
    """
    The following timelapse animations were created using the Timelapse web app. Click `Timelapse` on the left sidebar menu to create your own timelapse for any location around the globe.
"""
)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/spain.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

with row1_col2:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")
