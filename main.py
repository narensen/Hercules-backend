from google import genai
from fastapi import FastAPI
from services import *

app = FastAPI()
client = genai.Client()

if __name__ == "__main__":
    
    print(generate_ai_image("A muscular man doing a bicep curl in a gym with dumbbells, wearing a blue tank top and black shorts, with sweat glistening on his skin, high detail, realistic lighting, 4k resolution"))