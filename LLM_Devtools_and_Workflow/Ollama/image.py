import os
import ollama

print("Hello, Ollama!")
print("Current directory files:", os.listdir('.'))

try:
    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': 'What is in this image?',
            'images': ['image.jpg']  # Make sure this file exists
        }]
    )
    print("Response received:")
    print(response)
except Exception as e:
    print("Error during ollama.chat:", e)