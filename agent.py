import requests
import json

API_KEY = "SUA_CHAVE_AQUI"  # Coloque sua chave Copilot ou OpenAI
URL = "https://api.openai.com/v1/chat/completions"  # Endpoint do modelo

def agente_terminal():
    print("Agente IA iniciado. Digite 'sair' para encerrar.")
    while True:
        prompt = input("Você: ")
        if prompt.lower() == "sair":
            break

        payload = {
            "model": "gpt-4",
            "messages": [{"role": "user", "content": prompt}]
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.post(URL, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            resposta = response.json()["choices"][0]["message"]["content"]
            print("Agente:", resposta)
        else:
            print("Erro:", response.text)

if __name__ == "__main__":
    agente_terminal()
