import requests
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty

class WeatherApp:
    def pegar_clima(self, cidade):
        api_key = 'c1617eb3022d2f85cf2920060284b1c5'
        base_url = 'http://api.weatherstack.com/'
        complete_url = f'{base_url}current?access_key={api_key}&query={cidade}'
        response = requests.get(complete_url)
        data = response.json()
        if data.get('success') is False:
            return 'Cidade não encontrada.'
        else:
            temperatura = data.get('current').get('temperature')
            umidade = data.get('current').get('humidity')
            velocidade_vento = data.get('current').get('wind_speed')
            weather_icons_url = data.get('current').get('weather_icons')[0]
            return f'A temperatura atual em {cidade} é {temperatura}ºC, a umidade é de {umidade}% e a velocidade dos ventos é de {velocidade_vento} km/h.'

class MainApp(MDApp):
    weather = StringProperty("")

    def build(self):
        return Builder.load_string("""
BoxLayout:
    orientation: 'vertical'
    MDTextField:
        id: city_input
        hint_text: "Informe o nome da cidade"
        pos_hint: {"center_x": 0.5}
        text: ""
    MDRaisedButton:
        text: "Como está o tempo?"
        on_release: app.update_weather(city_input.text)
        pos_hint: {"center_x": 0.5}
        md_bg_color: 0, 0.7, 1, 0.9

    MDLabel:
        text: app.weather
        halign: "center"
        font_size: "18sp"
        theme_text_color: "Custom"
        text_color: 0, 0.7, 1, 0.9
""")

    def update_weather(self, city_name):
        weather_app = WeatherApp()
        self.weather = weather_app.pegar_clima(city_name)

MainApp().run()