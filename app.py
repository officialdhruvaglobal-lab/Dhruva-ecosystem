import streamlit as st
from gtts import gTTS
from io import BytesIO
import time

st.set_page_config(page_title="Dhruva's Career OS", layout="wide", page_icon="🚀")

if 'level_lib' not in st.session_state: st.session_state.level_lib = 1
if 'level_eng' not in st.session_state: st.session_state.level_eng = 1

st.markdown("""
<style>
    .stProgress .st-bo {background-color: #00ff00;}
    .success-msg {padding: 10px; background-color: #d1e7dd; color: #0f5132; border-radius: 5px;}
</style>
""", unsafe_allow_html=True)

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

with st.sidebar:
    st.title("👤 User: Dhruva")
    st.write("Status: **Training Mode**")
    st.write("---")
    st.write("📚 Library Sci: Level " + str(st.session_state.level_lib))
    st.progress(st.session_state.level_lib * 25)
    st.write("🗣️ English: Level " + str(st.session_state.level_eng))
    st.progress(st.session_state.level_eng * 20)

st.title("🎓 Atmanirbhar Learning System (v3.0)")
st.caption("Designed for Rural to Global Transformation")

module = st.selectbox("Select Module:", 
    ["🗣️ Communication (The Bridge)", "📚 Library Science (The Core)", "📈 Digital Marketing"])

if module == "🗣️ Communication (The Bridge)":
    st.header("🗣️ Desi to Global: Communication Lab")
    with st.expander("🟢 Level 1: Grammar (Basic)", expanded=True):
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("#### 📺 Concept: Is/Am/Are")
            st.video("https://www.youtube.com/watch?v=Fj-yZJg4bKw") 
        with col2:
            st.markdown("#### 🎧 Podcast: Sakhi")
            if st.button("Play Lesson"):
                speak("Namaste Dhruva. English mein 'Main hoon' ko 'I am' kehte hain. Ab suniye.")
                time.sleep(1)
                english_speak("I am a Librarian. I am confident.")
            
            st.markdown("---")
            q1 = st.radio("Correct Sentence:", ["I is going.", "I am going.", "I are going."])
            if st.button("Submit Answer"):
                if q1 == "I am going.":
                    st.balloons()
                    st.success("Correct! Level 2 Unlocked!")
                    st.session_state.level_eng = 2
                else:
                    st.error("Try Again.")

elif module == "📚 Library Science (The Core)":
    st.header("📚 Library Science: Zero to Job")
    with st.expander("🟢 Level 1: Excel Data Entry", expanded=True):
        st.write("Task: 5 Kitabon ka data entry karein.")
        t = st.text_input("Book Title")
        a = st.text_input("Author")
        if st.button("Save Data"):
            if t and a:
                st.success(f"Saved: {t} by {a}")
                st.info("Great! You are ready for Level 2.")
                st.session_state.level_lib = 2

elif module == "📈 Digital Marketing":
    st.header("📈 Brand Dhruva Dashboard")
    st.video("https://www.youtube.com/watch?v=nLdWqjE2Ew0")
    st.write("Task: Create your first post on Canva today.")

st.markdown("---")
st.caption("Powered by Unit B")
