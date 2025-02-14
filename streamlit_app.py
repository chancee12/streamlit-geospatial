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
    st.markdown(
    """
    <style>
    body {
    background-image: url("https://media.giphy.com/media/BW51OCstarPBm/giphy.gif");
    background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)


    st.sidebar.title("Contact")
    st.sidebar.info(
        """
        Chancee Vincent:
        [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6)
    
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
    st.title("Chancee's AI and GIS Integrated Applications")

    st.markdown(
        """
        Welcome to this unique platform combining the power of AI and Geospatial technologies. Featuring interactive web apps that leverage 
        [openai](https://openai.com)'s GPT-3 model, [streamlit](https://streamlit.io) for web deployment, and an array of open-source mapping libraries like 
        [leafmap](https://leafmap.org), [geemap](https://geemap.org), [pydeck](https://deckgl.readthedocs.io), and [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter).
        For questions ask Chancee.
        """
    )

    st.markdown(
        """
        The applications range from AI-assisted text generation to geospatial data visualization and manipulation.
        Continuously exploring ways to expand AI integration beyond the realm of Natural Language Processing into the exciting field of GIS. 
        Stay tuned for more innovative integrations!
        """
    )

    st.info("To navigate to different applications, click on the options in the left sidebar menu.")


    row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)
    with row1_col1:
        st.markdown('![](https://media.giphy.com/media/tkQbZfMb4686Kht2Ds/giphy.gif)')
    with row1_col2:
        st.markdown('![](https://media.giphy.com/media/aBBVebadA4Z4c4wDc8/giphy.gif)')
    with row1_col3:
        st.markdown('![](https://media.giphy.com/media/ITRemFlr5tS39AzQUL/giphy.gif)')
    with row1_col4:
        st.markdown('<iframe src="https://giphy.com/embed/0lGd2OXXHe4tFhb7Wh" width="480" height="480" frameBorder="0" allowFullScreen></iframe>', unsafe_allow_html=True)

    row2_col1, row2_col2, row2_col3, row2_col4 = st.columns(4)
    with row2_col1:
        st.markdown('![](https://media.giphy.com/media/AIl5hsiqF7Tb1uaMpE/giphy.gif)')
    with row2_col2:
        st.markdown('![](https://media.giphy.com/media/l4pTsNgkamxfk2ZLq/giphy.gif)')
    with row2_col3:
        st.markdown('![](https://media.giphy.com/media/QL8RF2CdcuK1YzkWqm/giphy.gif)')
    with row2_col4:
        st.markdown('![](https://media.giphy.com/media/BT6RWMRXKSxLYS8B7G/giphy.gif)')

        
