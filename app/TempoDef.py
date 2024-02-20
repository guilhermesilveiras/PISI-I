import requests
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.font_definitions import theme_font_styles



kv = """
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    Image:
        source: "icons/locationdef3.png"
        size_hint: .1, .1
        pos_hint: {"center_x": .5, "center_y": .95}
    MDLabel:
        id: location
        text: ""
        pos_hint: {"center_x": .5, "center_y": .89}
        halign: "center"
        font_size: "20sp"
        font_name: "Roboto"
    Image:
        id: weather_image
        source: ""
        pos_hint: {"center_x": .5, "center_y": .77}
    MDLabel:
        id: temperature
        text: ""
        markup: True
        pos_hint: {"center_x": .5, "center_y": .62}
        halign: "center"
        font_size: "60sp"
        font_name: "Roboto"
    MDLabel:
        id: weather
        text: ""
        pos_hint: {"center_x": .5, "center_y": .54}
        halign: "center"
        font_size: "20sp"
        font_name: "Roboto"
    MDFloatLayout:
        pos_hint: {"center_x": .25, "center_y": .4}
        size_hint: .22, .1
        Image:
            source: "icons/umidadedef.png"
            pos_hint: {"center_x": .1, "center_y": .5}
        MDLabel:
            id: humidity
            text: ""
            markup: True
            pos_hint: {"center_x": 1, "center_y": .7}
            font_size: "25sp"
            font_name: "Roboto"
        MDLabel:
            text: "Umidade"
            markup: True
            pos_hint: {"center_x": 1, "center_y": .3}
            font_size: "25sp"
            font_name: "Roboto"
    MDFloatLayout:
        pos_hint: {"center_x": .7, "center_y": .4}
        size_hint: .22, .1
        Image:
            source: "icons/winddef.png"
            pos_hint: {"center_x": .1, "center_y": .5}
        MDLabel:
            id: wind_speed
            text: ""
            markup: True
            pos_hint: {"center_x": 1.1, "center_y": .7}
            font_size: "25sp"
            font_name: "Roboto"
        MDLabel:
            text: "Ventos"
            markup: True
            pos_hint: {"center_x": 1.1, "center_y": .3}
            font_size: "25sp"
            font_name: "Roboto"
    MDFloatLayout:
        size_hint_y: .3
        canvas:
            Color:
                rgb: rgba(255, 255, 255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [10, 10, 0, 0]
        MDFloatLayout:
            pos_hint: {"center_x": .5, "center_y": .71}
            size_hint: .9, .32
            canvas:
                Color:
                    rgb: rgba(173, 216, 230, 1)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [6]
            TextInput:
                id: city_name
                hint_text: "Digite o nome da cidade"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y": .5}
                height: self.minimum_height
                multiline: False
                font_name: "Roboto"
                font_size: "20sp"
                hint_text_color: 1, 1, 1, 1
                foreground_color: 1, 1, 1, 1
                background_color: 1, 1, 1, 0 
                padding: 15
                cursor_color: 1, 1, 1, 1
                cursor_width: 2
        Button:
            text: "Como está o tempo?"
            font_name: "Roboto"
            font_size: "20sp"
            size_hint: .9, .32
            pos_hint: {"center_x": .5, "center_y": .29}
            background_color: 1, 1, 1, 0
            color: rgba(255, 255, 255, 224)
            on_release: app.search_weather()
            canvas.before:
                Color:
                    rgb: 1, 1, 1, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [6]
                Color:
                    rgb: rgba(173, 216, 230, 1)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [6]

"""

class WeatherApp(MDApp):


    

    api_key = 'b7c6eaa62d6e881ee25b2c42994ce00a'


    def build(self):
        return Builder.load_string(kv)
    
    def pegar_clima(self, cidade):
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={'b7c6eaa62d6e881ee25b2c42994ce00a'}"
            response = requests.get(url)
            x = response.json()
            if x["cod"] != "404":
                temperature = round(x["main"]["temp"]-273.15)
                humidity = x["main"]["humidity"]
                weather = x["weather"][0]["main"]
                id = str(x["weather"][0]["id"])
                wind_speed = round(x["wind"]["speed"]*18/5)
                location = x["name"] + ", " + x["sys"]["country"]
                self.root.ids.temperature.text = f"[b]{temperature}[/b]°C"
                self.root.ids.weather.text = str(weather)
                self.root.ids.humidity.text = f"{humidity}%"
                self.root.ids.wind_speed.text = f"{wind_speed}Km/h"
                self.root.ids.location.text = location
                self.root.ids.weather_image.source = "icons/nuvens.png"

            else:
                self.root.ids.temperature.text = "Cidade não encontrada!"
        except requests.ConnectionError:
            self.root.ids.temperature.text = "Sem conexão com a internet"
    
    def search_weather(self):
        city_name = self.root.ids.city_name.text
        if city_name.isdigit() or city_name == "":
            print("Digite um nome de cidade válido!")
        else:
            self.pegar_clima(city_name)

LabelBase.register(name="Roboto", fn_regular="fonts/Roboto-Regular.ttf")

if __name__ == "__main__":
    WeatherApp().run()