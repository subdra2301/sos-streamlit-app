import streamlit as st

# Page settings
st.set_page_config(
    page_title="SOS Button",
    page_icon="🚨",
    layout="centered"
)

# Center the button using CSS
st.markdown("""
<style>
.big-sos-button button {
    background-color: red;
    color: white;
    font-size: 40px;
    font-weight: bold;
    height: 200px;
    width: 200px;
    border-radius: 100px;
}
</style>
""", unsafe_allow_html=True)

st.title("🚨 Emergency SOS")

st.write("Press only in case of emergency")

st.divider()

# Big SOS button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("SOS", key="sos", help="Send emergency alert"):
        st.error("🚨 SOS ACTIVATED")
        st.warning("Contact emergency services immediately (112)")
