import streamlit as st
import time
import base64
from chatbot import ask_bot

st.set_page_config(page_title="askVIT", page_icon="🎓", layout="wide", initial_sidebar_state="expanded")

# ---------- PAGE STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- LOAD ROBOT IMAGE ----------
with open("robot.png", "rb") as f:
    encoded_img = base64.b64encode(f.read()).decode()

# ---------- HOME PAGE ----------
def show_home():
    st.markdown(f"""
    <style>
    .home-container {{
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: linear-gradient(135deg, #E8EEF5, #D6E0EC);
    }}

    .bounce-img {{
        width: 260px;
        animation: bounce 2s infinite;
    }}

    @keyframes bounce {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-25px); }}
    }}

    .tagline {{
        font-size: 28px;
        font-weight: 800;
        margin-top: 20px;
        color: #1F2933;
    }}

    .start-btn button {{
        margin-top: 35px;
        font-size: 20px !important;
        padding: 14px 36px !important;
        border-radius: 16px !important;
        background: linear-gradient(135deg, #5B7C99, #3E5C76) !important;
        color: white !important;
        border: none !important;
    }}
    </style>

    <div class="home-container">
        <img src="data:image/png;base64,{encoded_img}" class="bounce-img">
        <div class="tagline">Your VIT companion forever</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='start-btn'>", unsafe_allow_html=True)
    if st.button("Start Chat"):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)
        st.session_state.page = "chat"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ---------- CHAT PAGE ----------
def show_chat():
    st.markdown("""
    <style>

    /* SAFE: hide bar but keep sidebar toggle */
    header {visibility: hidden !important;}

    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&display=swap');
    * { font-family: 'Merriweather', serif !important; }

    .stApp {
        background: linear-gradient(135deg, #E8EEF5, #D6E0EC);
        color: #1F2933;
        font-size: 18px;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #4B5D4B, #3E4C3E) !important;
    }

    .profile-img {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        display: block;
        margin: auto;
    }

    .history-title {
        color: white;
        font-size: 24px;
        font-weight: 900;
        margin: 25px 0 15px 20px;
    }

    .history-text {
        color: #E5E7EB;
        font-size: 15px;
        margin-left: 22px;
        margin-bottom: 10px;
    }

    div[data-testid="stHorizontalBlock"] button {
        height: 52px !important;
        width: 100% !important;
        font-size: 17px !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        background: linear-gradient(135deg, #5B7C99, #3E5C76) !important;
        color: white !important;
        border: none !important;
    }

    .suggest-btn button {
        width: 100% !important;
        background: linear-gradient(135deg, #1F2933, #374151) !important;
        color: #E5E7EB !important;
        border-radius: 14px !important;
        border: none !important;
    }

    textarea {
        border-radius: 28px !important;
        font-size: 18px !important;
        border: 2px solid #5B7C99 !important;
        background-color: #F8FBFF !important;
    }

    .stTextArea label {
        background: none !important;
        padding: 0 !important;
        margin-bottom: 10px !important;
    }

    .stTextArea label p {
        font-size: 22px !important;
        font-weight: 800 !important;
        margin-left: 5px;
    }

    .answer-box {
        background: white;
        padding: 35px;
        border-radius: 18px;
        border-left: 8px solid #5B7C99;
        font-size: 19px;
        line-height: 1.7;
        margin-top: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    }
    </style>
    """, unsafe_allow_html=True)

    if "history" not in st.session_state:
        st.session_state.history = []
    if "current_q" not in st.session_state:
        st.session_state.current_q = ""
    if "current_a" not in st.session_state:
        st.session_state.current_a = ""

    with st.sidebar:
        st.markdown("""
        <img src="https://th.bing.com/th/id/OIP.uefA2dCEfm6ab9Jv3HugRwHaEc?w=279&h=180&c=7&r=0&o=7&dpr=1.5&pid=1.7&rm=3" class="profile-img">
        <h3 style="color:white;text-align:center;font-size:26px;">VIT Assistant</h3>
        <p style="color:white;text-align:center;font-size:18px;">Academic AI Guide</p>
        <div class="history-title">&nbsp;&nbsp;&nbsp;&nbsp;Query History</div>
        """, unsafe_allow_html=True)

        for q, a in reversed(st.session_state.history):
            st.markdown(f"<div class='history-text'>• {q}</div>", unsafe_allow_html=True)

    main_col, right_col = st.columns([0.75, 0.25])

    with main_col:
        st.markdown("<h1 style='font-size:4.4rem;font-weight:900;'>🎓 askVIT</h1>", unsafe_allow_html=True)
        st.subheader("           Advanced RAG Support for Vellore Institute of Technology")

        query = st.text_area(
            "Hey! What is your question today?",
            value=st.session_state.current_q,
            height=280
        )

        col1, col2, spacer, col3 = st.columns([1,1,3,1])

        with col1:
            if st.button("Ask Bot"):
                answer = ask_bot(query)
                st.session_state.current_a = answer
                st.session_state.history.append((query, answer))

        with col2:
            if st.button("Next Question"):
                st.session_state.current_q = ""
                st.session_state.current_a = ""

        with col3:
            if st.button("📋"):
                st.code(query)

        if st.session_state.current_a:
            st.markdown(
                f"<div class='answer-box'><b>Official Guidance</b><br><br>{st.session_state.current_a}</div>",
                unsafe_allow_html=True
            )

    with right_col:
        st.markdown(
            "<div style='font-size:28px;font-weight:900;text-align:center; margin-top:40px; margin-bottom:10%;'>💡 Suggested Questions</div>",
            unsafe_allow_html=True
        )

        empty, content = st.columns([1,4])
        with content:
            for s in [
                "What is FFCS?",
                "Minimum attendance policy?",
                "How does CDC placement work?",
                "Hostel rules for girls?",
                "How many credits to graduate?",
                "What is grading system?"
            ]:
                if st.button(s, key=s):
                    st.session_state.current_q = s
                    st.rerun()


# ---------- ROUTER ----------
if st.session_state.page == "home":
    show_home()
else:
    show_chat()
