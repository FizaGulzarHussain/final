import streamlit as st


st.markdown("""
  <style>
    .css-o18uir.e16nr0p33 {
      margin-top: -75px;
    }
  </style>
""", unsafe_allow_html=True)

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background: url(https://i.ibb.co/H2sSCfC/AI-Greener.png);
                background-repeat: no-repeat;
                padding-top
                : 120px;
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




st.markdown('<p style="color:#008000; font-size:50px;">Green Initiative Dashboard</p>', unsafe_allow_html=True)



st.markdown('<iframe title="dashboard" width="850" height="900" src="https://app.powerbi.com/view?r=eyJrIjoiZGE5Y2FlNWUtOGY2OS00MzZiLWFlOWUtMWFmMTQ3MzU5ZmRiIiwidCI6ImU4ZGExZWZhLWNiNjctNDI0MS1iMjhlLTAyY2NkN2E2NDc1NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>',  unsafe_allow_html=True)