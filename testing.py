
import streamlit as st
st.title("GPT Index Creator")
# from llama_index import GPTSimpleVectorIndex
# from pathlib import Path
# from gpt_index import download_loader
# import json
# import openai
# import os
# from PIL import Image


# os.environ['OPENAI_API_KEY'] = "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"


# def create_index(pdf_file):
#     PDFReader = download_loader("PDFReader")
#     loader = PDFReader()

#     # Create a directory to store the uploaded files
#     upload_dir = Path('uploads')
#     upload_dir.mkdir(exist_ok=True)

#     pdf_path = upload_dir / pdf_file.name
#     pdf_path.write_bytes(pdf_file.read())
#     documents = loader.load_data(file=pdf_path)

#     index = GPTSimpleVectorIndex.from_documents(documents)

#     index_filename = upload_dir / f'index_{pdf_path.stem}.json'
#     index.save_to_disk(index_filename)

#     return index_filename


# image = Image.open("C:\\Users\\WalkingTree\\Desktop\\App\\streamlit\\images\\ecai.png")
# st.image(image, caption='')

# st.title("GPT Index Creator")

# # Create a dropdown menu for single/multiple files
# upload_option = st.selectbox("Choose upload option", ["Single file", "Multiple files"])

# if upload_option == "Single file":
#     # Upload a single file
#     pdf_files = st.file_uploader("Upload PDF file", type="pdf")
#     if pdf_files is not None:
#         index_filename = create_index(pdf_files)
#         st.write(f"Index file created: {index_filename}")
#         # Add a unique key to the button
#         button_key = f"{pdf_files.name}-button"
#         if st.button("Download Index", key=button_key):
#             st.download_button(
#                 label="Download Index",
#                 data=open(index_filename, 'rb').read(),
#                 file_name=f"index_{pdf_files.name}.json",
#                 mime="application/json"
#             )

# elif upload_option == "Multiple files":
#     # Upload multiple files
#     pdf_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
#     if pdf_files is not None:
#         for pdf_file in pdf_files:
#             index_filename = create_index(pdf_file)
#             st.write(f"Index file created: {index_filename}")
#             # Add a unique key to the button
#             button_key = f"{pdf_file.name}-button"
#             if st.button("Download Index", key=button_key):
#                 st.download_button(
#                     label="Download Index",
#                     data=open(index_filename, 'rb').read(),
#                     file_name=f"index_{pdf_file.name}.json",
#                     mime="application/json"
#                 )
# image = Image.open("C:\\Users\\WalkingTree\\Desktop\\App\\streamlit\\images\\WTT Logo.jpg")
# st.image(image)
