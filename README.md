# Hustle-Mate - Your dost for every task
HustleMate is a **multi-agent, agent-to-agent (A2A) AI orchestration system** designed to automate and optimize a student’s academic workflow.  
Built with **AutoGen**, it leverages a network of specialized agents that collaborate autonomously to plan daily schedules, generate study materials, track assignments, and deliver timely reminders.

---

## ✅ Key Features

### 📅 Planner Agent
- Generates a personalized daily routine based on user input and timetable.
- Integrates OCR (OpenCV + Tesseract) for reading timetable images.
- Delegates study tasks, assignment checks, and reminders to other agents automatically.

### 📖 Study Assistant Agent
- Explains complex concepts in simple terms.
- Generates **AI-powered notes**, **flashcards**, and **quizzes**.
- Manages and retrieves user doubts for quick revision.

### 📝 Assignment Tracker Agent
- Authenticates with **Google Classroom API** using OAuth.
- Fetches active assignments with due dates and details.
- Integrates with Planner and Reminder agents to ensure deadlines are met.

### ⏰ Reminder Agent
- Sets reminders for assignments, quizzes, and study sessions.
- Sends notifications via:
  - 📧 **Email (SMTP with App Password)**
  - 📱 **WhatsApp (pywhatkit integration)**

### 📊 Progress Tracker Agent
- Logs task completions, quiz scores, and assignment submissions.
- Generates weekly/monthly progress reports.
- Sends reports via email or WhatsApp.

---

## ⚙️ Tech Stack

- **Language:** Python  
- **Framework:** [AutoGen](https://github.com/microsoft/autogen)  
- **LLM:** Gemini 2.5 Flash API  
- **Classroom Integration:** Google Classroom API (OAuth2)  
- **Frontend (Planned):** Streamlit  
- **OCR:** OpenCV + Tesseract  
- **Notifications:** SMTP (Email) + pywhatkit (WhatsApp)  
- **Multi-Agent Orchestration:** AutoGen GroupChat + GroupChatManager

---

## 🛠 Architecture

```
User Proxy Agent
      │
      ▼
Master Agent (Coordinator)
      │
┌─────┼────────┬──────────┬────────────┬───────────┐
▼     ▼        ▼          ▼            ▼
Planner  Study  Assignment  Reminder  Progress
Agent    Agent  Agent       Agent     Agent
```

- **Master Agent** acts as the central coordinator using A2A protocol.
- Delegates tasks to specialized agents based on the user's single query.
- Agents communicate via **AutoGen’s GroupChatManager**.

---

## 🔧 Setup & Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/HustleMate.git
cd HustleMate
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables
Create a `.env` file with:
```
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_CLIENT_SECRET=your_google_client_secret.json
SMTP_EMAIL=youremail@gmail.com
SMTP_APP_PASSWORD=your_app_password
```

### 5️⃣ Run the Application
```bash
python main.py
```

---

## 🎯 Usage Example

**User Input:**
```
I wake up at 7 AM, classes from 9 AM to 2 PM. I want to revise CNN, take a quiz on Machine Learning, check my AI assignments, and remind me to revise at 4 PM.
```
**HustleMate Actions (Auto):**
- Planner Agent creates a daily schedule.
- Study Agent generates CNN notes & ML quiz.
- Assignment Agent fetches AI assignments from Google Classroom.
- Reminder Agent schedules a reminder for 4 PM.
- Progress Agent logs completed tasks and updates progress.

---

## 📌 In Progress/Open for contribution

- Streamlit frontend for user-friendly interface
- AWS EC2 deployment for cloud-based access
- Push notifications for real-time alerts

---

## 🏆 Why HustleMate Stands Out

- **True Agent-to-Agent Protocol:** No manual switching; all agents coordinate in real-time.
- **Real Integrations:** Google Classroom, Email, WhatsApp.
- **End-to-End Workflow:** From planning → studying → tracking → reminders → progress reporting.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

