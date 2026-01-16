# 🧠 Nova – Desktop Voice Assistant (Python)

Nova is a Python-based **Windows desktop voice assistant** that listens to voice commands,
performs system actions, opens applications, plays music via Spotify,
and responds using text-to-speech.

---

## 📌 Features (Currently Supported)

### 🎙 Voice Interaction

- Always listening (microphone-based)
- Speech-to-text
- Text-to-speech responses

---

### ⏰ System Information

| Voice Command         | Action                    |
| --------------------- | ------------------------- |
| `what is the time`    | Speaks current time       |
| `what is the battery` | Speaks battery percentage |

---

### 📂 Open Applications

| Command                      | Action               |
| ---------------------------- | -------------------- |
| `open chrome`                | Opens Google Chrome  |
| `open notepad`               | Opens Notepad        |
| `open calculator`            | Opens Calculator     |
| `open word` / `open ms word` | Opens Microsoft Word |

---

### 🎵 Music (Spotify)

| Command            | Action                              |
| ------------------ | ----------------------------------- |
| `play <song name>` | Opens Spotify and searches the song |

If no song name is provided:

- Nova asks: **“Please tell me which song you want to play”**

---

### 📞 WhatsApp

| Command         | Action                     |
| --------------- | -------------------------- |
| `open whatsapp` | Opens WhatsApp through Web |

⚠️ WhatsApp Desktop does **not** allow auto-sending messages.

---

### 🔊 Volume Control

| Command           | Action           |
| ----------------- | ---------------- |
| `increase volume` | Increases volume |
| `decrease volume` | Decreases volume |
| `mute system`     | Mutes audio      |
| `unmute system`   | Unmutes audio    |

---

### 🌐 Web Search / AI Fallback

| Command                    | Action              |
| -------------------------- | ------------------- |
| `search python decorators` | Opens Google search |
| Unknown queries            | AI-based response   |

---

## 🚀 Future Improvements

### 🎵 Music

- Spotify Web API integration
- Pause / resume / next / previous commands

### 🧠 AI

- Context memory
- Better intent recognition
- Reduced web fallback

### 🖥 Desktop App

- Auto-start with Windows
- System tray menu
- Settings panel

---

## 📦 Convert Nova to Desktop App (EXE)

- python -m pip install pyinstaller
- python -m PyInstaller --onefile --noconsole tray_app.py
