import os
from google import genai
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Create Gemini client using your Google API Key
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


response = client.models.generate_content(
    model="gemini-3-flash-preview",  
    contents=input("Enter your question")
)

# Display the response text
print(response.text)