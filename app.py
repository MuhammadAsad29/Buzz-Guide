import streamlit as st
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from google import genai 

# ==========================================
# Task 4 & Bonus: API, Security, and Live Dataset
# ==========================================

# Load environment variables from the .env file
load_dotenv()

# Securely fetch the API key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the new Gemini Client securely
if api_key:
    client = genai.Client(api_key=api_key)
else:
    st.error("API Key not found. Please ensure your .env file is set up correctly with GEMINI_API_KEY.")

# Load real dataset directly from the internet (Bonus Mark)
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/IgorMinar/foodme/master/server/data/restaurants.csv"
    df = pd.read_csv(url)
    
    # Standardize column names
    df.rename(columns={
        'Restaurant name': 'Name',
        'Cuisine': 'Category',
        'Rating': 'Rating', 
        'Description': 'Description'
    }, inplace=True)
    
    # Generate mock social buzz scores
    np.random.seed(42)
    df['BuzzScore'] = np.random.randint(50, 100, size=len(df))
    
    return df

df = load_data()

# ==========================================
# Task 5: Visualization / UI (Streamlit)
# ==========================================

st.title("🌃 BuzzGuide: AI Night Out Recommender")
st.write("Find the perfect night out based on real internet data and AI-powered recommendations!")

# User Inputs
st.sidebar.header("Your Preferences")
preferred_category = st.sidebar.selectbox("What cuisine/category?", df['Category'].dropna().unique())
min_rating = st.sidebar.slider("Minimum Rating", 1.0, 5.0, 3.0)
user_vibe = st.sidebar.text_area("What is the vibe? (e.g., 'romantic', 'cheap', 'high energy')", height=150)

if st.button("Get Recommendation"):
    filtered_df = df[(df['Category'] == preferred_category) & (df['Rating'] >= min_rating)]
    
    if filtered_df.empty:
        st.warning("No venues match those exact criteria. Try lowering the rating or changing the cuisine!")
    else:
        top_venue = filtered_df.sort_values(by="BuzzScore", ascending=False).iloc[0]
        
        st.subheader(f"🏆 Top Match: {top_venue['Name']}")
        st.write(f"**Cuisine:** {top_venue['Category'].title()} | **Rating:** {top_venue['Rating']} / 5.0 | **Buzz Score:** {top_venue['BuzzScore']}/100")
        
        if api_key:
            st.info("Generating AI personalized pitch...")
            
            prompt = f"""
            Act as a local nightlife expert. I am looking for a '{user_vibe}' vibe. 
            I found a place called {top_venue['Name']}. Here is its description: {top_venue['Description']}.
            
            Write a 3-sentence enthusiastic pitch telling me why this specific place is perfect for my requested vibe. 
            Do not make up fake features about the venue, just relate its description to my vibe.
            """
            
            try:
                # Using the fast, lightweight model to avoid 503/404 errors
                response = client.models.generate_content(
                    model='gemma-4-31b-it', 
                    contents=prompt
                )
                st.write("### AI Assistant Says:")
                st.write(response.text)
            except Exception as e:
                st.error(f"API Error: Details: {e}")
        else:
            st.warning("Cannot generate AI pitch. Please provide a valid API key in your .env file.")

st.markdown("---")
st.caption("Data sources: Real public CSV fetched via URL. AI powered by Gemini Free API.")