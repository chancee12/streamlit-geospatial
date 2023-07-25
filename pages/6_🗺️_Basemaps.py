import streamlit as st
import leafmap.foliumap as leafmap

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
    def app():
        st.title("Search Basemaps")
        st.markdown(
            """
        This app is a demonstration of searching and loading basemaps from [xyzservices](https://github.com/geopandas/xyzservices) and [Quick Map Services (QMS)](https://github.com/nextgis/quickmapservices). Selecting from 1000+ basemaps with a few clicks.  
        """
        )

        with st.expander("See demo"):
            st.image("https://i.imgur.com/0SkUhZh.gif")

        row1_col1, row1_col2 = st.columns([3, 1])
        width = 800
        height = 600
        tiles = None

        with row1_col2:

            checkbox = st.checkbox("Search Quick Map Services (QMS)")
            keyword = st.text_input("Enter a keyword to search and press Enter:")
            empty = st.empty()

            if keyword:
                options = leafmap.search_xyz_services(keyword=keyword)
                if checkbox:
                    qms = leafmap.search_qms(keyword=keyword)
                    if qms is not None:
                        options = options + qms

                tiles = empty.multiselect(
                    "Select XYZ tiles to add to the map:", options)

            with row1_col1:
                m = leafmap.Map()

                if tiles is not None:
                    for tile in tiles:
                        m.add_xyz_service(tile)

                m.to_streamlit(height=height)


    app()
