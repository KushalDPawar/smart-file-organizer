import streamlit as st
import os
import shutil

st.set_page_config(page_title="File Organizer", layout="centered")

st.title("📁 File Organizer by Extension")
st.write("Organize files in a folder automatically by their extensions.")

folder_path = st.text_input("Enter full folder path:")

if st.button("Organize Files"):
    if not folder_path:
        st.error("Please enter a folder path.")
    elif not os.path.exists(folder_path):
        st.error("Folder does not exist.")
    else:
        files_moved = 0

        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                ext = file.split(".")[-1]

                ext_folder = os.path.join(folder_path, ext.upper())
                os.makedirs(ext_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(ext_folder, file))
                files_moved += 1

        st.success(f"✅ Done! Organized {files_moved} files.")
