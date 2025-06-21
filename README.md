# Smart Task Scheduler & Messenger  
#### Video Demo: [https://youtu.be/oTynS6eHUYE](https://youtu.be/oTynS6eHUYE)

---

#### Description:

Smart Task Scheduler & Messenger is a Python-based productivity assistant designed to simplify two common user needs: quick communication and effective task reminders. The application allows users to either send an instant WhatsApp message using voice input or schedule a future task that will notify them with either a system notification or a reminder file. It uses speech recognition to take user input via microphone and integrates scheduling and messaging features into a single lightweight script.

The idea stemmed from observing the repetitive friction in daily productivity workflows: manually opening WhatsApp for simple messages, and forgetting tasks that aren’t logged into a calendar or alarm. Instead of relying on separate apps for reminders and messaging, this tool combines both functionalities into one command-line Python program.

---

#### File Overview:

This project consists of a single Python file named `Project(1).py`, which encapsulates all the functionality. It is structured into clearly separated modules:

- **Voice Input Module (`get_voice_input`)**:  
  This function captures spoken input using the `SpeechRecognition` library and converts it into text via Google’s Speech API. It includes basic error handling for cases like silence, unclear speech, or no internet. If the voice input fails, the user is prompted to type their message instead. This fallback mechanism was intentionally included for reliability and better user experience.

- **WhatsApp Messaging Module (`send_whatsapp_message`)**:  
  Using `pywhatkit`, this function allows users to send a WhatsApp message instantly to any valid phone number with the country code. The message can be dictated or typed manually. For convenience and automation, the WhatsApp tab is automatically closed after sending the message.

- **Task Scheduler (`schedule`)**:  
  This module lets users schedule a task by specifying a delay (in days, hours, minutes, and seconds). For short-term reminders (5 minutes or less), the app issues a popup system notification using the `plyer` library. For longer delays, the app creates a `.txt` reminder in a dedicated `~/Reminders` directory, ensuring the user has a persistent record of scheduled tasks.

- **Reminder File Creator (`create_text_reminder`)**:  
  This function generates a human-readable reminder file with the task name and the scheduled timestamp. This design ensures flexibility even on systems where desktop notifications may be disabled or missed.

- **Main Entry Point (`main`)**:  
  This interactive CLI prompts the user to choose between sending a WhatsApp message or scheduling a reminder. It orchestrates the logic accordingly, taking in input parameters and calling the appropriate modules.

---

#### Design Decisions:

Several design choices were debated during development. One key decision was handling short vs. long reminders differently. Originally, all tasks were meant to trigger system notifications, but this posed reliability issues for longer durations (especially if the script or system shut down). Thus, a split was introduced: short-term tasks use real-time notifications, while long-term tasks are logged as files, giving users control and persistence.

Another consideration was voice input. Although convenient, it’s inherently unreliable in noisy environments. To address this, a manual fallback input method was added. This hybrid design balances innovation with practicality.

The decision to keep everything in a single file was made to reduce setup complexity and enhance portability. However, with additional features, modularization into multiple scripts or classes would be the logical next step.

---

#### Conclusion:

Smart Task Scheduler & Messenger is a practical and user-friendly tool that demonstrates how voice recognition, automation, and messaging can be combined in a cohesive, minimal Python project. It offers users real utility while also serving as a strong example of integrating multiple external libraries into a functional application. Whether you're reminding yourself to check on dinner or instantly messaging a colleague, this script gets it done—with your voice or your keyboard.
