import os
from dotenv import load_dotenv
import google.generativeai as genai

#loads env variable
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel("gemini-3-flash-preview")

chat = model.start_chat(history=[])

print ("--- 🚀 Gemini Dynamic Chat (Type 'bye' to quit) ---")

while True: 

    prompt = input("you: ")

    if prompt.lower() in ['exit', 'quit', 'bye']:
        print("Gemini: Goodbye! Happy coding!")
        break
    try:
        response = chat.send_message(prompt)
        print(f"Gemini: {response.text}\n")
    except Exception as e:
        print(f"⚠️ Error: {e}")


# # for m in genai.list_models():
# #     if 'generateContent' in m.supported_generation_methods:
# #         print(m.name)