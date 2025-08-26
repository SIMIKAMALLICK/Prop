import streamlit as st
import random

st.set_page_config(page_title="Pagol", page_icon="🤪", layout="centered")

# ------------------ CSS for rainbow background + floating emojis ------------------
page_style = """
<style>
body {
  margin: 0;
  height: 100vh;
  background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a1c4fd, #c2e9fb, #d4fc79);
  background-size: 400% 400%;
  animation: rainbowBG 18s ease infinite;
  color: #222;
  font-family: "Comic Sans MS", cursive, sans-serif;
}

/* dark overlay for readability */
.block-container {
  background: rgba(255, 255, 255, 0.15);
  border-radius: 15px;
  padding: 20px;
  backdrop-filter: blur(6px);
}

/* rainbow background animation */
@keyframes rainbowBG {
  0%{background-position:0% 50%}
  50%{background-position:100% 50%}
  100%{background-position:0% 50%}
}

/* Floating emojis */
.floater {
  position: absolute;
  font-size: 28px;
  animation: floaty linear infinite;
}
@keyframes floaty {
  from { transform: translateY(100vh) rotate(0deg); opacity: 1; }
  to { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
}

/* Center all buttons */
div.stButton > button {
  width: 100%;
  background: linear-gradient(135deg, #ff758c, #ff7eb3);
  color: white;
  border-radius: 12px;
  font-size: 18px;
  font-weight: bold;
  border: none;
  padding: 10px 0;
  transition: 0.3s;
}
div.stButton > button:hover {
  transform: scale(1.05);
  background: linear-gradient(135deg, #ff4d6d, #ff85a1);
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Generate floating emojis
def emoji_rain():
    emojis = ["😂", "🤪", "🤣", "🙃", "🤡", "😜"]
    html = "<div>"
    for i in range(20):
        emoji = random.choice(emojis)
        left = random.randint(2, 95)
        duration = random.uniform(6, 12)
        delay = random.uniform(-8, 0)
        size = random.randint(24, 38)
        html += f"<div class='floater' style='left:{left}%; font-size:{size}px; animation-duration:{duration}s; animation-delay:{delay}s;'>{emoji}</div>"
    html += "</div>"
    return html

st.markdown(emoji_rain(), unsafe_allow_html=True)

# ------------------ Random GIF lists ------------------
YES_GIFS = [
    "https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif"
]


# ------------------ Title ------------------
st.markdown(
    "<h1 style='text-align:center; color:#fff; text-shadow:2px 2px 8px #000;'>Shruti Sona Chader Kona Dim Pereche Athero Khana🤪</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center; color:#fff; font-size:20px; margin-bottom:30px;'>Tui Pagol Seta Mene Nile Gift Ache😏</p>",
    unsafe_allow_html=True,
)

# ------------------ Buttons ------------------
col1, col2, col3 = st.columns([1,2,1])  # Center buttons
with col2:
    yes = st.button("Ha tui udmad 😂")
    no = st.button("Na tui e udmad 😤")

# ------------------ Logic ------------------
if yes:
    gif = random.choice(YES_GIFS)
    st.balloons()
    st.markdown(
        "<div style='text-align:center; background:rgba(255,255,255,0.3); border-radius:12px; padding:15px;'>"
        "<h3 style='color:#fff;'>Awwwe 💖 How can you be mad? 😘</h3>"
        "<p style='color:#fff; font-size:18px;'>💕 You’re a queen 👑</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='text-align:center; margin-top:15px;'><img src='{gif}' width='320'></div>",
        unsafe_allow_html=True,
    )

elif no:
    gif = random.choice(NO_GIFS)
    st.markdown(
        "<div style='text-align:center; background:rgba(255,255,255,0.3); border-radius:12px; padding:15px;'>"
        "<h3 style='color:#fff;'>Tui na bolleo sobaijane tui pagol... 🤔</h3>"
        "<p style='color:#fff; font-weight:bold;'>Pagla detected anyway 🤡😜</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns([1,2,1])  # Center the image
    with col2:
        st.image("pagla.jpeg", width=320, caption="Pagla confirmed 🤡")
