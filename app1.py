import requests
import os

# Make sure to set your API key as an environment variable
api_key = os.getenv("MISTRAL_API_KEY")

url = "https://codestral.mistral.ai/v1/fim/completions"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {api_key}",
}
data = {
    "model": "codestral-latest",
    "prompt": "def fibonacci(n: int):",
    "suffix": "n = int(input('Enter a number: '))\nprint(fibonacci(n))",
    "max_tokens": 8000,
    "temperature": 0,
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    # print("Response:", response.json())
    response_data = response.json()
    print(response_data["choices"][0]["message"]["content"])
else:
    print(f"Error: {response.status_code}")
    print(response.text)


print(
    f"""
{data["prompt"]}
{response_data["choices"][0]["message"]["content"]}
{data['suffix']}
      """
)
