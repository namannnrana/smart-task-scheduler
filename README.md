# 🧠 Smart Task Scheduler & Messenger

🎥 **Video Demo**: [https://youtu.be/oTynS6eHUYE](https://youtu.be/oTynS6eHUYE)

**Smart Task Scheduler & Messenger** is a Python-based productivity assistant designed to simplify two common user needs: quick communication and effective task reminders. It allows users to either send an instant WhatsApp message using voice input or schedule a future task that will notify them with either a system notification or a reminder file.

Using speech recognition to capture voice commands, this tool integrates messaging and scheduling into a single, lightweight command-line program.

---

## 💡 Motivation

The idea stemmed from everyday productivity friction:
- Manually opening WhatsApp just to send simple messages
- Forgetting tasks that weren’t added to a calendar or alarm

Instead of switching between apps, this script provides **two key functions**:
- 🎙️ Speak and send a message instantly
- ⏰ Schedule a reminder with a voice or keyboard input

---

## 🗂️ File Overview

This version of the project has been modularized for maintainability:

```
smart-task-scheduler/
├── main.py                  # Entry point for the CLI interface
├── voice_input.py           # Captures and processes spoken input
├── whatsapp_messenger.py    # Sends WhatsApp messages via pywhatkit
├── scheduler.py             # Handles notifications and text reminders
└── reminders/               # Auto-created for long-term task reminder files
```

---

## 🔍 Module Breakdown

### 🎙️ `get_voice_input` (in `voice_input.py`)
- Captures speech using `SpeechRecognition` and Google’s Speech API
- Includes robust error handling for silence, noise, or connectivity issues
- Falls back to manual keyboard input if voice recognition fails

### 💬 `send_whatsapp_message` (in `whatsapp_messenger.py`)
- Sends an instant WhatsApp message via `pywhatkit`
- Accepts either dictated or typed input
- Automatically closes the browser tab after sending

### ⏰ `schedule` (in `scheduler.py`)
- Accepts a delay (days, hours, minutes, seconds) for scheduling
- For delays under 5 minutes: shows a **system popup notification**
- For longer delays: creates a **.txt file reminder** in `~/Reminders`

### 📝 `create_text_reminder`
- Generates a persistent file-based reminder containing task details
- Designed as a fallback when notifications may be missed or unsupported

### 🧭 `main.py`
- Command-line interface that prompts the user to:
  - (1) Send a WhatsApp message
  - (2) Schedule a task reminder
- Routes logic based on user selection

---

## 💡 Design Decisions

### 📌 Dual Reminder Strategy
- **Short reminders** use system notifications for immediacy
- **Long reminders** are saved to disk to survive system reboots or script shutdown

### 🧠 Voice Input with Fallback
- Voice control is powerful but error-prone in noisy environments
- A **manual input fallback** ensures a reliable experience for all users

### 🗃️ Originally Single-File
- The project began as a compact single-file script
- It has since been modularized into separate logical components to support future growth and better organization

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/namannnrana/smart-task-scheduler.git
cd smart-task-scheduler
```

### 2. Install Dependencies

```bash
pip install SpeechRecognition pywhatkit plyer pyaudio
```

> Trouble with PyAudio?
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

### 3. Run the Program

```bash
python main.py
```

---

## 📜 Certificate

This project was submitted as the final project for:

**[CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/)** by Harvard University  
📄 Certificate Link: [cs50.harvard.edu/certificates/c8cf09c0-fefc-4dca-ae68-58eee7816efe](https://cs50.harvard.edu/certificates/c8cf09c0-fefc-4dca-ae68-58eee7816efe)

---

## 🙋 Author

**Naman Rana**  
🔗 [GitHub: @namannnrana](https://github.com/namannnrana)

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- CS50 Team & Professor David J. Malan
- Python open-source community
- Users who inspired this real-world utility
