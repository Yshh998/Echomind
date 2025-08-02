# 🧠 EchoMind: Your Personal Contextual Memory OS

> Rethinking productivity with memory that thinks like you do.

---

## 🎯 Introduction

We live in an era where AI can autocomplete our sentences and summarize meetings — but it still doesn’t understand what truly matters to us.

**EchoMind** is a personal memory system designed to act as your **second brain** — but smarter. It goes beyond keyword search or summarization. EchoMind captures your thoughts, your emotions, and your intentions — helping you **remember not just what you thought, but why it mattered.**

---

## 🔍 The Problem

Even with advanced tools, people still experience:

- 🔎 **Information Overload** — scattered notes, Slack threads, Notion docs, bookmarks no one revisits  
- 🤯 **Mental Fatigue** — forgetting why a decision was made or losing focus mid-task  
- 🕳️ **Context Loss** — switching between tools without a system that tracks your thinking  

Most AI tools react to prompts.  
**EchoMind remembers your thinking.**

---

## 🚀 What's Built (Current MVP)

This prototype, built in **Streamlit**, includes:

### 💭 Thought Capture
- Input your thoughts and reflections
- Select associated emotion (😄 Happy, 😟 Stressed, 🤔 Curious, etc.)
- Add tags to group thoughts by topic or intent
- Timestamp is auto-saved
- Data is stored in temporary session memory (no database yet)

### 🔍 Memory Recall
- Filter thoughts by:
  - Emotion
  - Tag (text input)
- View previous entries in reverse chronological order
- Includes: emotion, tags, and formatted timestamp

### 📈 Weekly Reflection Dashboard
- Shows a 7-day overview of your emotional patterns and thought frequency
- Key features:
  - Total thoughts captured this week
  - Emotion frequency count
  - Sample memory highlights
  - 📊 Visual mood analytics:
    - Line chart of daily emotions
    - Bar chart of total weekly mood distribution

---

## 🧠 What Makes EchoMind Different

| Feature | EchoMind | Most Tools |
|---------|----------|-------------|
| Intention-aware recall | ✅ Yes | ❌ No |
| Emotionally tuned triggers | ✅ Yes | ❌ No |
| Cognitive memory threads | ✅ Yes | ❌ No |
| Visualized reflection | ✅ Yes | ❌ No |
| Smart capture workflow | ✅ Yes | ❌ No |

---

## 🧪 Tech Stack (Current Version)

| Function | Tool |
|---------|------|
| UI / App Framework | [Streamlit](https://streamlit.io) |
| Data Handling | Python, Pandas |
| Visualization | Matplotlib |
| State Management | Streamlit session state |

> ⚠️ No LLMs (e.g., OpenAI) or external APIs are currently used.

---

## 🔭 Planned Features

These features are in the roadmap but not yet implemented:

- 🔐 User login and multi-user support (via Supabase)
- ☁️ Cloud-based memory storage (PostgreSQL or Firebase)
- 🤖 AI-powered summarization and emotion prediction (GPT-4o)
- 🧠 Natural language recall (e.g., “Why was I hesitant in May?”)
- 🔁 Semantic memory search (LangChain + Pinecone)
- 👥 Team memory threads and shared thought timelines
- 🕸️ Mindmap visualization (Mermaid.js or D3.js)
- 🔔 Smart reminders based on mood or context

---

## 📌 Example Use Cases

- **Product Manager** → “Remind me what feedback I got after changing the roadmap.”
- **Researcher** → “Find that paper I loved in March about GPT-4 tuning.”
- **Creative** → “What ideas did I abandon when I felt burnt out?”

---

## 💻 Run Locally

```bash
git clone https://github.com/your-username/echomind.git
cd echomind
pip install -r requirements.txt
streamlit run app.py
