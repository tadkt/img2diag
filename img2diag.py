from openai import OpenAI
import base64
import os
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

# Imagefile = D:/Data Science stuffs/DENSO OCR/Ảnh chụp màn hình 2024-11-27 213311.png
def open_image():
    Imagefile = input("Enter the path of input image: ")
    return Imagefile

def img2jsonl(image_path):
    client = OpenAI()

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Getting the base64 string
    base64_image = encode_image(image_path)


    # Call no_1
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Define elements and connections based on this Vietnamese user's diagram, take into consideration that this diagram is made in a Vietnamese factory setting to correct any context mistake. Transcribe to jsonl format:\n{\"type\": \"node\", \"data\": {\"id\": str, \"label\": str, \"x\": int, \"y\": int}}\n{\"type\": \"node\", \"data\": {\"id\": str, \"label\": str, \"x\": int, \"y\": int}}\n{\"type\": \"arrow\", \"data\": {\"source\": str, \"target\": str,\"label\": str}}",
            },
            {
            "type": "image_url",
            "image_url": {
                "url":  f"data:image/jpeg;base64,{base64_image}"
            },
            },
        ],
        }
    ],
    )
    response1 = repr(response.choices[0].message.content)

    # Call no_2
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Define elements and connections based on this Vietnamese user's diagram, take into consideration that this diagram is made in a Vietnamese factory setting to correct any context mistake. Transcribe to jsonl format:\n{\"type\": \"node\", \"data\": {\"id\": str, \"label\": str}}\n{\"type\": \"node\", \"data\": {\"id\": str, \"label\": str}}\n{\"type\": \"arrow\", \"data\": {\"id\": str, \"id_source\": str, \"id_target\": str,\"label\": str}}",
            },
            {
            "type": "image_url",
            "image_url": {
                "url":  f"data:image/jpeg;base64,{base64_image}"
            },
            },
        ],
        },
        {
        "role": "assistant",
        "content": [{ "type": "text", "text": response1 }]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "From this jsonl file reorganize the diagram structuredly centered at (0,0) to return new json that contains (x1,y1),(x2,y2) rectangle cordinate for each node and corresponding (x1,y1), (x2,y2), (optional (x3,y3) for 2-line arrow) arrow cordinate for each arrow base on \"id_source\" and \"id_target\". Example format below:\n{\"type\": \"node\", \"data\": {\"id\": \"str\", \"label\": \"str\", \"x1\": \"int\", \"y1\": \"int\", \"x2\": \"int\", \"y2\": \"int\"}}\n{\"type\": \"node\", \"data\": {\"id\": \"str\", \"label\": \"str\", \"x1\": \"int\", \"y1\": \"int\", \"x2\": \"int\", \"y2\": \"int\"}}\n{\"type\": \"arrow\", \"data\": {\"id\": \"str\", \"label\": \"str\", \"x1\": \"int\", \"y1\": \"int\", \"x2\": \"int\", \"y2\": \"int\", \"x3\": \"Optional[int]\", \"y3\": \"Optional[int]\"}}"
            },   
        ],
        },
    ],
    )
    response2 = repr(response.choices[0].message.content)
    return response2

def main():
    image_path = open_image()
    jsonl_str = img2jsonl(image_path=image_path)
    print(jsonl_str)

if __name__ == "__main__":
    main()