# 🌟 Zentrack AI  
### 🧘‍♀️ Your Personal Habit & Wellness Multi-Agent System  

Zentrack AI is a multi-agent system designed to help users build and maintain healthy daily habits.  
It automates reminders, tracks actions, generates summaries, and provides intelligent habit recommendations.  

---

## 💡 Why Zentrack AI?

Most people struggle with consistency.  
We forget habits, skip routines, or lose motivation. Manual tracking becomes tiring and inconsistent.  

Zentrack AI solves this by:  
- 🕒 Automatically scheduling reminders  
- ✔ Tracking behavior (done / skipped / snoozed)  
- 📊 Summarizing daily & weekly progress  
- 🎯 Providing personalized recommendations  
- 🧠 Maintaining long-term memory  

---

## 🔑 Key Features

- ⏰ Automated habit reminders  
- 🔁 Daily behavior simulation  
- 📆 Weekly & daily summary generation  
- 🤖 Personalized recommendation engine  
- 💾 Long-term memory storage  
- 📈 Observability logs  
- 📥 CSV export for analysis  
- 🧪 14-day simulation via Kaggle Notebook  

---

## 🏗 Multi-Agent Architecture

(ASCII Diagram)

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

```
zentrack-ai/
├─ README.md
├─ notebook/
│   └─ Zentrack_AI_Demo.ipynb
├─ src/
│   ├─ agents/
│   ├─ memory/
│   ├─ tools/
│   └─ demo/
└─ assets/
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/nivedithan29/zentrack-ai.git
cd zentrack-ai
```

### 2️⃣ Run the demo simulation

```bash
python -m src.demo.run_simulation
```

This will generate:  
- 🎯 14-day habit simulation  
- 📊 METRIC logs  
- 📈 Summary report  
- 💡 Recommendation  
- 📂 CSV export (`demo_habit_history.csv`)  

---

## 📊 Example Output

### Summary (sample)
- ✔ Overall completion: **57.14%**  
- ✔ Completed: **24**  
- ❌ Skipped: **11**  
- 💤 Snoozed: **7**  

### Recommendation (sample)
💬 *"Good start! Try reducing targets for the hardest habit or adjusting reminder times."*

---

## 🛠 Technologies Used

- 🐍 Python  
- 📘 Pandas  
- 🤖 Multi-agent architecture  
- 🧰 Custom tools (CSV Exporter, Metrics Logger)  
- 🗄 Memory Bank  
- 🧪 Kaggle Notebook  

---

## 🔮 Future Enhancements

- 📱 Mobile or Web UI  
- 🔔 Push notifications  
- 🏃 Google Fit integration  
- 📉 Habit trend visualization  
- ☁ Deployment using Agent Engine  

---

## 📜 License

MIT License  
