
import json
import requests
import time

def get_ollama_response(model, char_chat, user_chat):
    # Define the URL for the Ollama API
    url = "http://192.168.1.109:11434/api/chat"

    # Set up headers and data payload
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": f"""Write a flawless stable diffusion prompt of a Hermes the acient greek God of messages and heralds. Incoperate themes of technology,  and mysticism , Use the given context and reference locations,  Use the following as context for the prompt Assistant:{char_chat}, User{user_chat}.  """},

        ],
        "stream": False  # Change to True if you want streaming responses

    }


    response = requests.post(url, headers=headers, data=json.dumps(data))
    json_data = response.json()
    content = json_data.get('message', {}).get('content', "No content found")
    print("Content:", content)
    return content

        #return response.json().get(["messages"]["content"], "No response text found.")
        #print(response.json().get("response", "No response text found."))



def get_hermes_response(prompt, model, user_chat):
    # Define the URL for the Ollama API
    url = "http://192.168.1.109:11434/api/generate"

    # Set up headers and data payload
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False  # Change to True if you want streaming responses

    }


    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the request was successful
    if response.status_code == 200:
        print (response.json().get("response", "No response text found."))
        return response.json().get("response", "No response text found.")
    else:
        return f"Error: {response.status_code}"


def get_auto_response(model="hermes3"):
    # Define the URL for the Ollama API
    url = "http://192.168.0.166:11434/api/generate"

    # Set up headers and data payload
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": """ Your job is a study companion/motivational tutor. You must remind the user to stay focused on studying for the CompTIA A+ core 2 exam! Please provide a motivational reminder and  a question based on the A+ core 2 course  objectives: (Operating systems, Security, Software troubleshooting, Operational procedures) """,
        "stream": False,  # Change to True if you want streaming responses
    }


    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the request was successful
    if response.status_code == 200:
        return response.json().get("response", "No response text found.")
    else:
        return f"Error: {response.status_code}"
