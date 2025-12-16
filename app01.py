import streamlit as st

st.set_page_config(page_title="AI Roadmap", layout="centered")

st.title("🪜 AI & Data Science Roadmap")

tasks = [
    "Python mastery", "Pandas + NumPy", "Statistics basics", "3 mini projects",
    "ML algorithms", "scikit-learn", "4 serious projects", "Kaggle participation",
    "Neural networks basics", "APIs", "Deploy 2 projects", "GitHub portfolio",
    "Freelancing", "Internships", "Local businesses", "Remote junior roles"
]

progress = 0
completed = []

for task in tasks:
    if st.checkbox(task, key=task):
        completed.append(task)

progress = int((len(completed) / len(tasks)) * 100)

st.progress(progress)
st.success(f"{progress}% Completed")

st.subheader("💼 Paid Work You Can Get")
st.write("""
- Freelance Data Analyst  
- Junior ML Engineer  
- AI Automation Developer  
- Business Data Consultant  
- Research Assistant  
""")
st.info("Keep progressing and building your portfolio to unlock more opportunities!")