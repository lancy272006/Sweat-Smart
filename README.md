# 💪🏋️‍♀️ SWEAT SMART – Gym Nutrition Assistant

SWEAT SMART is a **Streamlit-based AI gym assistant** that provides **fiber-rich food suggestions and nutrition guidance** to support gym workouts. The app connects to a **locally running LLM (Gemma)** using an API endpoint and delivers interactive, real-time responses.

---

## 🚀 Features

* 🧠 AI-powered nutrition guidance
* 🥗 Focus on fiber-rich foods for workouts
* 💬 Chat-style interface
* 🔒 Runs fully on a **local server** (no cloud dependency)
* ⚡ Built with Streamlit for fast UI development

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – Frontend UI
* **Requests** – API communication
* **Local LLM (Gemma)** – AI model
* **LM Studio / Local API Server**

---

## 📂 Project Structure

```
 gym-chatbot/
 ├── app.py          # Main Streamlit application
 ├── README.md       # Project documentation
 └── requirements.txt
```

---

## ⚙️ Prerequisites

Make sure you have the following installed:

* Python 3.8+
* Streamlit
* Requests
* LM Studio (or any local LLM server)
* Gemma model downloaded and running locally

---

## 📦 Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd gym-chatbot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

1. Start your **local LLM server** (example using LM Studio)

   * Load the **Gemma model**
   * Enable **Local API Server**
   * Note the API URL (example):

     ```
     http://192.168.27.162:1234/v1/chat/completions
     ```

2. Update the API URL in `app.py` if needed:

```python
API_URL = "http://192.168.27.162:1234/v1/chat/completions"
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Open the browser at:

```
http://localhost:8501
```

---

## 🧩 How It Works

* User enters a nutrition-related question
* The question is sent as a **payload** to the local LLM API
* The Gemma model processes the input
* The AI-generated response is displayed in the app

---

## 📌 Example Use Cases

* What to eat before a gym workout
* Fiber-rich foods for muscle recovery
* Healthy diet tips for fitness beginners

---

## 🔐 Privacy & Security

* Runs **100% locally**
* No internet or cloud AI required
* Your data never leaves your system

---

## 📈 Future Improvements

* Add workout-specific diet plans
* User profile personalization
* Meal tracking integration
* UI theming and animations

---

## 👩‍💻 Author

**Lancy**
AI & Python Enthusiast

---

## 📄 License

This project is for **educational and personal use**.

---



