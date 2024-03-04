import streamlit as st
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background: url(https://i.ibb.co/6nRsDh1/133-konicaminolta.jpg);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()
st.markdown('<p style="color:#008000; font-size:50px;">Maintenance and Updates</p>', unsafe_allow_html=True)

# Custom CSS for styling
custom_css = """
    <style>
        .stApp {
            background-color:#F1ECDD; /* Set your desired background color */
            font-family: Arial, sans-serif; /* Set font family */
        }

    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)