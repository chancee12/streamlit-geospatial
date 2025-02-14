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

    st.sidebar.title("Contact")
    st.sidebar.info(
        """
        Chancee Vincent:
        [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6)
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
