import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# -----------------------------
# 🌿 PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="MedAI Clinical Assistant",
    page_icon="🧬",
    layout="wide"
)

# -----------------------------
# 🌗 THEME TOGGLE
# -----------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

st.sidebar.button("🌗 Toggle Theme", on_click=toggle_theme)

# -----------------------------
# 🎨 DYNAMIC CSS (DARK / LIGHT)
# -----------------------------
if st.session_state.theme == "dark":
    bg = "linear-gradient(135deg, #050b12, #071a24, #02060a)"
    text = "white"
    box = "rgba(0,255,208,0.08)"
    border = "#00ffd0"
else:
    bg = "linear-gradient(135deg, #f5f7fa, #e4edf5, #dfe9f3)"
    text = "#111"
    box = "rgba(0,0,0,0.05)"
    border = "#0077ff"

st.markdown(f"""
<style>

.stApp {{
    background: {bg};
    color: {text};
}}

/* Title */
.title {{
    font-size: 40px;
    text-align: center;
    font-weight: bold;
    color: {border};
    margin-bottom: 10px;
}}

/* Response box */
.response-box {{
    background: {box};
    padding: 20px;
    border-radius: 15px;
    border-left: 4px solid {border};
    min-height: 200px;
}}

/* Buttons */
.stButton button {{
    background: linear-gradient(135deg, #00ffd0, #00aaff);
    color: black;
    font-weight: bold;
    border-radius: 10px;
}}

.stButton button:hover {{
    transform: scale(1.05);
}}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# 🧬 HEADER
# -----------------------------
st.markdown('<div class="title">🧬 MedAI Clinical Decision System</div>', unsafe_allow_html=True)
st.caption("AI-powered Medical Knowledge Assistant (RAG + Groq)")

# -----------------------------
# LAYOUT
# -----------------------------
col1, col2, col3 = st.columns([1, 2, 2])

# -----------------------------
# 📂 LEFT PANEL
# -----------------------------
with col1:
    st.markdown("### 📄 Medical PDF Upload")

    uploaded_file = st.file_uploader("Upload Report", type=["pdf"])

    if uploaded_file:
        if st.button("Analyze Document"):
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            res = requests.post(f"{API_URL}/upload", files=files)

            if res.status_code == 200:
                st.success("Document Indexed ✔")
            else:
                st.error(res.text)

# -----------------------------
# 🧠 CENTER PANEL
# -----------------------------
with col2:
    st.markdown("### 🧠 Clinical Query")

    query = st.text_input("Enter disease / symptoms / question")

    ask = st.button("Get Medical Insight")

# -----------------------------
# 📊 RIGHT PANEL
# -----------------------------
with col3:
    st.markdown("### 🧾 AI Medical Report")

    if "response" not in st.session_state:
        st.session_state.response = "Waiting for analysis..."

    if ask and query:
        with st.spinner("Analyzing medical data..."):
            res = requests.post(
                f"{API_URL}/ask",
                params={"query": query},
                timeout=60
            )

            if res.status_code == 200:
                st.session_state.response = res.json().get("answer", "")
            else:
                st.session_state.response = res.text

    st.markdown(f"""
    <div class="response-box">
        🩺 <b>Diagnosis Output:</b><br><br>
        {st.session_state.response}
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("⚠️ Educational AI system only. Not a medical diagnosis tool.")