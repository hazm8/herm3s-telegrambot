# Herm3s - Telegram AI chatbot

Using the Nous Research [Hermes3](https://nousresearch.com/hermes3/) llm this is chatbot emulates Hermes, the Greek god of messages and heralds.

A locally hosted AI chatbot intergrated into a telegram bot.
Requires running [Ollama](https://github.com/ollama/ollama) and [Auto1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) locally.
![auto1111 images](https://github.com/hazm8/herm3s-telegrambot/blob/main/images/photo_2024-10-04_17-06-26.jpg)
## Installing
#### Linux Install
```
git clone https://github.com/hazm8/herm3s-telegrambot.git
cd herm3s-telegrambot
python3 -m venv venv
source venv/bin/activate
pip install pyTelegramBotAPI
```

## Setup
1. Create a Telegram Bot with @BotFather
2. Copy Token and Chat Id into secret.py
3. Edit your local URL in lamachat.py and auto11.py
4. Set Auto1111 to run with the flags: ``` --api --listen --port 7861 ```
5. Create ollama model using the Herems3 gguf model. I downloaded it [here](https://huggingface.co/bartowski/Hermes-3-Llama-3.1-8B-GGUF).
6. Create the herm3s ollama model using the model file ``` ollama create hermes3 -f hermes3.mf ```
7. create the Caption Bot using ``` ollama create CapBot -f CapBot.mf ```

## Running
1. Verify that the ollama api is running by visiting ``` http://localhost:11434 ```
2. Launch Auto111
3. In your your /herm3s/ directory run:
```
source /venv/bin/activate
python3 herm3s.py
```

## Models

- [Hermes3](https://nousresearch.com/hermes3/)
- [DreamShaper8 LCM](https://civitai.com/models/4384?modelVersionId=252914)



