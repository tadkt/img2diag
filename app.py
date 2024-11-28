import streamlit as st
# from openai import OpenAI
# import base64
import os
from PIL import Image
from img2diag import img2jsonl, process_jsonl_str, jsonl2graph
from dotenv import load_dotenv

load_dotenv()

def main():
    st.title("DENSO OCR")
    st.write("Upload image:")

    image_file = st.file_uploader("Upload image:", type=["jpg", "png", "jpeg"])
    if image_file:
        try:
            # Save the uploaded file to a temporary path
            temp_path = os.path.join("temp", image_file.name)
            os.makedirs("temp", exist_ok=True)
            
            # Write the uploaded file to the temp path
            with open(temp_path, "wb") as f:
                f.write(image_file.getbuffer())
            st.write("File uploaded successfully:", temp_path)
            diag_file = st.text_input(label="Enter Output name: (.jpg)")
            jsonl_str = img2jsonl(image_path=temp_path)
            st.write("JSONL string:", jsonl_str)
            jsonl_content = process_jsonl_str(json_str=jsonl_str)
            st.write("Processed JSONL content:", jsonl_content)
            # st.write("Generated diagram path:", diag_path)
            diag_path = jsonl2graph(jsonl_content, diag_name=diag_file)
            st.image(diag_path)
        except Exception as e:
            print(f"Error occurs: {e}")

if __name__ == "__main__":
    main()


