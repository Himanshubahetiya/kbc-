import streamlit as st

def show():
    # 1. Premium & Immersive KBC UI Styling (Custom CSS)
    st.markdown("""
        <style>
        /* Overall Page Background - Deep Studio Blue Gradient */
        .stApp {
            background: radial-gradient(circle at center, #0a0935 0%, #03021a 100%);
            color: #ffffff;
            font-family: 'Inter', sans-serif;
        }
        
        /* Center alignment utility */
        .kbc-center {
            text-align: center;
        }
        
        /* Hero Image Container to look like a premium broadcast screen */
        .image-container {
            border: 2px solid rgba(255, 215, 0, 0.3);
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 229, 255, 0.15), inset 0 0 20px rgba(255,255,255,0.1);
            margin-bottom: 30px;
        }
        
        /* 3D Metallic Gold Title */
        .kbc-main-title {
            font-family: 'Cinzel', 'Georgia', serif;
            font-size: 3.2rem;
            font-weight: 900;
            letter-spacing: 4px;
            background: linear-gradient(180deg, #FFF7C2 0%, #FFD700 40%, #B8860B 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0px 4px 8px rgba(0,0,0,0.5));
            margin-bottom: 2px;
        }

        /* Neon Lifeline Cyan Subtitle */
        .kbc-sub-title {
            color: #00E5FF;
            font-size: 1.1rem;
            letter-spacing: 6px;
            text-transform: uppercase;
            font-weight: 700;
            margin-bottom: 35px;
            text-shadow: 0 0 10px rgba(0, 229, 255, 0.4);
        }

        /* Signature KBC Hexagonal/Diamond Inspired Dialogue Box */
        .kbc-dialog-box {
            background: linear-gradient(90deg, rgba(0,229,255,0.03) 0%, rgba(255,215,0,0.06) 50%, rgba(0,229,255,0.03) 100%);
            border-top: 1.5px solid rgba(255, 215, 0, 0.4);
            border-bottom: 1.5px solid rgba(255, 215, 0, 0.4);
            border-left: 3px solid #00E5FF;
            border-right: 3px solid #00E5FF;
            border-radius: 25px;
            padding: 22px 30px;
            margin: 30px auto;
            max-width: 800px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        
        .kbc-dialog-text {
            font-size: 1.3rem;
            color: #f0f0f0;
            font-style: italic;
            font-weight: 500;
            letter-spacing: 0.5px;
            line-height: 1.5;
        }

        /* Custom styling for the primary action button to match KBC Hotseat Theme */
        div.stButton > button:first-child {
            background: linear-gradient(90deg, #100e4a 0%, #1a1773 50%, #100e4a 100%) !important;
            color: #FFD700 !important;
            font-size: 1.3rem !important;
            font-weight: 700 !important;
            letter-spacing: 2px !important;
            border: 2px solid #FFD700 !important;
            border-radius: 30px !important;
            padding: 12px 0px !important;
            box-shadow: 0 0 15px rgba(255, 215, 0, 0.2) !important;
            transition: all 0.3s ease !important;
        }

        div.stButton > button:first-child:hover {
            background: linear-gradient(90deg, #FFD700 0%, #FFA751 100%) !important;
            color: #03021a !important;
            box-shadow: 0 0 25px rgba(255, 215, 0, 0.6) !important;
            border-color: #ffffff !important;
            transform: scale(1.02);
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. Main Layout Centering Container
    col_blank1, col_main, col_blank2 = st.columns([1, 10, 1])
    
    with col_main:
        # 3. Cinematic Hero Banner Wrapper (Using web URL to prevent path errors)
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(
            "https://www.koimoi.com/wp-content/new-galleries/2022/07/kbc-director-reveals-format-changes-talks-about-joys-of-working-with-big-b-01.jpg",
            use_container_width=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

        # 4. Text Branding Headers
        st.markdown('<h1 class="kbc-main-title kbc-center">KAUN BANEGA CROREPATI</h1>', unsafe_allow_html=True)
        # st.markdown('<p class="kbc-sub-title kbc-center">⚡ FASTEST FINGER FIRST ⚡</p>', unsafe_allow_html=True)

        # 5. Amitabh Bachchan Signature Dialogue Box
        st.markdown("""
            <div class="kbc-dialog-box kbc-center">
                <p class="kbc-dialog-text">"Deviyon aur sajjano, taiyaar ho jaiye hotseat par baithne ke liye!"</p>
            </div>
        """, unsafe_allow_html=True)

        # 6. Centered Action Button Area
        c1, c2, c3 = st.columns([2, 2, 2])
        with c2:
            if st.button("START GAME", use_container_width=True):
                st.session_state.page = "rules"
                st.rerun()

        st.markdown("<br><p class='kbc-center' style='opacity:0.4; font-size:0.85rem; letter-spacing:1px;'>HEADPHONES RECOMMENDED FOR THE BEST EXPERIENCE</p>", unsafe_allow_html=True)