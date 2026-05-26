# utils/styles.py

def load_css():

    return """
    <style>

    .stApp {
        background: radial-gradient(circle at center, #001a4d 0%, #000428 100%);
        color: white;
    }

    /* TITLE */

    h1 {
        text-align: center;
        color: white;
        font-size: 55px !important;
        font-weight: bold;
    }

    h2, h3 {
        text-align: center;
        color: white;
    }

    /* TIMER */

    .timer {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        color: #ffcc00;
        margin-bottom: 30px;
        animation: pulse 1s infinite;
    }

    @keyframes pulse {

        0% {
            transform: scale(1);
        }

        50% {
            transform: scale(1.1);
        }

        100% {
            transform: scale(1);
        }
    }

    /* QUESTION BOX */

    .question-box {

        background: linear-gradient(
            180deg,
            #102c70,
            #061640
        );

        padding: 25px;

        border-radius: 20px;

        text-align: center;

        font-size: 32px;

        font-weight: bold;

        border: 3px solid #4da6ff;

        margin-bottom: 40px;

        box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
    }

    /* OPTION BUTTON */

    div.stButton > button {

        background: linear-gradient(
            180deg,
            #111827,
            #000000
        ) !important;

        color: white !important;

        border: 2px solid #4da6ff !important;

        border-radius: 40px !important;

        height: 75px !important;

        font-size: 22px !important;

        font-weight: bold !important;

        margin-top: 15px;

        transition: all 0.3s ease-in-out;

        box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
    }

    /* HOVER */

    div.stButton > button:hover {

        border: 2px solid #ffcc00 !important;

        color: #ffcc00 !important;

        transform: scale(1.03);
    }

    /* SELECTED BUTTON */

    div.stButton > button:disabled {

        background: linear-gradient(
            180deg,
            #ffcc00,
            #ff9900
        ) !important;

        color: black !important;

        border: 2px solid white !important;

        opacity: 1 !important;
    }

    /* SELECTED ORDER */

    .selected-order {

        background: rgba(255,255,255,0.08);

        padding: 20px;

        border-radius: 20px;

        border: 2px solid #4da6ff;

        margin-top: 30px;
    }

    .circle-box {

    width: 70px;
    height: 70px;

    border-radius: 50%;

    border: 3px solid #33aaff;

    display: flex;

    justify-content: center;

    align-items: center;

    font-size: 28px;

    font-weight: bold;

    color: white;

    margin: auto;

    background: radial-gradient(
        circle,
        #0b1f4d,
        #000000
    );

    box-shadow: 0px 0px 15px rgba(0,0,0,0.5);
}
    </style>
    """