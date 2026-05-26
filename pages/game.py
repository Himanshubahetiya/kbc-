import streamlit as st
import time
from assets.sounds.sound import play_sound

def show():

    st.title("⚡ Fastest Finger First")

    # =====================================
    # CURRENT QUESTION
    # =====================================

    question = st.session_state.current_question

    # =====================================
    # TIMER
    # =====================================

    elapsed = int(
        time.time() - st.session_state.start_time
    )

    remaining = max(0, 20 - elapsed)

    # =====================================
    # TIME UP
    # =====================================

    if remaining <= 0:

        st.session_state.user_order = []

        st.session_state.page = "result"

        st.rerun()

    # =====================================
    # TIMER UI
    # =====================================

    st.markdown(
        f"""
        <div class="timer">
            ⏳ {remaining} sec
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================
    # QUESTION BOX
    # =====================================

    st.markdown(
        f"""
        <div class="question-box">
            {question["question"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================
    # OPTIONS
    # =====================================

    options = question["options"]

    labels = ["A", "B", "C", "D"]

    for index, option in enumerate(options):

        already_selected = (
            option in st.session_state.selected_order
        )

        label = labels[index]

        button_text = (
            f"{label}. {option}"
        )

        if already_selected:

            button_text = (
                f"✅ {label}. {option}"
            )

        if st.button(
            button_text,
            disabled=already_selected,
            use_container_width=True,
            key=f"option_{index}"
        ):

            st.session_state.selected_order.append(
                option
            )

            st.session_state.selected_labels.append(
                label
            )

            st.rerun()

    # =====================================
    # SPACE
    # =====================================

    st.write("")
    st.write("")

    # =====================================
    # BOTTOM SECTION
    # =====================================

    bottom_cols = st.columns(
        [2, 1, 1, 1, 1, 2]
    )

    # =====================================
    # CLEAR BUTTON
    # =====================================

    with bottom_cols[0]:

        if st.button(
            "❌ CLEAR",
            use_container_width=True,
            key="clear_button"
        ):

            st.session_state.selected_order = []

            st.session_state.selected_labels = []

            st.rerun()

    # =====================================
    # CIRCLE BOXES
    # =====================================

    for i in range(4):

        with bottom_cols[i + 1]:

            if i < len(
                st.session_state.selected_labels
            ):

                value = (
                    st.session_state.selected_labels[i]
                )

            else:

                value = "-"

            st.markdown(
                f"""
                <div class="circle-box">
                    {value}
                </div>
                """,
                unsafe_allow_html=True
            )

    # =====================================
    # SUBMIT BUTTON
    # =====================================

    with bottom_cols[5]:

        submit_disabled = (
            len(st.session_state.selected_order) != 4
        )

        if st.button(
            "SUBMIT ➜",
            use_container_width=True,
            disabled=submit_disabled,
            key="submit_button"
        ):

            st.session_state.user_order = (
                st.session_state.selected_order.copy()
            )

            st.session_state.page = "result"

            st.rerun()

    # =====================================
    # AUTO REFRESH TIMER
    # =====================================

    time.sleep(1)

    st.rerun()