from kivymd.app import MDApp
from kivy.lang import Builder

image = """
Image:
    source: "icons/location.png"

"""

class TutorialApp(MDApp):
    def build(self):
        images = Builder.load_string(image)
        return images
    

if __name__ == "__main__":
    TutorialApp().run()