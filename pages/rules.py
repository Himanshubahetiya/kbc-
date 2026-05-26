import streamlit as st
import time

def show():
    # 1. Premium CSS Theme for KBC Rules Screen
    st.markdown("""
        <style>
        /* Deep Studio Background */
        .stApp {
            background: radial-gradient(circle at center, #0a0935 0%, #03021a 100%);
            color: #ffffff;
            font-family: 'Inter', sans-serif;
        }
        
        .kbc-center {
            text-align: center;
        }
        
        /* Modernized Golden Title */
        .rules-title {
            font-family: 'Cinzel', 'Georgia', serif;
            font-size: 2.8rem;
            font-weight: 900;
            letter-spacing: 3px;
            background: linear-gradient(180deg, #FFF7C2 0%, #FFD700 40%, #B8860B 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0px 4px 6px rgba(0,0,0,0.6));
            margin-bottom: 5px;
        }

        .rules-subtitle {
            color: #00E5FF;
            font-size: 1rem;
            letter-spacing: 4px;
            text-transform: uppercase;
            font-weight: 700;
            margin-bottom: 40px;
            text-shadow: 0 0 8px rgba(0, 229, 255, 0.3);
        }

        /* Rule Card Wrapper */
        .rule-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(0, 229, 255, 0.2);
            border-radius: 12px;
            padding: 20px 25px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            box-shadow: inset 0 0 15px rgba(0, 229, 255, 0.05);
            transition: transform 0.2s ease;
        }
        
        .rule-card:hover {
            transform: translateX(5px);
            border-color: rgba(255, 215, 0, 0.4);
            background: rgba(255, 215, 0, 0.02);
        }

        /* Number Badge Style */
        .rule-number {
            font-size: 1.5rem;
            font-weight: 800;
            color: #00E5FF;
            background: rgba(0, 229, 255, 0.1);
            border: 1px solid #00E5FF;
            border-radius: 50%;
            width: 45px;
            height: 45px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 20px;
            flex-shrink: 0;
            box-shadow: 0 0 10px rgba(0, 229, 255, 0.2);
        }

        /* Rule Text Style */
        .rule-text {
            font-size: 1.15rem;
            color: #e0e0e0;
            line-height: 1.4;
            font-weight: 500;
        }
        
        .rule-highlight {
            color: #FFD700;
            font-weight: 700;
        }

        /* Custom Hotseat Button Theme */
        div.stButton > button:first-child {
            background: linear-gradient(90deg, #100e4a 0%, #1a1773 50%, #100e4a 100%) !important;
            color: #FFD700 !important;
            font-size: 1.25rem !important;
            font-weight: 700 !important;
            letter-spacing: 2px !important;
            border: 2px solid #FFD700 !important;
            border-radius: 30px !important;
            padding: 12px 0px !important;
            box-shadow: 0 0 15px rgba(255, 215, 0, 0.2) !important;
            transition: all 0.3s ease !important;
            margin-top: 20px;
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

    # 2. Centered Layout Structure
    col_b1, col_main, col_b2 = st.columns([1, 8, 1])
    
    with col_main:
        # Headers
        st.markdown('<h1 class="rules-title kbc-center">नियमावली (RULES)</h1>', unsafe_allow_html=True)
        st.markdown('<p class="rules-subtitle kbc-center">⚡ FASTEST FINGER FIRST ROUND ⚡</p>', unsafe_allow_html=True)
        
        # 3. Interactive Rule Cards instead of normal bullet points
        st.markdown("""
            <div class="rule-card">
                <div class="rule-number">1</div>
                <div class="rule-text">Aapke paas answers arrange karne ke liye kul <span class="rule-highlight">20 Seconds</span> ka samay hoga.</div>
            </div>
            <div class="rule-card">
                <div class="rule-number">2</div>
                <div class="rule-text">Options ko di gayi <span class="rule-highlight">Sahi Chronological Order</span> (Correct Sequence) mein arrange karein.</div>
            </div>
            <div class="rule-card">
                <div class="rule-number">3</div>
                <div class="rule-text">Jo sabse kam samay mein sabse <span class="rule-highlight">Sahi Jawab</span> dega, wahi Hotseat par baithega!</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("") # Spacer
        
        # 4. Action Button Area
        c1, c2, c3 = st.columns([1.5, 2, 1.5])
        with c2:
            if st.button("START FFF ROUND", use_container_width=True):
                st.session_state.page = "game"
                st.session_state.start_time = time.time()
                st.rerun()