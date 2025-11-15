from kivy.app import App
from kivy.lang import Builder

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

    def miles(self):
        return float(self.root.ids.miles_input.text)


    def results(self):
        miles = self.miles()
        km = miles * MILES_TO_KM
        self.output_km = f"{km: }"

    def handel_change(self, change):
        new_miles = self.miles() + change
        self.root.ids.miles_input.text = str(new_miles)

ConvertMilesKmApp().run()
