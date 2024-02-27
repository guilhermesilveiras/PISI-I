import requests
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.progressbar import MDProgressBar
from kivy.clock import Clock

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
        pos_hint: {"center_x": .5, "center_y": .79}
    MDLabel:
        id: temperature
        text: ""
        markup: True
        pos_hint: {"center_x": .5, "center_y": .68}
        halign: "center"
        font_size: "60sp"
        font_name: "Roboto"
    MDLabel:
        id: weather
        text: ""
        pos_hint: {"center_x": .5, "center_y": .60}
        halign: "center"
        font_size: "20sp"
        font_name: "Roboto"
    
    MDFloatLayout:
        pos_hint: {"center_x": .7, "center_y": .5}
        size_hint: .22, .1
        Image:
            source: "icons/hightemp.png"
            pos_hint: {"center_x": .1, "center_y": .5}
        MDLabel:
            id: temp_max
            text: ""
            markup: True
            pos_hint: {"center_x": 1, "center_y": .7}
            font_size: "25sp"
            font_name: "Roboto"
        MDLabel:
            text: "Temp. Máxima"
            markup: True
            pos_hint: {"center_x": 1, "center_y": .3}
            font_size: "25sp"
            font_name: "Roboto"
    MDFloatLayout:
        pos_hint: {"center_x": .25, "center_y": .5}
        size_hint: .22, .1
        Image:
            source: "icons/lowtemp.png"
            pos_hint: {"center_x": .1, "center_y": .5}
        MDLabel:
            id: temp_min
            text: ""
            markup: True
            pos_hint: {"center_x": 1, "center_y": .7}
            font_size: "25sp"
            font_name: "Roboto"
        MDLabel:
            text: "Temp. Mínima"
            markup: True
            pos_hint: {"center_x": 1, "center_y": .3}
            font_size: "25sp"
            font_name: "Roboto"
    
    MDFloatLayout:
        pos_hint: {"center_x": .25, "center_y": .35}
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
        pos_hint: {"center_x": .7, "center_y": .35}
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

    MDProgressBar:
        id: progress_bar
        size_hint: None, None
        size: dp(150), dp(7)
        pos_hint: {'center_x': .5, 'center_y': .025}
        color: 0, 0.6, 1, 1  # Azul claro
"""

class WeatherApp(MDApp):
    api_key = 'b7c6eaa62d6e881ee25b2c42994ce00a'

    def build(self):
        return Builder.load_string(kv)

    def pegar_clima(self, cidade):
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={self.api_key}"
            response = requests.get(url)
            x = response.json()
            if x["cod"] != "404":
                temperature = round(x["main"]["temp"]-273.15)
                temp_max = round(x["main"]["temp_max"] - 273.15)
                temp_min = round(x["main"]["temp_min"] - 273.15)
                humidity = x["main"]["humidity"]
                weather = x["weather"][0]["main"]
                id = str(x["weather"][0]["id"])
                wind_speed = round(x["wind"]["speed"]*18/5)
                location = x["name"] + ", " + x["sys"]["country"]
                self.root.ids.temperature.text = f"[b]{temperature}[/b]°C"
                self.root.ids.temp_max.text = f"[b]{temp_max}[/b]°C"
                self.root.ids.temp_min.text = f"[b]{temp_min}[/b]°C"
                self.root.ids.weather.text = str(weather)
                self.root.ids.humidity.text = f"{humidity}%"
                self.root.ids.wind_speed.text = f"{wind_speed}Km/h"
                self.root.ids.location.text = location
                
                if id == '800':
                    self.root.ids.weather_image.source = "icons/sun5.png"
                elif '200' <= id <= '232':
                    self.root.ids.weather_image.source = "icons/storm.png"
                elif '300' <= id <= '321' or '500' <= id <= '531':
                    self.root.ids.weather_image.source = "icons/rain3.png"
                elif '600' <= id <= '622':
                    self.root.ids.weather_image.source = "icons/snow2.png"
                elif '701' <= id <= '781':
                    self.root.ids.weather_image.source = "icons/nevoa.png"
                elif '801' <= id <= '804':
                    self.root.ids.weather_image.source = "icons/cloudsdef.png"



            else:
                self.root.ids.temperature.text = "Cidade não encontrada!"
        except requests.ConnectionError:
            self.root.ids.temperature.text = "Sem conexão com a internet"

    def search_weather(self):
        city_name = self.root.ids.city_name.text
        if city_name.isdigit() or city_name == "":
            print("Digite um nome de cidade válido!")
        else:
            # reiniciando a barra de progressão?
            self.root.ids.progress_bar.value = 0
            self.root.ids.progress_bar.color = (0, 0.6, 1, 1)  # Azul claro
            self.root.ids.progress_bar.start()
            # clock.schedule ver documentação depois
            Clock.schedule_once(self.update_progress_bar_once)
            # chama função pegar_clima
            self.pegar_clima(city_name)

    def update_progress_bar_once(self, dt):
        Clock.schedule_interval(self.update_progress_bar, 0.05)  # atualiza a cada 0.05 segundos

    def update_progress_bar(self, dt):
    # atualiza a barra com valores de 0 a 100
        progress = self.root.ids.progress_bar.value
        if progress < 100:
            progress += 10  # velocidade de carregamento da barra!!!
            self.root.ids.progress_bar.value = progress
            return True 
        return False  # para de chamar a função


LabelBase.register(name="Roboto", fn_regular="fonts/Roboto-Regular.ttf")

if __name__ == "__main__":
    WeatherApp().run()
