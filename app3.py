import requests
import os

# Retrieve the API key from the environment variables
api_key = os.getenv("MISTRAL_API_KEY")

# Define the URL and headers
url = "https://codestral.mistral.ai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {api_key}",
}

# Define the data payload
data = {
    "model": "codestral-latest",
    "messages": [{"role": "user", "content": "Write a function for fibonacci"}],
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Check the response status and print the response content
if response.status_code == 200:
    response_data = response.json()
    print(response_data["choices"][0]["message"]["content"])

else:
    print(f"Error: {response.status_code}")
    print(response.text)
