import streamlit as st
from PIL import Image

# Set page title and icon
st.set_page_config(page_title="Lexi - Learn German", page_icon="🇩🇪", layout="wide")

# Header Section
st.image("https://upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Germany.svg", width=100)
st.title("Lexi - Your Personalized German Learning Platform")
st.subheader("Affordable, Interactive, and AI-Driven Language Learning")

# Industry Overview
st.markdown("### 🌍 Industry Overview")
st.write(
    "The global online language learning market is projected to reach **$81.55 billion by 2028**. "
    "German is among the most sought-after languages due to Germany’s strong economy and demand for skilled workers."
)

# Market Opportunity
st.markdown("### 🚀 Market Opportunity")
st.write(
    "Germany attracts over **400,000 international students** and a growing number of professionals. "
    "Traditional language schools can be expensive and rigid, making online platforms a preferred choice."
)

# Unique Value Proposition
st.markdown("### 🎯 Why Choose Lexi?")
st.write("Lexi stands out from competitors with:")
st.markdown(
    "- ✅ **Real-time interactive lessons** with skilled tutors.\n"
    "- ✅ **Flexible group sizes** (1:1, 1:2, 1:3) to suit different learning needs.\n"
    "- ✅ **Affordable pricing** (£5–£15 per session).\n"
    "- ✅ **AI-driven personalization** with interactive videos and gamification.\n"
    "- ✅ **Comprehensive progress tracking** and transparent teacher rating system."
)

# Competitive Landscape
st.markdown("### 🔍 Competitive Comparison")
competitors = {
    "Duolingo": "Free and gamified, but lacks deep conversational practice.",
    "Babbel": "Structured courses with real-life conversation skills, but costly.",
    "italki": "One-on-one tutoring, but lacks structured progress tracking.",
    "Goethe-Institut": "Certified courses but expensive and rigid.",
    "Lingoda": "Live structured classes, but pricing limits accessibility.",
    "Preply": "Flexible scheduling, but quality depends on tutors."
}
for competitor, description in competitors.items():
    st.markdown(f"- **{competitor}**: {description}")

# Pricing Section
st.markdown("### 💰 Pricing Plans")
st.write("Choose a plan that fits your learning style:")
st.markdown(
    "- **Pay-Per-Class:** £5 - £15 per session.\n"
    "- **Subscription Model:** Access pre-recorded structured courses.\n"
    "- **Bundled Packages:** Discounts for course packages."
)

# Target Audience
st.markdown("### 🎯 Who is Lexi for?")
st.write(
    "- **International students** moving to Germany.\n"
    "- **Professionals** relocating for work (IT, engineering, healthcare).\n"
    "- **Expats and travelers** wanting German language skills.\n"
    "- **Indian students and job seekers** aiming for German institutions."
)

# Call to Action
st.markdown("## Ready to Learn German the Smart Way? 🇩🇪")
st.write("Join Lexi today and start your journey to mastering German!")
st.button("Sign Up Now")

# Footer
st.markdown("---")
st.write("📢 Contact us: support@lexi.com | 🌍 Visit: www.lexi.com")
