from PIL import Image
import requests
from io import BytesIO
from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv
import json
from fastapi import Response


""""<span style='color: rgb(255, 165, 0);'>This is line 1 text</span><br>\n"
    "<span style='color: rgb(255, 165, 0);'>This is line 2 text</span>"""""

app = FastAPI()
secret = "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"
@app.get("/bnw/")
async def blackandwhite(url: str, invert: int, plaintext: int):
    option = invert

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)

    dict_of_newlines = {}
    line = 0

    loaded_image = Image.open(BytesIO(response.content))
    width, height = loaded_image.size
    resized = loaded_image.resize((150, int(round(height/width * 150 * 0.55))))
    grayscale_image = resized.convert('L')
    width, height = grayscale_image.size

    string_to_print = ""
    
    def brightness_calculator(brightness):
        if option == 1:
            ascii_table = "@%#*+=-:. "
        elif option == 0:
            ascii_table = " .:-=+*#%@"
        
        max_val = len(ascii_table) - 1
        pos = int(round(brightness / 255 * max_val))
        return ascii_table[pos]


    for h in range(0, height):
        for w in range(0, width):
            brightness = grayscale_image.getpixel((w, h))
            char = brightness_calculator(brightness)
            string_to_print += char
        if plaintext == 0:
            dict_of_newlines[f"line{line}"] = string_to_print
            line += 1
            string_to_print = ""
        elif plaintext == 1:
            string_to_print += "\n"
        
    
    if plaintext:
        return Response(content=string_to_print, media_type="text/plain")
    else:
        return dict_of_newlines

@app.get("/ai/{message}")
async def AI(message: str):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {secret}",
        },
        data=json.dumps({
            "model": "openrouter/free",
            "messages": [
            {
                "role": "user",
                "content": f"Make an ASCII art of {message}, DO NOT INCLUDE ANYTHING ELSE"
            }
            ]
        })
        )
    data = response.json()
    ascii_art = data["choices"][0]["message"]["content"]

    return Response(content=ascii_art, media_type="text/plain")

@app.get("/colored/")
async def colored(url: str, invert: int):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    loaded_image = Image.open(BytesIO(response.content))
    width, height = loaded_image.size
    resized = loaded_image.resize((200, int(round(height/width * 200 * 0.65))))
    width, height = resized.size

    string_to_print = """<pre style="font-family: monospace; line-height: 1;">"""

    def brightness_calculator(r, g, b):
        if invert == 1:
            ascii_table = "@%#*+=-:. "
        elif invert == 0:
            ascii_table = " .:-=+*#%@"
        
        brightness = int(round(0.2126*r + 0.7152*g + 0.0722*b))
        max_val = len(ascii_table) - 1
        pos = int(round(brightness / 255 * max_val))
        return ascii_table[pos]
    
    for h in range(0, height):
        for w in range(0, width):
            pixel_rgb = resized.getpixel((w, h))
            r, g, b = pixel_rgb[0], pixel_rgb[1], pixel_rgb[2]
            char = brightness_calculator(r, g, b)
            string_to_print += f"""<span style='color: rgb({r}, {g}, {b});'>{char}</span>"""
        string_to_print += "\n"
    
    string_to_print += "</pre>"

    return Response(content=string_to_print, media_type="text/html")
