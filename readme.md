# PostGenie 🧞‍♂️

**PostGenie** is your magical automation sidekick for generating and posting content — without using any API. It interacts directly with public AI tools (like ChatGPT) to generate posts and then publishes them to your public pages using browser automation.

✨ No tokens. No API keys. No rate limits. Just real-time AI-to-AI automation.

---

## ✨ Why PostGenie?

Creating and sharing content regularly is time-consuming. PostGenie is built to do it all for you:

- 🤖 Automatically **generate content** via ChatGPT (using automation)
- 📝 Auto-login and **post to your pages** using browser simulation
- 🔐 Store login and config data **securely with encryption**
- 🧠 Customize logic, templates, and schedules
- 💻 Use the PyQt6 GUI **or run it headlessly** as a background worker
- 🔄 Supports **fully unattended, always-on operation**

---

## 🔐 Secure by Design

PostGenie uses `.env.enc` to store sensitive credentials like login info and platform URLs in **encrypted form**.

- `.env` is encrypted into `.env.enc` using a local secret key
- The app loads and decrypts `.env.enc` at runtime
- No plaintext credentials are exposed in logs or the interface

> You stay in control — PostGenie runs **locally** and securely.

---

## 🛠️ Use Cases

- Run as a **desktop app** with PyQt6 UI to monitor and control posts
- Run as a **worker script or server process** to auto-generate and publish content on a schedule
- Perfect for managing public pages while avoiding API restrictions or account detection

---

## 🧠 Tech Stack

- **Python 3.10+**
- **SeleniumBase** – browser automation (no API needed)
- **PyQt6** – modern GUI
- **cryptography** – AES encryption for `.env.enc`
- **dotenv** – environment variable management

---
