# RecruitPal – Intelligent HR Assistant 🤖💼

**RecruitPal** is a comprehensive AI-powered HR assistant that helps recruiters analyze candidate data and search the global talent pool with intelligent insights. It combines natural language processing, talent analytics, and global data integration for smart hiring.

---

## 🔥 Features

### 📊 Database Chat

* **Upload & Analyze**: Upload job descriptions (PDF) and candidate data (CSV) for AI-powered analysis
* **Smart Insights**: Get detailed analysis of skills, experience, and hiring recommendations
* **Contextual Conversations**: AI maintains context from previous conversations
* **Professional Actions**: Send emails and create calendar events from the chat

### 🌐 Global Chat

* **Global Talent Search**: Search the worldwide talent pool using People Data Labs API
* **Context-Aware Conversations**: Maintains last 5 chats for follow-up questions
* **Professional Link Extraction**: Auto-fetch LinkedIn, GitHub, Twitter, and email links
* **Rich Candidate Profiles**: View role, experience, skills, and contact info
* **Interactive Follow-ups**: One-click refinements and suggestions

### 💎 Enhanced UI/UX

* Modern dark theme and responsive layout
* Smooth transitions with Framer Motion
* Real-time processing indicators and link cards
* Markdown support for AI responses

---

## 🛠️ Tech Stack

### Frontend

* React 18 (Vite)
* Tailwind CSS
* Framer Motion
* React Markdown
* Lucide React

### Backend

* Python Flask (REST API)
* PostgreSQL
* Google Gemini AI
* People Data Labs API
* Composio (Email & Calendar automation)

---

## 🚀 Getting Started

### 📁 Project Structure (Local)

```
recruiter-bandhu/
├── client/       → Frontend (React)
├── server/       → Backend (Flask)
```

---

### 🧬 Clone the Repository

```bash
git clone https://github.com/sohamshirke10/recruiter-bandhu.git
cd recruiter-bandhu
```

---

### 📦 Install Dependencies

#### Frontend

```bash
cd client
npm install
```

#### Backend

```bash
cd ../server
pip install -r requirements.txt
```

---

### ⚙️ Set Up Environment Variables

#### In `client/.env`

```
VITE_BACKEND_URL=http://localhost:5000
```

#### In `server/.env`

```
GOOGLE_API_KEY=your_gemini_api_key
CONNECTION_URL=your_postgres_connection_string
PEOPLE_DATA_LABS_API_KEY=your_pdl_api_key
```

---

### 🧪 Run the Application

#### Backend

```bash
cd server
python app.py
```

#### Frontend (in another terminal)

```bash
cd client
npm run dev
```

---

## 🧠 Usage

### Database Chat

* Click **"Start New Analysis"** → **"Database Chat"**
* Upload Job Description (PDF) and Candidate Data (CSV)
* Ask questions to analyze fit, skills, or comparisons

### Global Chat

* Click **"Start New Analysis"** → **"Global Chat"**
* Enter search queries in natural language
* View professional data, profiles, and follow-up suggestions

---

## 📡 API Endpoints

| Method | Endpoint               | Description                   |
| ------ | ---------------------- | ----------------------------- |
| POST   | `/newChat`             | Create a new database chat    |
| POST   | `/chat`                | Send message to database chat |
| POST   | `/chat/2`              | Send message to global chat   |
| GET    | `/gettables`           | Get all chat tables           |
| GET    | `/get-chats`           | Get chat history              |
| GET    | `/get-job-description` | Get job description summary   |

---

## 🤝 Contributing

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Submit a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---
