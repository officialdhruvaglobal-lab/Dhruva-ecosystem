import streamlit as st
import feedparser
import datetime
import pandas as pd
import time

# --- 1. CONFIGURATION & DESIGN ---
st.set_page_config(page_title="Adhirathi Ecosystem", layout="wide", page_icon="🦁")

st.markdown("""
<style>
    /* Dark Theme & Premium Vibe */
    .stApp { background-color: #000000; color: #e0e0e0; }
    
    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #333; }
    
    /* Glass Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .glass-card:hover { transform: translateY(-3px); border-color: #FFD700; }
    
    /* News Cards */
    .news-card {
        background-color: #121212;
        border-left: 4px solid #1DB954;
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 8px;
    }
    .news-link { color: #fff; text-decoration: none; font-weight: bold; font-size: 1.1em; }
    
    /* Text Accents */
    .gold-text { color: #FFD700; font-weight: bold; }
    .green-text { color: #1DB954; font-weight: bold; }
    
    /* Metrics */
    .metric-value { font-size: 2em; font-weight: bold; color: #38BDF8; }
</style>
""", unsafe_allow_html=True)

# --- 2. LIVE NEWS ENGINE ---
def fetch_live_news(topic):
    """Google News se real-time data lata hai."""
    try:
        if topic == "Library":
            rss_url = "https://news.google.com/rss/search?q=Library+Science+Digital+Libraries&hl=en-IN&gl=IN&ceid=IN:en"
        elif topic == "Tech":
            rss_url = "https://news.google.com/rss/search?q=Artificial+Intelligence+In+Education&hl=en-IN&gl=IN&ceid=IN:en"
        else:
            rss_url = "https://news.google.com/rss/search?q=Employment+News+India+Government+Jobs&hl=en-IN&gl=IN&ceid=IN:en"
        
        feed = feedparser.parse(rss_url)
        return feed.entries[:5] # Top 5 news
    except:
        return []

# --- 3. STATIC KNOWLEDGE BASE (Ye 'Khali Na Ho' wala part hai) ---
DATA_STORE = {
    "Exams (NET/JRF)": {
        "Unit 1: IFLA & Bodies": "IFLA (1927, The Hague) controls global library standards. Core Programs: UAP (Universal Availability of Publications) & UBC.",
        "Unit 2: Laws": "1948: Madras Act (First in India). 1967: Maharashtra Act. Ranganathan's 5 Laws are the constitution of Library Science.",
        "Unit 5: Classification": "DDC (Dewey, 1876) vs CC (Ranganathan, 1933). DDC uses pure notation (numbers), CC uses mixed notation (A-Z, 0-9).",
        "Unit 7: Automation": "ISO 2709 for data exchange. Z39.50 for retrieval. RFID for security. MARC 21 for Cataloging."
    },
    "Skills (Harvard Level)": {
        "Koha (LMS)": "The Open Source King. Modules to master: Patron Management, Cataloging (MARC), Circulation. Install on Ubuntu using 'sudo apt-get install koha-common'.",
        "Python for Lib": "Use 'Pandas' library to clean Excel data of books. Use 'BeautifulSoup' to scrape book data. Automate ISBN checks.",
        "English Comm.": "Resume Tip: Don't say 'I did BLIS'. Say 'I specialize in Information Architecture & Digital Archiving'."
    },
    "Jobs (Database)": [
         {"Role": "Metadata Specialist", "Org": "Netflix (Remote)", "Pay": "$45/hr", "Type": "MNC"},
         {"Role": "Librarian Gr-II", "Org": "KVS India", "Pay": "₹44,900", "Type": "Govt"},
         {"Role": "Digital Archivist", "Org": "Smithsonian", "Pay": "$60/hr", "Type": "Remote"}
    ]
}

# --- 4. SYSTEM BRAIN (LOGS) ---
if 'system_logs' not in st.session_state:
    st.session_state.system_logs = [{"Time": str(datetime.datetime.now().strftime("%H:%M")), "Event": "System Booted", "Status": "Online"}]

def add_log(event, status):
    st.session_state.system_logs.append({
        "Time": str(datetime.datetime.now().strftime("%H:%M")),
        "Event": event,
        "Status": status
    })

# --- 5. INTELLIGENT SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2919/2919600.png", width=80)
    st.markdown("## **Adhirathi Empire**")
    
    # Login System
    user_mode = st.text_input("🔑 Admin Key (Password)", type="password")
    
    if user_mode == "Adhirathi123":
        st.success("Welcome, Commander. 🦁")
        menu = st.radio("Menu", ["Dashboard", "📡 Live Radar (News)", "Manage Content", "System Diary"])
        is_admin = True
    else:
        st.info("Student View")
        menu = st.radio("Menu", ["Dashboard", "📚 Learn", "📡 Live Radar (News)", "💼 Job Portal", "📝 Mock Test"])
        is_admin = False
    
    st.markdown("---")
    if not is_admin:
        st.markdown("<div class='glass-card'>💎 <strong>Premium Mentorship</strong><br>Unlock 1-on-1 Guide<br>₹999/mo</div>", unsafe_allow_html=True)

# --- 6. MAIN INTERFACE ---

# === DASHBOARD ===
if menu == "Dashboard":
    st.markdown("<h1>Adhirathi <span class='gold-text'>Command Center</span></h1>", unsafe_allow_html=True)
    
    # Marquee
    st.markdown("""
    <div style='background:#1DB954; color:black; padding:10px; border-radius:5px; font-weight:bold;'>
    📢 LIVE UPDATE: UGC NET Notification Expected Soon | New Remote Jobs Added in Database
    </div><br>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.markdown("<div class='glass-card'><div class='metric-value'>15+</div>Modules Ready</div>", unsafe_allow_html=True)
    c2.markdown("<div class='glass-card'><div class='metric-value'>Global</div>News Feeds Live</div>", unsafe_allow_html=True)
    c3.markdown("<div class='glass-card'><div class='metric-value'>AI</div>System Tracking</div>", unsafe_allow_html=True)
    
    st.info("Tip: 'Live Radar' check karo real-time updates ke liye.")

# === LIVE RADAR (NEWS) ===
elif menu == "📡 Live Radar (News)":
    st.header("🌍 Global Intelligence Radar")
    
    tab1, tab2 = st.tabs(["📚 Library Science News", "🤖 Tech & AI"])
    
    with tab1:
        if st.button("Refresh Library Feed 🔄"):
            add_log("News", "Library Feed Updated")
        
        news = fetch_live_news("Library")
        if news:
            for item in news:
                st.markdown(f"""
                <div class='news-card'>
                    <a href='{item.link}' target='_blank' class='news-link'>{item.title}</a>
                    <p style='color:#888; font-size:12px;'>{item.published}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Google News connect nahi ho raha. Internet check karein.")

    with tab2:
        st.write("AI Updates:")
        news = fetch_live_news("Tech")
        for item in news:
             st.markdown(f"<div class='news-card'><a href='{item.link}' target='_blank' class='news-link'>{item.title}</a></div>", unsafe_allow_html=True)

# === LEARN SECTION ===
elif menu == "📚 Learn":
    st.header("The Knowledge Vault")
    
    tab1, tab2, tab3 = st.tabs(["🔥 UGC NET", "🛠️ Skills", "🗣️ English"])
    
    with tab1:
        unit = st.selectbox("Select Unit", list(DATA_STORE["Exams (NET/JRF)"].keys()))
        st.markdown(f"<div class='glass-card'><h3>{unit}</h3><p>{DATA_STORE['Exams (NET/JRF)'][unit]}</p></div>", unsafe_allow_html=True)
    
    with tab2:
        skill = st.selectbox("Select Skill", list(DATA_STORE["Skills (Harvard Level)"].keys()))
        st.markdown(f"<div class='glass-card'><h3>{skill}</h3><p>{DATA_STORE['Skills (Harvard Level)'][skill]}</p></div>", unsafe_allow_html=True)
        
    with tab3:
        st.markdown("<div class='glass-card'><h3>Interview Script</h3><p>'I am not just a librarian; I am a data curator. I ensure information reaches the right user at the right time using tools like Koha and DSpace.'</p></div>", unsafe_allow_html=True)

# === JOBS ===
elif menu == "💼 Job Portal":
    st.header("💼 Global Job Command")
    
    st.subheader("🔥 Premium Database (Verified)")
    for job in DATA_STORE["Jobs (Database)"]:
        st.markdown(f"""
        <div class='glass-card'>
            <div style='display:flex; justify-content:space-between;'>
                <h3 style='margin:0'>{job['Role']}</h3>
                <span class='gold-text'>{job['Pay']}</span>
            </div>
            <p>{job['Org']} | {job['Type']}</p>
            <button style='background:#FFD700; color:black; border:none; padding:5px; border-radius:4px;'>Apply Now</button>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("📡 Live Internet Jobs (Feed)")
    live_jobs = fetch_live_news("Jobs")
    for job in live_jobs:
        st.markdown(f"<div class='glass-card'>🆕 <strong>{job.title}</strong><br><a href='{job.link}' style='color:#1DB954;'>View Details</a></div>", unsafe_allow_html=True)

# === MOCK TEST ===
elif menu == "📝 Mock Test":
    st.header("🔥 PYQ Battleground")
    with st.container():
        st.markdown("<div class='glass-card'><strong>Q: Who is the father of Library Science in India?</strong></div>", unsafe_allow_html=True)
        ans = st.radio("Select Answer:", ["Melvil Dewey", "S.R. Ranganathan", "W.C. Sayers"], key="q1")
        if st.button("Submit Answer"):
            if ans == "S.R. Ranganathan":
                st.balloons()
                st.success("Correct! 🎯")
            else:
                st.error("Wrong Answer.")

# === ADMIN: SYSTEM DIARY ===
elif menu == "System Diary":
    st.header("🤖 System Logs (The Watcher)")
    df = pd.DataFrame(st.session_state.system_logs)
    st.table(df)

# === ADMIN: CONTENT ===
elif menu == "Manage Content":
    st.header("Content Control")
    st.warning("Admin Access Only")
    st.text_area("Update Content:", value="System content is currently locked by Adhirathi Protocol.")




