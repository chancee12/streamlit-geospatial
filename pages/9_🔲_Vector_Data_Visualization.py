import os
import fiona
import geopandas as gpd
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
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():

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

    def save_uploaded_file(file_content, file_name):
        """
        Save the uploaded file to a temporary directory
        """
        import tempfile
        import os
        import uuid

        _, file_extension = os.path.splitext(file_name)
        file_id = str(uuid.uuid4())
        file_path = os.path.join(tempfile.gettempdir(), f"{file_id}{file_extension}")

        with open(file_path, "wb") as file:
            file.write(file_content.getbuffer())

        return file_path


    def app():

        st.title("Upload Vector Data")

        row1_col1, row1_col2 = st.columns([2, 1])
        width = 950
        height = 600

        with row1_col2:

            backend = st.selectbox(
                "Select a plotting backend", ["folium", "kepler.gl", "pydeck"], index=2
            )

            if backend == "folium":
                import leafmap.foliumap as leafmap
            elif backend == "kepler.gl":
                import leafmap.kepler as leafmap
            elif backend == "pydeck":
                import leafmap.deck as leafmap

            url = st.text_input(
                "Enter a URL to a vector dataset",
                "https://github.com/giswqs/streamlit-geospatial/raw/master/data/us_states.geojson",
            )

            data = st.file_uploader(
                "Upload a vector dataset", type=["geojson", "kml", "zip", "tab"]
            )

            container = st.container()

            if data or url:
                if data:
                    file_path = save_uploaded_file(data, data.name)
                    layer_name = os.path.splitext(data.name)[0]
                elif url:
                    file_path = url
                    layer_name = url.split("/")[-1].split(".")[0]

                with row1_col1:
                    if file_path.lower().endswith(".kml"):
                        fiona.drvsupport.supported_drivers["KML"] = "rw"
                        gdf = gpd.read_file(file_path, driver="KML")
                    else:
                        gdf = gpd.read_file(file_path)
                    lon, lat = leafmap.gdf_centroid(gdf)
                    if backend == "pydeck":

                        column_names = gdf.columns.values.tolist()
                        random_column = None
                        with container:
                            random_color = st.checkbox("Apply random colors", True)
                            if random_color:
                                random_column = st.selectbox(
                                    "Select a column to apply random colors", column_names
                                )

                        m = leafmap.Map(center=(lat, lon))
                        m.add_gdf(gdf, random_color_column=random_column)
                        st.pydeck_chart(m)

                    else:
                        m = leafmap.Map(center=(lat, lon), draw_export=True)
                        m.add_gdf(gdf, layer_name=layer_name)
                        # m.add_vector(file_path, layer_name=layer_name)
                        if backend == "folium":
                            m.zoom_to_gdf(gdf)
                        m.to_streamlit(width=width, height=height)

            else:
                with row1_col1:
                    m = leafmap.Map()
                    st.pydeck_chart(m)


    app()
