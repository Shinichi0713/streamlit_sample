# page3.py
import streamlit as st
import os, glob

dir_base = os.path.dirname(os.path.dirname(__file__)).replace('\\','/')
dir_store = "/pages/image_txt"

def main():
    st.title("画像と説明の投稿アプリ")
    print(dir_base + dir_store)
    # 画像のアップロード
    uploaded_image = st.file_uploader("画像をアップロードしてください", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        st.image(uploaded_image, caption="アップロードされた画像")

        # 画像の説明
        image_description = st.text_input("画像の説明を入力してください")
        st.write(f"画像の説明: {image_description}")

        # 画像と説明を保存
        if st.button('保存'):
            save_image_and_description(uploaded_image, image_description)

def save_image_and_description(image, description):
    # os.mkdir(dir_base + dir_store + "/image")
    # os.mkdir(dir_base + dir_store + "/txt")
    files = glob.glob(dir_base + dir_store + "/image/*")
    number_files = len(files)
    image_path = f"{dir_base + dir_store }/image/{number_files}.png"
    txt_path = f"{dir_base + dir_store }/txt/{number_files}.txt"
    print(image_path)
    with open(image_path, "wb") as f:
        f.write(image.getbuffer())
    with open(txt_path, "w") as f:
        f.write(description)

if __name__ == "__main__":
    main()

