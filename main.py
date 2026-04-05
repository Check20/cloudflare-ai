import os
import requests
import sys

# Credenciales desde variables de entorno
ACCOUNT_ID = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")

def run_ai_prompt(prompt):
    if not ACCOUNT_ID or not AUTH_TOKEN:
        print("Critical Error: Missing Environment Variables (ACCOUNT_ID or AUTH_TOKEN)")
        sys.exit(1)

    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/google/gemma-4-26b-a4b-it"
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    payload = {
        "messages": [
            {"role": "system", "content": "You are a specialized technical assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    user_prompt = "Explain the benefits of PEP-8 for scalable Python projects"
    result = run_ai_prompt(user_prompt)
    print(result)
