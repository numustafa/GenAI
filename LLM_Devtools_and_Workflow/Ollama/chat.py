import os
import ollama

print("Hello, Ollama!")
print("Current directory files:", os.listdir('.'))

try:
    response = ollama.chat(
        model='deepseek-r1:1.5b',
        messages=[{
            'role': 'user',
            'content': 'What is in the name of last Ottoman King?'
        }]
    )
    print("Response received:")
    print(response)
except Exception as e:
    print("Error during ollama.chat:", e)