import streamlit as st
import random
import time

from data.questions import fff_questions
from assets.sounds.sound import play_sound


def show():

    st.title("🏆 RESULT")

    # =====================================
    # DATA
    # =====================================

    question = st.session_state.current_question

    correct_order = question["correct_order"]

    user_order = st.session_state.user_order

    # =====================================
    # RESULT CHECK
    # =====================================

    if user_order == correct_order:

        play_sound(
            "assets/sounds/correct.mpeg"
        )

        st.success("🎉 Correct Order")

    else:

        play_sound(
            "assets/sounds/wrong.mpeg"
        )

        st.error("❌ Wrong Answer")

        st.markdown(
            "## ✅ Correct Order"
        )

        for i, item in enumerate(
            correct_order,
            start=1
        ):

            st.write(
                f"{i}. {item}"
            )

    # =====================================
    # USER ANSWER
    # =====================================

    st.write("")

    st.markdown(
        "## 🧠 Your Answer"
    )

    if len(user_order) == 0:

        st.error(
            "❌ No Answer Submitted"
        )

    else:

        for i, item in enumerate(
            user_order,
            start=1
        ):

            st.write(
                f"{i}. {item}"
            )

    # =====================================
    # SPACE
    # =====================================

    st.write("")
    st.write("")
    st.write("")

    # =====================================
    # BUTTONS
    # =====================================

    col1, col2 = st.columns(2)

    # =====================================
    # PLAY AGAIN
    # =====================================

    with col1:

        if st.button(
            "🔄 PLAY AGAIN",
            use_container_width=True,
            key="play_again_btn"
        ):

            st.session_state.page = "landing"

            st.session_state.selected_order = []

            st.session_state.selected_labels = []

            st.session_state.user_order = []

            st.session_state.start_time = time.time()

            st.rerun()

    # =====================================
    # NEXT QUESTION
    # =====================================

    with col2:

        if st.button(
            "➡ NEXT QUESTION",
            use_container_width=True,
            key="next_question_btn"
        ):

            available_questions = [

                q for q in fff_questions

                if q != st.session_state.current_question
            ]

            st.session_state.current_question = (
                random.choice(available_questions)
            )

            # RESET

            st.session_state.selected_order = []

            st.session_state.selected_labels = []

            st.session_state.user_order = []

            st.session_state.start_time = time.time()

            # OPEN GAME PAGE

            st.session_state.page = "game"

            st.rerun()

