import os
import leafmap.foliumap as leafmap
import leafmap.colormaps as cm
import streamlit as st

def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect")
        return False
    else:
        return True  # Password correct.

if check_password():
    st.set_page_config(layout="wide")

    st.sidebar.title("Contact")
    st.sidebar.info(
        """
        Chancee Vincent:
        [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6)
        """)

    @st.cache_data
    def load_cog_list():
        print(os.getcwd())
        in_txt = os.path.join(os.getcwd(), "data/cog_files.txt")
        with open(in_txt) as f:
            return [line.strip() for line in f.readlines()[1:]]

    @st.cache_data
    def get_palettes():
        return list(cm.palettes.keys())

    st.title("Raster Data Visualization")
    st.markdown(
        """
    An interactive web app for visualizing local raster datasets and Cloud Optimized GeoTIFF ([COG](https://www.cogeo.org)). The app was built using [streamlit](https://streamlit.io), [leafmap](https://leafmap.org), and [Titiler](https://developmentseed.org/titiler/).
        """)

    row1_col1, row1_col2 = st.columns([2, 1])

    with row1_col1:
        cog_list = load_cog_list()
        cog = st.selectbox("Select a sample Cloud Opitmized GeoTIFF (COG)", cog_list)

    with row1_col2:
        empty = st.empty()
        url = empty.text_input("Enter a HTTP URL to a Cloud Optimized GeoTIFF (COG)", cog)
        if url:
            try:
                options = leafmap.cog_bands(url)
            except Exception as e:
                st.error(e)
            default = options[:3] if len(options) > 3 else options[0]
            bands = st.multiselect("Select bands to display", options, default=options)

            if len(bands) not in [1, 3]:
                st.error("Please select one or three bands")

        add_params = st.checkbox("Add visualization parameters")
        vis_params = st.text_area("Enter visualization parameters", "{}") if add_params else {}

        if len(vis_params) > 0:
            try:
                vis_params = eval(vis_params)
            except Exception as e:
                st.error(f"Invalid visualization parameters. It should be a dictionary. Error: {e}")
                vis_params = {}

        submit = st.button("Submit")

    m = leafmap.Map(latlon_control=False)

    if submit:
        if url:
            try:
                m.add_cog_layer(url, bands=bands, **vis_params)
            except Exception as e:
                with row1_col2:
                    st.error(e)
                    st.error("Work in progress. Try it again later.")

    with row1_col1:
        m.to_streamlit()
