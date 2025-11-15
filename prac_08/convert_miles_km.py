from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):

    output_km = StringProperty("0")

    def handle_convert(self):
        self.results()

    def build(self):
        self.title = "Convert miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def results(self):
        miles = float(self.root.ids.miles_input.text)
        km = miles * MILES_TO_KM
        self.output_km = f"{km: }"

ConvertMilesKmApp().run()
