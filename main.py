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
        response = requests.get(complete_url)
        data = response.json()
        if data.get('success') is False:
            return 'Cidade não encontrada.'
        else:
            temperatura = data.get('current').get('temperature')
            return f'A temperatura atual em {cidade} é {temperatura}ºC.'


    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Olá! Seja bem vindo ao "Como está o tempo?", o aplicativo que te informa a leitura do tempo atual!')
        self.textinput = TextInput(text='Digite a cidade aqui')
        button = Button(text='Como está o tempo?')
        button.bind(on_press=self.update_label)
        layout.add_widget(self.label)
        layout.add_widget(self.textinput)
        layout.add_widget(button)
        return layout
    
    def update_label(self, instance):
        city = self.textinput.text
        weather = self.pegar_clima(city)
        self.label.text = weather

if __name__ == '__main__':
    WeatherApp().run()