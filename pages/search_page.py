# page2.py
import streamlit as st
from PIL import Image
from icrawler.builtin import BingImageCrawler
from icrawler.builtin import GoogleImageCrawler
import os, shutil, glob



def fetch_image_urls(keyword, max_num=5):
    folder_base = os.path.dirname(os.path.abspath(__file__))
    crawler = GoogleImageCrawler(storage={"root_dir": folder_base + '/image_crawling'})
    crawler.crawl(keyword=keyword, max_num=max_num)

    urls = []
    for path in crawler.storage.files.values():
        urls.append(path['file_url'])

    return urls

# 例：'puppy'の画像を10枚取得
urls = fetch_image_urls('puppy', 10)
for url in urls:
    print(url)


# st.title("クローリング")
def crawling(keyword):
    folder_base = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(folder_base + "/image_crawling"):
        shutil.rmtree(folder_base + "/image_crawling")
    crawler = BingImageCrawler(storage = {'root_dir' : folder_base + '/image_crawling'})
    crawler.crawl(keyword = keyword, max_num = 5)
    print("検索が完了しました")

def make_image_search():
    st.title("画像をキーワードで検索")
    keyword = st.text_input("検索ワードを入力してください", help="例：lego")
    if st.button("検索"):
        crawling(keyword)
        st.write("検索が完了しました")
        files = glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/image_crawling/*.jpg")
        for i, file in enumerate(files):
            img = Image.open(file)
            st.image(img, caption=f"画像{i+1}")

if __name__ == "__main__":
    # print(fetch_image_urls('lego'))
    make_image_search()

