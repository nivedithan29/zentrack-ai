# Zentrack AI
### *Your Personal Habit & Wellness Agent*

Zentrack AI is a multi-agent system designed to help users build and maintain healthy daily habits. It uses automated reminders, tracking, weekly summaries, and personalized recommendations to support long-term wellness.

---

## 🚀 Why Zentrack AI?
People struggle with consistency. We forget habits, skip routines, or lose motivation.  
Zentrack AI solves this by acting like a personal habit coach that actively tracks, reminds, evaluates, and recommends improvements.

---

## 🧠 Features
- Daily habit tracking (done, skipped, snoozed)
- Smart reminders and scheduling
- Weekly insight reports
- Personalized habit suggestions
- Long-term memory storage
- CSV export for analysis
- Demo simulation using Kaggle Notebook

---

## 🏗 Multi-Agent Architecture
                 ┌──────────────────────┐
                 │      User Input       │
                 └───────────┬───────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │     Onboarding Agent      │
                └───────┬───────────────────┘
                        │
                        ▼
               ┌──────────────────────────┐
               │       Memory Bank        │
               └───────┬─────────┬────────┘
                       │         │
                       ▼         ▼
    ┌────────────────────────┐  ┌────────────────────────────┐
    │     Scheduler Agent    │  │     Tracker Agent           │
    └─────────────┬──────────┘  └───────┬────────────────────┘
                  │                      │
                  ▼                      │
        ┌──────────────────────┐         │
        │    Reminder Agent    │─────────┘
        └───────────┬──────────┘
                    ▼
         ┌────────────────────────┐
         │     Summary Agent      │
         └─────────────┬─────────┘
                       ▼
         ┌────────────────────────┐
         │ Recommendation Agent    │
         └────────────────────────┘

---

## 📁 Project Structure

zentrack-ai/
├─ README.md
├─ notebook/
│ └─ Zentrack_AI_Demo.ipynb
├─ src/
│ ├─ agents/
│ ├─ memory/
│ ├─ tools/
│ └─ demo/
└─ assets/

---

Running it generates:
- Habit tracking simulation  
- Daily/weekly summary  
- Completion rate chart  
- Exported CSV files  

---

## 🛠 Tools & Technologies
- Python  
- Pandas, Matplotlib  
- Multi-Agent System  
- Sessions + Memory Bank  
- Custom tools (CSV export, metrics logger)  
- Kaggle Notebook  

---

## 🌱 Future Enhancements
- Mobile app integration  
- Google Fit / Health API syncing  
- Push notifications  
- Social habit challenges  
- More intelligent recommendation system  

---

## 📜 License
MIT License
