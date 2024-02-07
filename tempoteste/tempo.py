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

    def velocidade_vento(self, cidade):
        api_key = 'c1617eb3022d2f85cf2920060284b1c5'
        base_url = 'http://api.weatherstack.com/'
        complete_url = f'{base_url}current?access_key={api_key}&query={cidade}'
        response = requests.get(complete_url)
        data = response.json()
        if data.get('success') is False:
            return 'Cidade não encontrada.'
        else:
            wind_speed = data.get('current').get('wind_speed')
            return f'A velocidade do vento em {cidade} é {wind_speed} km/h.'

    def umidade(self, cidade):
        api_key = 'c1617eb3022d2f85cf2920060284b1c5'
        base_url = 'http://api.weatherstack.com/'
        complete_url = f'{base_url}current?access_key={api_key}&query={cidade}'
        response = requests.get(complete_url)
        data = response.json()
        if data.get('success') is False:
            return 'Cidade não encontrada.'
        else:
            humidity = data.get('current').get('humidity')
            return f'A umidade em {cidade} é {humidity}%.'

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Olá! Seja bem vindo ao "Como está o tempo?", o aplicativo que te informa a leitura do tempo atual!')
        self.textinput = TextInput(text='Digite a cidade aqui')
        button_temp = Button(text='Como está o tempo?')
        button_temp.bind(on_press=self.update_label_temp)
        button_wind = Button(text='Velocidade dos ventos')
        button_wind.bind(on_press=self.update_label_wind)
        button_humidity = Button(text='Umidade')
        button_humidity.bind(on_press=self.update_label_humidity)
        layout.add_widget(self.label)
        layout.add_widget(self.textinput)  # <<< problema no input?
        layout.add_widget(button_temp)
        layout.add_widget(button_humidity )
        layout.add_widget(button_wind)
        layout.add_widget(button_humidity)
        return layout

    def update_label_temp(self, instance):
        cidade = self.textinput.text
        weather = self.pegar_clima(cidade)
        self.label.text = weather

    def update_label_vento(self, instance):
        cidade = self.textinput.text
        velocidadevento = self.velocidade_vento(cidade)
        self.label.text = velocidadevento

    def update_label_umidade(self, instance):
        cidade = self.textinput.text
        umidadelocal = self.umidade(cidade)
        self.label.text = umidadelocal

if __name__ == '__main__':
    WeatherApp().run()
        