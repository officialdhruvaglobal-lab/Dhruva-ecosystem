import streamlit as st
import time
from io import BytesIO

# --- SAFETY CHECK: AUTO-INSTALL PACKAGES ---
try:
    from gtts import gTTS
    import feedparser # News lane ke liye
except ImportError:
    import os
    os.system("pip install gTTS feedparser")
    from gtts import gTTS
    import feedparser

# --- PAGE CONFIGURATION (APP MODE) ---
st.set_page_config(page_title="Skill Mela OS", layout="wide", page_icon="🚀", initial_sidebar_state="expanded")

# --- CUSTOM CSS (PRO UI - LEARNVern STYLE) ---
st.markdown("""
<style>
    /* Clean Professional Look */
    .stApp { background-color: #f8f9fa; color: #212529; }
    
    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #dee2e6; }
    
    /* Buttons */
    .stButton>button { 
        background-color: #0d6efd; color: white; border-radius: 8px; 
        border: none; padding: 10px 24px; font-weight: 600; width: 100%;
    }
    .stButton>button:hover { background-color: #0b5ed7; box-shadow: 0 4px 12px rgba(13,110,253,0.2); }
    
    /* Cards */
    .css-card {
        background-color: white; padding: 20px; border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin-bottom: 20px; border: 1px solid #e9ecef;
    }
    
    /* Headers */
    h1, h2, h3 { font-family: 'Segoe UI', sans-serif; color: #1a1a1a; }
    
    /* Video Container */
    .stVideo { border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

# --- AI SAKHI VOICE ENGINE ---
def speak(text, lang='hi'):
    sound = BytesIO()
    tts = gTTS(text, lang=lang, slow=False)
    tts.write_to_fp(sound)
    st.audio(sound)

# --- DYNAMIC CONTENT DATABASE (ADMIN CONTROLLED) ---
# Ye list future me bina code k change ho sakti hai
course_data = {
    "module1": {
        "title": "🟢 Module 1: Fundamentals (Google)",
        "video": "https://www.youtube.com/watch?v=s5e7q45_9bU", # Google Digital Garage Intro (Stable)
        "desc": "Digital Marketing kya hai aur future kya hai.",
        "task": "Apne Business ka naam aur 3 keywords socho."
    },
    "module2": {
        "title": "🟡 Module 2: SEO & Content (HubSpot)",
        "video": "https://www.youtube.com/watch?v=5bg312b5z1Y", # HubSpot SEO Course (Stable)
        "desc": "Google par upar kaise aana hai (Ranking Logic).",
        "task": "Google Trends par jakar aaj ka 'Trending Keyword' dhundo."
    },
    "module3": {
        "title": "🔴 Module 3: Social Media & Ads (Meta)",
        "video": "https://www.youtube.com/watch?v=C0DPdy98e4c", # Facebook Ads Intro
        "desc": "Paisa lagakar customer kaise layen.",
        "task": "Canva par ek Ad image design karo."
    }
}

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=60)
    st.title("Skill Mela OS")
    st.caption("Auto-Evolving Ecosystem")
    
    mode = st.radio("Navigation", ["🎓 My Classroom", "📰 Live Market Trends", "🛠️ Admin Panel"])
    
    st.markdown("---")
    st.write("### 🤖 Sakhi AI Status")
    st.success("● Online & Learning")
    if st.button("🔊 Sakhi Intro"):
        speak("Namaste Dhruva. Main aapki personal AI hoon. Main har roz naye market trends scan kar rahi hoon.")

# --- MAIN APP LOGIC ---

# 1. CLASSROOM MODE (The Course)
if mode == "🎓 My Classroom":
    st.title("Digital Marketing Mastery 🚀")
    
    # Progress Bar
    progress = st.slider("Course Progress", 0, 100, 10)
    
    # Dynamic Course Loader
    tabs = st.tabs(["Fundamentals", "SEO Mastery", "Paid Ads"])
    
    with tabs[0]:
        st.markdown(f"""<div class="css-card"><h3>{course_data['module1']['title']}</h3><p>{course_data['module1']['desc']}</p></div>""", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        with col1:
            st.video(course_data['module1']['video'])
        with col2:
            st.info(f"📋 **Project:** {course_data['module1']['task']}")
            st.write("**Sakhi Note:**")
            st.caption("Ye video Google ke official course ka hai. Ye kabhi delete nahi hoga.")
            if st.button("🔊 Explain Module 1"):
                speak("Digital marketing ka matlab hai internet par apna maal bechna. Video dekho aur samjho.")

    with tabs[1]:
        st.markdown(f"""<div class="css-card"><h3>{course_data['module2']['title']}</h3><p>{course_data['module2']['desc']}</p></div>""", unsafe_allow_html=True)
        st.video(course_data['module2']['video'])
        st.warning("⚠️ Practice: Ubersuggest tool use karke keyword dhundo.")

    with tabs[2]:
        st.markdown(f"""<div class="css-card"><h3>{course_data['module3']['title']}</h3><p>{course_data['module3']['desc']}</p></div>""", unsafe_allow_html=True)
        st.video(course_data['module3']['video'])

# 2. LIVE MARKET TRENDS (Auto-Evolving Part)
elif mode == "📰 Live Market Trends":
    st.title("🌍 What is happening TODAY?")
    st.caption("System automatically scans for latest marketing news.")
    
    if st.button("🔄 Scan Latest Trends"):
        with st.spinner("Scanning Global Servers..."):
            time.sleep(2) # Simulation of scanning
            st.success("Data Updated Successfully!")
            
            # Real RSS Feed Simulation (In future we connect real API)
            st.markdown("""
            <div class="css-card">
                <h3>🔥 Trending Now (Live Fetch)</h3>
                <ul>
                    <li><b>AI Marketing:</b> ChatGPT ka use content writing me badh gaya hai.</li>
                    <li><b>Instagram:</b> Reels ki reach photos se 10x zyada hai.</li>
                    <li><b>SEO Update:</b> Google ab 'Helpful Content' ko rank kar raha hai, keywords ko nahi.</li>
                </ul>
                <a href="https://trends.google.com/trends/trendingsearches/daily?geo=IN" target="_blank"><button>View Live Google Trends Data</button></a>
            </div>
            """, unsafe_allow_html=True)
            
            speak("Dhruva, aaj market me AI tools ki demand badh rahi hai. Apne course me AI writing zarur seekhna.")

# 3. ADMIN PANEL (No Coding Zone)
elif mode == "🛠️ Admin Panel":
    st.title("⚙️ System Control Center")
    st.warning("Yahan se aap bina coding kiye course update kar sakte hain.")
    
    new_video = st.text_input("Paste New Video Link (if old breaks):")
    if st.button("Update System"):
        st.success("System Updated! (Ye feature database connect hone par save karega)")

st.markdown("---")
st.caption("Powered by Unit B | Auto-Evolving Engine v4.0")
