import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

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

    st.sidebar.title("Contact")
    st.sidebar.info(
        """
        Chancee Vincent:
        [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6)
        """
    )

    st.title("Heatmap")

    with st.expander("See source code"):
        with st.echo():
            filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
            m = leafmap.Map(center=[40, -100], zoom=4, tiles="stamentoner")
            m.add_heatmap(
                filepath,
                latitude="latitude",
                longitude="longitude",
                value="pop_max",
                name="Heat map",
                radius=20,
            )
    m.to_streamlit(height=700)
