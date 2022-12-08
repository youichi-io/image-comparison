import streamlit as st
from utils import image_comparison

with st.sidebar:
    st.set_page_config(
        page_title="Streamlit Image Comparison",
        page_icon="🔥",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.markdown(
        """
        <h2 style='text-align: center'>
        Streamlit Image Comparison Demo
        </h2>
        """,
        unsafe_allow_html=True,
    )

    st.write("##")

    with st.form(key="Streamlit Image Comparison"):
        # image one inputs
        img1_url = st.file_uploader("Image 1", accept_multiple_files=False)
        # image two inputs
        img2_url = st.file_uploader("Image 2", accept_multiple_files=False)
        
        # continious parameters
        col1, col2 = st.columns([1, 1])
        with col1:
            starting_position = st.slider(
                "Starting position of the slider:", min_value=0, max_value=100, value=50
            )
        with col2:
            width = st.slider(
                "Component width:", min_value=400, max_value=1000, value=700, step=100
            )
            
        # centered submit button
        col1, col2, col3 = st.columns([2, 6, 2])
        with col2:
            submit = st.form_submit_button("Update Render 🔥")

if img1_url is not None and img2_url is not None:
    static_component = image_comparison(
        img1=img1_url,
        img2=img2_url,
        width=width,
        starting_position=starting_position,
    )
