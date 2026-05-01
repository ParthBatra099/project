# 🤖 JUNE - Just Unified Neural Engine

A **futuristic AI productivity assistant** with voice interaction and an intelligent dashboard inspired by Jarvis-style interfaces.

## ✨ Features

- 🎙️ **Voice-Driven Interface** - Natural conversational AI
- 📊 **Smart Task Management** - AI-powered productivity tracking
- ⏱️ **Focus Timer System** - Pomodoro-style productivity modes
- 🧠 **Intelligent Suggestions** - Context-aware recommendations
- 🎨 **Futuristic Dark UI** - Neon glowing Jarvis-inspired interface
- ⚡ **Real-time Communication** - Socket.io powered interactions
- 🔄 **Multiple Modes** - Coding, Study, and Break modes

## 🏗️ Architecture

```
JUNE-AI-Assistant/
├── frontend/                 # React.js UI
├── backend/                  # Node.js server
├── ai-engine/               # Flask AI logic
├── shared/                  # Shared utilities
└── docs/                    # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Node.js v16+
- Python 3.9+
- npm or yarn

### Installation

```bash
# Clone the repository
git clone https://github.com/ParthBatra099/project.git
cd project

# Install backend dependencies
cd backend && npm install

# Install AI engine dependencies
cd ../ai-engine && pip install -r requirements.txt

# Install frontend dependencies
cd ../frontend && npm install
```

### Running the Application

```bash
# Terminal 1: Start Flask AI Engine
cd ai-engine
python app.py

# Terminal 2: Start Node.js Backend
cd backend
node server.js

# Terminal 3: Start React Frontend
cd frontend
npm start
```

Access the application at `http://localhost:3000`

## 🎯 Core Features

### Voice Assistant System
- Continuous background listening
- Wake word: "JUNE"
- Natural conversational responses
- Voice command processing

### Modes System
- **Coding Mode**: Focus timer + project tracking
- **Study Mode**: Subject-based task management
- **Break Mode**: Rest suggestions and reminders

### Task Management
- Create, update, and track tasks
- Project organization
- Priority-based suggestions
- Status tracking (pending/in-progress/completed)

### Focus Timer
- Customizable Pomodoro timer (default: 50 min)
- Circular animated display
- Progress tracking
- Break notifications

## 🎨 UI Design

- **Dark Theme**: #0a0e27 background
- **Neon Glow**: Blue/purple gradient accents
- **Animations**: Framer Motion powered
- **Cards**: Glassmorphism effect
- **Core**: Animated glowing AI orb

## 🛠️ Technology Stack

### Frontend
- React.js
- Framer Motion
- Tailwind CSS
- Socket.io Client

### Backend
- Node.js + Express
- Socket.io
- MongoDB (optional)

### AI Engine
- Flask
- Flask-CORS
- NLP libraries

## 📚 API Documentation

See `/docs/API.md` for detailed API endpoints.

## 🔐 Environment Variables

Create `.env` files in `backend/` and `ai-engine/`:

```env
# backend/.env
PORT=5000
FLASK_SERVER=http://localhost:5001
NODE_ENV=development

# ai-engine/.env
FLASK_PORT=5001
DEBUG=True
```

## 📖 Documentation

- [Architecture Guide](./docs/ARCHITECTURE.md)
- [Voice Integration Guide](./docs/VOICE.md)
- [Component Documentation](./docs/COMPONENTS.md)
- [API Reference](./docs/API.md)

## 🤝 Contributing

Fork this repository and submit a pull request with your improvements.

## 📝 License

MIT License - feel free to use this project for personal or commercial purposes.

## 🌟 Credits

Inspired by Jarvis (Iron Man) and modern AI assistants like Siri and Alexa.

---

**Made with ❤️ by ParthBatra099**
