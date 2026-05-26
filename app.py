import streamlit as st
import random
import time

from utils.styles import load_css

from data.questions import fff_questions

from pages import (
    landing,
    rules,
    game,
    result
)

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="KBC Clone",
    layout="centered"
)

# =====================================
# LOAD CSS
# =====================================

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

# =====================================
# SESSION STATE
# =====================================

defaults = {

    "page": "landing",

    "selected_order": [],

    "selected_labels": [],

    "user_order": [],

    "start_time": time.time(),

    "current_question": random.choice(
        fff_questions
    )
}

for key, value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value

# =====================================
# MAIN PAGE CONTAINER
# =====================================

main_container = st.empty()

# =====================================
# ROUTING
# =====================================

with main_container.container():

    if st.session_state.page == "landing":

        landing.show()

    elif st.session_state.page == "rules":

        rules.show()

    elif st.session_state.page == "game":

        game.show()

    elif st.session_state.page == "result":

        result.show()