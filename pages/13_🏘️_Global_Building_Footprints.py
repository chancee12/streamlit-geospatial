import ee
import geemap.foliumap as geemap
import geopandas as gpd
import streamlit as st

st.set_page_config(layout="wide")


@st.cache(persist=True)
def ee_authenticate(token_name="EARTHENGINE_TOKEN"):
    geemap.ee_initialize(token_name=token_name)


st.sidebar.info(
    """
    - Hugging Face: <https://huggingface.co/spaces/Chancee12>
    - GitHub repository: <https://github.com/chancee12/>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Chancee Vincent, Axim Geospatial Solutions Architect:
    [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6) | [GitHub](https://github.com/chancee12/)
    
    [Axim Geospatial](https://www.aximgeo.com/)
    
    Additional Thank You, Qiusheng Wu:
    [LinkedIn](https://www.linkedin.com/in/qiushengwu/)    
    """
)

st.title("Global Building Footprints")

col1, col2 = st.columns([8, 2])


@st.cache_data
def read_data(url):
    return gpd.read_file(url)


countries = 'https://github.com/giswqs/geemap/raw/master/examples/data/countries.geojson'
states = 'https://github.com/giswqs/geemap/raw/master/examples/data/us_states.json'

countries_gdf = read_data(countries)
states_gdf = read_data(states)

country_names = countries_gdf['NAME'].values.tolist()
country_names.remove('United States of America')
country_names.append('USA')
country_names.sort()
country_names = [name.replace('.', '').replace(' ', '_')
                 for name in country_names]

state_names = states_gdf['name'].values.tolist()

basemaps = list(geemap.basemaps)

Map = geemap.Map()

with col2:

    basemap = st.selectbox("Select a basemap", basemaps,
                           index=basemaps.index('HYBRID'))
    Map.add_basemap(basemap)

    country = st.selectbox('Select a country', country_names,
                           index=country_names.index('USA'))
    fc = None
    
    if country == 'USA':
        state = st.selectbox('Select a state', state_names,
                             index=state_names.index('Florida'))
        layer_name = state

        try:
            fc = ee.FeatureCollection(
                f'projects/sat-io/open-datasets/MSBuildings/US/{state}')
        except:
            st.error('No data available for the selected state.')

    else:
        try:
            fc = ee.FeatureCollection(
                f'projects/sat-io/open-datasets/MSBuildings/{country}')
        except:
            st.error('No data available for the selected country.')

        layer_name = country


    color = st.color_picker('Select a color', '#FF5500')

    style = {'fillColor': '00000000', 'color': color}

    split = st.checkbox("Split-panel map")

    if fc is not None:  # Check if fc is not None before adding the layer
        if split:
            left = geemap.ee_tile_layer(fc.style(**style), {}, 'Left')
            right = left
            Map.split_map(left, right)
        else:
            Map.addLayer(fc.style(**style), {}, layer_name)

        Map.centerObject(fc.first(), zoom=16)

    with st.expander("Data Sources"):
        st.info(
            """
            [Microsoft Building Footprints](https://gee-community-catalog.org/projects/msbuildings/)
            """
        )


with col1:

    Map.to_streamlit(height=1000)
