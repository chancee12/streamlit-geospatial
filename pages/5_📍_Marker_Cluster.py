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
    
    Additional Thank You, Qiusheng Wu:
    [LinkedIn](https://www.linkedin.com/in/qiushengwu/)    
    """
)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
        regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'

        m.add_geojson(regions, layer_name='US Regions')
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            color_column='region',
            icon_names=['gear', 'map', 'leaf', 'globe'],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
