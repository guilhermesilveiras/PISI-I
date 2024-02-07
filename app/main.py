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
            return f'A temperatura atual em {cidade} é {temperatura}ºC.'

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
    MDRaisedButton:
        text: "Como está o tempo?"
        on_release: app.update_weather(city_input.text)
        pos_hint: {"center_x": 0.5}
        md_bg_color: 1, 0.5, 0, 1
    MDLabel:
        text: app.weather
        halign: "center"
        font_size: "18sp"
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
""")

    def update_weather(self, city_name):
        weather_app = WeatherApp()
        self.weather = weather_app.pegar_clima(city_name)

MainApp().run()