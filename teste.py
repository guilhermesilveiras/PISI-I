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
        if response.status_code == 200:
            data = response.json()
            return data['current']
        else:
            return 'Erro ao buscar o clima'
    
    def build(self):
        layout = BoxLayout (orientation = 'vertical')
        self.label = Label(text= 'Olá, seja bem vindo ao aplicativo "Como está o clima?", para começar, digite a cidade e pressione em "Como está o clima".')
        self.textinput = TextInput(text = 'Digite a cidade aqui: ')
        button = Button(text='Como está o clima?')
        button.bind(on_press=self.update_label)
        layout.add_widget(self.label)
        layout.add_widget(self.textinput)
        layout.add_widget(button)
        return layout
    
    def update_label(self, instance):
        cidade = self.textinput.text
        weather = self.pegar_clima(cidade)
        
        # Verifique se a busca do clima retornou um erro
        if isinstance(weather, str):
            self.label.text = weather
        else:
            # Se não houver erro, exiba os dados desejados do clima
            self.label.text = f'Temperatura: {weather["temperature"]}°C, Condição: {weather["weather_descriptions"][0]} e hora {weather["observation_time"]}'

if __name__ == '__main__':
    WeatherApp().run()