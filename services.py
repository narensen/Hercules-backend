from fastapi import FastAPI
from google import genai
import json
from dotenv import load_dotenv
import os
from google.genai import types
from PIL import Image

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=GOOGLE_API_KEY)

def prompt_structure(prompt: str) -> str:

    json_structure = {
        "exercise_name": "",
        "description": "Like what it is how to perform it and how many sets and reps",
        "image_prompt" : "A detailed realistic description for an AI image generator to create an image of the exercise being performed",
        
    }

    final_prompt = f"""Create a detailed AI-generated prompt structure based on the following input: {prompt} 
    the output should be in json format in this way dont type anything else just the json alone+ {json_structure}"""

    return final_prompt

def generate_ai_workout_plan(prompt: str) -> str:

    final_prompt = prompt_structure(prompt)

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=final_prompt,
    )
    
    print(response.text)
    new_response = response.text
    new_response = new_response.replace('```', '')
    new_response = new_response.replace('json', '')
    return json.loads(new_response)

def generate_ai_image(prompt: str) -> str:

    response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
)

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image.save("generated_image.png")