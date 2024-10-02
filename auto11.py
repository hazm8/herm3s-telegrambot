import requests
import json
import base64
import time
import random
import string
import os
from lamachat import get_ollama_response
# Set the URL for the API
def auto_gen (Input, user_chat):
    url = "http://192.168.0.166:7861/sdapi/v1/txt2img"
    prompt = get_ollama_response(model = "CapBot",  char_chat=Input , user_chat=user_chat,)
    pre_prompt ="((high quality digital artwork masterpiece, high quality)),hermes, masculine god, greek god, god of magic and technology, winged helmet"
    re_prompt = pre_prompt + " " + prompt + "8k, unity render,character artwork"
    #print(prompt)




    override_settings = {}
    override_settings["CLIP_stop_at_last_layers"] : 2 # or whatever you need
    # Define the payload (prompt, settings, etc.)
    payload = {
        "prompt": f"{re_prompt}",
        "negative_prompt":"BadDream, badhandv4",
        "steps": 9,
        "width": 512,
        "height": 768,
        "cfg_scale":1.5,
        "sampler_index": "LCM",
        "scheduler" : "Exponential",
        "batch_size": 1,
        "override_settings": override_settings,
        "override_settings_restore_afterwards": False,
        "alwayson_scripts": {
      }
    }

    # Send the POST request
    response = requests.post(url, json=payload)

    # Parse the response (the generated image data is in 'images' field)
    result = response.json()

    # Print the result or save the image (base64 encoded)
    #print(result)

    # Optionally, save the image to a file
    if 'images' in result:
        img_data = result['images'][0]

        with open("output.png", "wb") as f:
            f.write(base64.b64decode(img_data))
            pic = 'output.png'
            new_pic = save_as(pic)
            return new_pic



def save_as(img):
    random_int = random.randint(1000, 9999)  # Generate a random integer
    random_str = ''.join(random.choices(string.ascii_lowercase, k=5))  # Generate a random string
    rnd_name = f"{random_int}_{random_str} " + ".png"
    try:    # Rename the file
        os.rename(img, rnd_name)
        #target_directory ="/mnt/sentinel/a1111/stable-diffusion-webui/output"
        #new_file_path = os.path.join(target_directory, rnd_name)
        #shutil.move(rnd_name, new_file_path)
        print(f"Successfully renamed '{img}' to '{rnd_name}'")
    except FileNotFoundError:
        print(f"The file '{img}' does not exist.")
    except PermissionError:
        print("You do not have permission to rename this file.")
    except OSError as error:
        print(f"Error: {error}")
    return rnd_name
