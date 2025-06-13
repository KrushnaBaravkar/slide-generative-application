import requests

def script_generator(prompt):
    url = "http://127.0.0.1:11434 /api/chat"

    payload = {
        "model": "llama3.2",  # or "llama3" if that's what you pulled
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data["message"]["content"]
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Exception occurred: {e}"

print(script_generator("Write a motivational speech for students."))
