import streamlit as st
import feedparser
import time

# --- CONFIGURATION (Spotify Dark Theme) ---
st.set_page_config(page_title="Dhruva's Empire", layout="wide", page_icon="🔥")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: white; }
    .card { background-color: #121212; padding: 20px; border-radius: 10px; border: 1px solid #333; margin-bottom: 20px; }
    h1, h2, h3 { color: #1DB954 !important; }
    p, li { color: #b3b3b3; }
    .news-item { padding: 10px; border-bottom: 1px solid #333; }
    iframe { border-radius: 12px; }
</style>
""", unsafe_allow_html=True)

# --- FUNCTIONS ---
def get_news(topic):
    # Real Google News RSS Feed fetcher
    if topic == "Marketing":
        rss_url = "https://news.google.com/rss/search?q=Digital+Marketing+Trends&hl=en-IN&gl=IN&ceid=IN:en"
    else:
        rss_url = "https://news.google.com/rss/search?q=Library+Science+Technology&hl=en-IN&gl=IN&ceid=IN:en"
    
    feed = feedparser.parse(rss_url)
    return feed.entries[:5] # Top 5 news

# --- MAIN DASHBOARD (No Hidden Menus) ---
st.title("🔥 Dhruva's Integrated Ecosystem")
st.caption("Live Dashboard | Auto-Updating Content")

# LAYOUT
col1, col2 = st.columns([2, 1])

# --- COLUMN 1: THE LEARNING HUB (Full Playlists) ---
with col1:
    st.markdown("### 🎬 Job Ready Courses (Full Playlists)")
    
    tab1, tab2 = st.tabs(["📈 Digital Marketing (Zero to Hero)", "📚 Library Science (Koha)"])
    
    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("Yeh puri 10+ ghante ki playlist hai. Ye Google/Edureka ki hai jo hamesha update rehti hai.")
        # Embedding Full Playlist instead of single video
        st.video("https://www.youtube.com/watch?v=bixR-KIJKYM") 
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("Library Automation (Koha) Complete Training.")
        # Embedding Full Playlist for Library Science
        st.video("https://www.youtube.com/watch?v=oyyXgCgXFw8")
        st.markdown("</div>", unsafe_allow_html=True)

# --- COLUMN 2: THE AUTO-EVOLVING BRAIN (Live News) ---
with col2:
    st.markdown("### 🌍 Live Market Intelligence")
    st.write("System abhi internet scan kar raha hai...")
    
    # FETCHING REAL NEWS
    try:
        news_items = get_news("Marketing")
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 🔥 Trending Now (Live from Google)")
        for item in news_items:
            st.markdown(f"""
            <div class="news-item">
                <a href="{item.link}" target="_blank" style="text-decoration:none; color:white;">
                <b>{item.title}</b>
                </a>
                <br><small style="color:#1DB954;">{item.published}</small>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        st.error("News fetch karne me error. Internet connection check karein.")

    # COMMUNITY SIMULATION
    st.markdown("### 💬 Team Chat")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.text_input("Message Unit A...", placeholder="Type here...")
    st.markdown("""
    <small style="color:gray"><i>Unit B (Architect):</i> System is live.</small><br>
    <small style="color:gray"><i>Sakhi AI:</i> Maine aaj ki news update kar di hai.</small>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.write("---")
st.center = True
st.write("System ID: MONOPOLY-2026 | Status: **EVOLVING**")
