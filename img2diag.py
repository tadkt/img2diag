from openai import OpenAI
import base64
import os
from PIL import Image
from dotenv import load_dotenv
from draw import jsonl2graph

load_dotenv()

# Imagefile = D:/Data Science stuffs/DENSO OCR/Ảnh chụp màn hình 2024-11-27 213311.png
def open_image():
    Imagefile = input("Enter the path of input image: ")
    return Imagefile

def process_jsonl_str(json_str):
    jsonl_content = json_str.split("```")[1]
    if jsonl_content.startswith("json\n"):
        jsonl_content = jsonl_content[4:]
    elif jsonl_content.startswith("jsonl\n"):
        jsonl_content = jsonl_content[5:]
    return f"{jsonl_content}\n"
    # return jsonl_content

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
                "text": "From this jsonl file reorganize the diagram structuredly centered at (0,0) to return a new json that contains (x1,y1),(x2,y2) rectangle coordinates for each node and corresponding (x1,y1), (x2,y2), (optional (x3,y3) for 2-line arrow) arrow coordinates for each arrow based on \"id_source\" and \"id_target\". Ensure that the beginning and ending of edges are connected to the edges of nodes, and if necessary, split arrows into two segments to create a perpendicular angle. Leave a bit of space between nodes so that the connections are visually clear. Make sure the resulting json does not contain any blank lines and follows the exact format below:\n{\"type\": \"node\", \"data\": {\"id\": \"str\", \"label\": \"str\", \"x1\": int, \"y1\": int, \"x2\": int, \"y2\": int}}\n{\"type\": \"arrow\", \"data\": {\"id\": \"str\", \"label\": \"str\", \"x1\": int, \"y1\": int, \"x2\": int, \"y2\": int, \"x3\": Optional[int], \"y3\": Optional[int]\"}}\nEnsure the output strictly adheres to the specified jsonl format and contains no additional text or metadata."
            },
        ],
        },
    ],temperature = 0
    )
    response2 = (response.choices[0].message.content)
    return response2

# def img2jsonl(image_path):
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
    response2 = response.choices[0].message.content
    return response2

def main():
    image_path = open_image()
    jsonl_str = img2jsonl(image_path=image_path)
    jsonl_content = process_jsonl_str(json_str=jsonl_str)
    jsonl2graph(jsonl_content, "hello.jpg")

if __name__ == "__main__":
    main()