import streamlit as st
import time
from io import BytesIO

# --- ERROR HANDLING FOR gTTS (Safety First) ---
try:
    from gtts import gTTS
except ImportError:
    import os
    os.system("pip install gTTS")
    from gtts import gTTS

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Dhruva's Ecosystem", layout="wide", page_icon="🎧")

# --- SPOTIFY THEME CSS (THE MAGIC) ---
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #121212;
        color: white;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 1px solid #282828;
    }
    
    /* Neon Green Buttons */
    .stButton>button {
        background-color: #1DB954;
        color: white;
        border-radius: 50px;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1ed760;
        transform: scale(1.05);
        box-shadow: 0 0 10px #1DB954;
    }

    /* Progress Bar */
    .stProgress > div > div > div > div {
        background-color: #1DB954;
    }

    /* Cards (Containers) */
    .css-1r6slb0 {
        background-color: #181818;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* Headers */
    h1, h2, h3 {
        color: white !important;
        font-family: 'Circular', sans-serif;
    }
    p {
        color: #b3b3b3;
    }
    
    /* Input Fields */
    .stTextInput>div>div>input {
        background-color: #282828;
        color: white;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'level_lib' not in st.session_state: st.session_state.level_lib = 1
if 'level_eng' not in st.session_state: st.session_state.level_eng = 1

# --- HELPER FUNCTIONS ---
def speak(text):
    sound = BytesIO()
    tts = gTTS(text, lang='hi', slow=False)
    tts.write_to_fp(sound)
    st.audio(sound)

def english_speak(text):
    sound = BytesIO()
    tts = gTTS(text, lang='en', slow=False)
    tts.write_to_fp(sound)
    st.audio(sound)

# --- SIDEBAR (NAVIGATION) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/2048px-Spotify_logo_without_text.svg.png", width=50)
    st.title("Dhruva OS")
    st.caption("Premium Learning Hub")
    
    st.write("---")
    
    menu = st.radio("NAVIAGTION", 
        ["🏠 Home", "🗣️ Communication", "📚 Library Sci", "📈 Marketing"],
        index=0)
    
    st.write("---")
    st.write("YOUR PROGRESS")
    st.write("Lib Sci")
    st.progress(st.session_state.level_lib * 25)
    st.write("English")
    st.progress(st.session_state.level_eng * 20)

# --- HOME PAGE ---
if menu == "🏠 Home":
    st.title("Good Evening, Dhruva")
    st.subheader("Jump back in")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="background-color: #181818; padding: 20px; border-radius: 10px;">
            <h3>📚 Library Science</h3>
            <p>Resume from Level 1</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="background-color: #181818; padding: 20px; border-radius: 10px;">
            <h3>🗣️ English Lab</h3>
            <p>Practice Daily Speak</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="background-color: #181818; padding: 20px; border-radius: 10px;">
            <h3>📈 Brand Stats</h3>
            <p>Check Growth</p>
        </div>
        """, unsafe_allow_html=True)

# --- COMMUNICATION MODULE ---
elif menu == "🗣️ Communication":
    st.title("Communication Mix")
    st.caption("Playlist for your tongue")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Now Playing: Grammar Basics")
        st.video("https://www.youtube.com/watch?v=Fj-yZJg4bKw")
    
    with col2:
        st.markdown("### 🎧 AI Trainer")
        st.info("Tap play to listen to the accent.")
        if st.button("▶️ Play Lesson"):
            english_speak("I am building a global system. I am confident.")
            st.success("Playing...")
        
        st.write("---")
        st.write("Test your skills:")
        q = st.selectbox("Complete: I ___ a CEO.", ["is", "am", "are"])
        if st.button("Check Answer"):
            if q == "am":
                st.balloons()
                st.success("Perfect! Level Up!")
            else:
                st.error("Try again.")

# --- LIBRARY SCIENCE MODULE ---
elif menu == "📚 Library Sci":
    st.title("Library Automation Hits")
    
    with st.expander("💿 Track 1: Data Entry", expanded=True):
        st.write("Add your first book record")
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Book Title", placeholder="e.g. Atomic Habits")
        with c2:
            st.text_input("Author", placeholder="e.g. James Clear")
        
        if st.button("Save to Database"):
            st.success("Added to library!")

# --- MARKETING MODULE ---
elif menu == "📈 Marketing":
    st.title("Viral Charts")
    st.metric(label="Profile Views", value="10.5K", delta="12%")
    st.video("https://www.youtube.com/watch?v=nLdWqjE2Ew0")
