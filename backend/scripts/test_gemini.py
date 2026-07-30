import os
import google.generativeai as genai

# Test Gemini integration script
api_key = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
genai.configure(api_key=api_key)

print("Gemini configuration ready.")