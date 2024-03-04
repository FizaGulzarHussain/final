import streamlit as st



st.markdown("""
  <style>
    /* Adjusting the height of the chatbot */
    .flowise-chatbot {
        height: 600px; /* Increase this value as needed */
    }

    /* Moving the chatbot to the bottom right */
    .flowise-chatbot {
        position: fixed;
        bottom: 20px;
        right: 20px;
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

st.markdown(
    '<iframe title="dashboard" width="850" height="900" src="https://app.powerbi.com/view?r=eyJrIjoiZGE5Y2FlNWUtOGY2OS00MzZiLWFlOWUtMWFmMTQ3MzU5ZmRiIiwidCI6ImU4ZGExZWZhLWNiNjctNDI0MS1iMjhlLTAyY2NkN2E2NDc1NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>',
    unsafe_allow_html=True)

# Add the JavaScript code as a string
javascript_code = """
<script type="module">
    import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
    Chatbot.init({
        chatflowid: "4e572b6b-4507-4594-bda9-283e7e21be5a",
        apiHost: "http://localhost:3000",
    })
</script>
"""

# Display the JavaScript code in the Streamlit app
st.components.v1.html(javascript_code)
