import streamlit as st
import base64


def play_sound(file_path):

    with open(file_path, "rb") as audio_file:

        audio_bytes = audio_file.read()

    encoded_audio = base64.b64encode(
        audio_bytes
    ).decode()

    audio_html = f"""
        <audio autoplay>
            <source
                src="data:audio/mpeg;base64,{encoded_audio}"
                type="audio/mpeg">
        </audio>
    """

    st.components.v1.html(
        audio_html,
        height=0
    )