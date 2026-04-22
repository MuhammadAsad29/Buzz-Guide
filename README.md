# 🌃 BuzzGuide: AI Night Out Recommender

BuzzGuide is an interactive, AI-powered web application that helps users find the perfect restaurant or nightlife activity based on their specific mood and vibe. 

Instead of relying on AI hallucinations, BuzzGuide fetches a **real-world dataset** of venues, filters them based on user preferences (cuisine and rating), and passes the top factual match to the **Gemini API**. The AI then acts as a local nightlife expert, generating a highly personalized, 3-sentence pitch tailored exactly to the user's requested vibe.

## ✨ Features
* **Live Dataset Integration:** Dynamically fetches and parses a public CSV dataset using Pandas, ensuring recommendations are based on real places.
* **AI Persona Adaptation:** Uses Google's `gemini-2.5-flash-lite` model to adapt its tone (e.g., romantic, casual, energetic, or even a 1940s detective) based on the user's input.
* **Interactive UI:** A clean, responsive web interface built entirely in Python using Streamlit.
* **Secure API Handling:** Utilizes `python-dotenv` to keep API keys hidden and secure from public repositories.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Frontend/UI:** [Streamlit](https://streamlit.io/)
* **AI/LLM:** [Google GenAI SDK](https://ai.google.dev/) (Gemini 2.5 Flash Lite)
* **Data Processing:** Pandas, NumPy
* **Security:** python-dotenv

## 🚀 Installation & Setup

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR_USERNAME/buzzguide.git](https://github.com/YOUR_USERNAME/buzzguide.git)
cd buzzguide
2. Install required dependencies
Make sure you have Python installed, then run:

Bash
pip install streamlit pandas numpy python-dotenv google-genai
3. Set up your API Key
You will need a free Google Gemini API key. Get one from Google AI Studio.

Create a new file in the root directory named .env

Add your API key to the file like this:

Plaintext
GEMINI_API_KEY=your_actual_api_key_here
🎮 Usage
Once your dependencies are installed and your API key is secured in the .env file, launch the application by running:

Bash
streamlit run app.py
A local web server will start, and the BuzzGuide interface will automatically open in your default web browser.

Select your preferred cuisine, set a minimum rating, type in your exact vibe (e.g., "I need a quiet, dimly lit spot for an anniversary dinner"), and let the AI do the rest!

📝 License
This project was built as part of an academic assignment on Generative AI integration. It is open-source and available under the MIT License.
