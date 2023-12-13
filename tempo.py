import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class WeatherApp(App):

    def pegar_clima(self, cidade):
        api_key = 'c1617eb3022d2f85cf2920060284b1c5'
        base_url = 'http://api.weatherstack.com/'
        complete_url = f'{base_url}current?access_key={api_key}&query={cidade}' 