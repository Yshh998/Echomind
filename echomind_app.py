import streamlit as st
import datetime
import matplotlib.pyplot as plt
import pandas as pd

# Set page config
st.set_page_config(page_title="🧠 EchoMind Prototype")

# App title
st.title("🧠 EchoMind – Personal Contextual Memory OS")

st.markdown("""
Welcome to the prototype of EchoMind — your intelligent second brain. This tool captures your thoughts, recalls them based on context and emotion, and helps you reflect intentionally over time.
""")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["💭 Capture Thought", "🔍 Recall Memory", "📈 Weekly Reflection"])

# Initialize memory store
if "memories" not in st.session_state:
    st.session_state.memories = []

# Page 1: Capture Thought
if page == "💭 Capture Thought":
    st.subheader("💭 Capture a New Thought or Insight")
    with st.form("thought_form"):
        thought = st.text_area("What's on your mind?")
        emotion = st.selectbox("What are you feeling?", ["😄 Happy", "😟 Stressed", "🤔 Curious", "😠 Frustrated", "😌 Calm"])
        tags = st.text_input("Tags (comma-separated, e.g., idea, strategy, team)")
        submit = st.form_submit_button("Save Thought")

        if submit and thought.strip():
            st.session_state.memories.append({
                "text": thought.strip(),
                "emotion": emotion,
                "tags": [tag.strip() for tag in tags.split(",") if tag.strip()],
                "timestamp": datetime.datetime.now()
            })
            st.success("🧠 Thought captured successfully!")

# Page 2: Recall Memory
elif page == "🔍 Recall Memory":
    st.subheader("🔍 Recall Past Thoughts")
    selected_emotion = st.selectbox("Filter by emotion", ["All"] + ["😄 Happy", "😟 Stressed", "🤔 Curious", "😠 Frustrated", "😌 Calm"])
    tag_filter = st.text_input("Search by tag")

    filtered = []
    for mem in st.session_state.memories:
        if selected_emotion != "All" and mem["emotion"] != selected_emotion:
            continue
        if tag_filter and tag_filter.lower() not in [t.lower() for t in mem["tags"]]:
            continue
        filtered.append(mem)

    if not filtered:
        st.info("No matching memories found.")
    else:
        for mem in reversed(filtered):
            st.markdown(f"""
            **🕒 {mem['timestamp'].strftime('%b %d, %Y %I:%M %p')}**  
            *Emotion:* {mem['emotion']}  
            *Tags:* {', '.join(mem['tags'])}  
            > {mem['text']}
            ---
            """)

# Page 3: Weekly Reflection with Mood Graph
elif page == "📈 Weekly Reflection":
    st.subheader("📈 Weekly Emotional Reflection")

    today = datetime.datetime.now()
    week_ago = today - datetime.timedelta(days=7)

    last_week_memories = [mem for mem in st.session_state.memories if mem["timestamp"] >= week_ago]

    if not last_week_memories:
        st.info("You have not captured any thoughts in the past week.")
    else:
        st.markdown(f"**You’ve captured {len(last_week_memories)} thoughts this week.**")

        # Emotional breakdown
        emotion_counts = {}
        for mem in last_week_memories:
            emotion_counts[mem["emotion"]] = emotion_counts.get(mem["emotion"], 0) + 1

        st.markdown("### 🧠 Emotional Trends")
        for emotion, count in emotion_counts.items():
            st.write(f"{emotion}: {count} times")

        st.markdown("### 📝 Sample Highlights")
        for mem in reversed(last_week_memories[:3]):
            st.markdown(f"""
            **🕒 {mem['timestamp'].strftime('%b %d, %Y %I:%M %p')}**  
            *Emotion:* {mem['emotion']}  
            > {mem['text']}
            ---
            """)

        # 🟦 Mood Graph: Line + Bar with Emotion Colors
        st.markdown("### 📊 Mood Graph")

        df = pd.DataFrame(last_week_memories)
        df["date"] = df["timestamp"].dt.date

        daily_counts = df.groupby(["date", "emotion"]).size().unstack(fill_value=0)
        weekly_counts = df["emotion"].value_counts()

        # Define colors for each emotion
        emotion_colors = {
            "😄 Happy": "#FFD700",
            "😟 Stressed": "#FF6347",
            "🤔 Curious": "#1E90FF",
            "😠 Frustrated": "#8B0000",
            "😌 Calm": "#32CD32"
        }

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

        for emotion in daily_counts.columns:
            ax1.plot(daily_counts.index, daily_counts[emotion], label=emotion, marker='o', color=emotion_colors.get(emotion, 'gray'))
        ax1.set_title("📈 Mood Trend Over the Week (Line Graph)")
        ax1.set_xlabel("Date")
        ax1.set_ylabel("Number of Thoughts")
        ax1.legend(title="Emotion")
        ax1.grid(True)

        bar_colors = [emotion_colors.get(emotion, 'gray') for emotion in weekly_counts.index]
        weekly_counts.plot(kind='bar', color=bar_colors, ax=ax2)
        ax2.set_title("📊 Weekly Emotion Summary (Bar Chart)")
        ax2.set_xlabel("Emotion")
        ax2.set_ylabel("Total Count")
        ax2.grid(axis='y')

        plt.tight_layout()
        st.pyplot(fig)
