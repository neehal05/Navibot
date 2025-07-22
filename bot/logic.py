# bot/logic.py
import openai
# import os

# Check OpenApi Key 
client = openai.OpenAI(api_key="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")

# System prompt
SYSTEM_PROMPT = {"role": "system", "content": "You are a helpful assistant."}

# Main function
def get_bot_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "you are a artificial intelligence that provide anser of my question."},
                      {"role": "user", "content": user_input}],
            temperature=0.5
        )

        if not response.choices or not response.choices[0].message.content.strip():
            print("Warning: Empty response from API")
            return []

        response_text = response.choices[0].message.content.strip()
        return response_text
    
    except Exception as e:
        print("OpenAI API error:", e)
        return "Sorry, I'm having trouble responding right now."
