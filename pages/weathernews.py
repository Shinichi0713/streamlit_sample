import streamlit as st
import requests, json, os
from transformers import LukeForSequenceClassification, MLukeTokenizer

api_key = "88888"

def get_weather(city: str):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    weather_data = response.json()
    return weather_data

def get_image_satellite(date_string: str):

    endpoint = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=" + date_string
    response = requests.get(endpoint)
    print(response.content)
    str_data = response.content.decode('utf-8')
    json_data = json.loads(str_data)
    url = json_data['url']
    response = requests.get(url)
    image = response.content
    dir_current = os.path.dirname(__file__)
    with open(dir_current + "/sattelite.png", "wb") as fp:
        fp.write(image)
    return url

def display_weather():
    st.title("天気情報")
    city = st.text_input('都市名を入力してください:')
    if city:
        weather_data = get_weather(city)
        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        
        st.write(f"主な天気: {main_weather}")
        st.write(f"詳細: {description}")
        st.write(f"温度: {temp}K")
        st.write(f"温度: {temp - 273.15:.2f}℃")
        st.write(f"湿度: {humidity}%")

# display_weather()
print(get_weather('Washington'))
