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

    st.title("Split-panel Map")

    with st.expander("See source code"):
        with st.echo():
            m = leafmap.Map()
            m.split_map(
                left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover 2020'
            )
            m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

    m.to_streamlit(height=700)
