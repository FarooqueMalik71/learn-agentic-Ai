import os
import nest_asyncio
from dotenv import load_dotenv
from litellm import completion

# Enable async support in REPL or CLI
nest_asyncio.apply()

# Load environment variables from .env file
load_dotenv()

# Get Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")
os.environ["GEMINI_API_KEY"] = api_key

# Welcome Message
print("🔹 Gemini CLI Chatbot (type 'exit' to quit)\n")

# Continuous Chat Loop
while True:
    try:
        user_input = input("🟦 You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Exiting the chatbot. Shukriya!")
            break

        # Create message payload
        messages = [{"role": "user", "content": user_input}]

        # Call LiteLLM Gemini Model
        response = completion(
            model="gemini/gemini-2.0-flash",
            messages=messages
        )

        # Display Response
        print("🟨 Gemini:", response['choices'][0]['message']['content'], "\n")

    except Exception as e:
        print("❌ Error:", str(e))
