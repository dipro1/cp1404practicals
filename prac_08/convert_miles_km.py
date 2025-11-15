from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window



class ConvertMilesKmApp(App):

    def build(self):
        Window.size = (200, 100)
        self.title = "Convert miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root




ConvertMilesKmApp().run()
