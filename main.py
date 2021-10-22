# import libraries
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

# import main.kv using builder method
Builder.load_file("main.kv")

# create root class
class MyLayout(Widget):
    def change_value(self, value):
        if value == 100:
            value = 0
        else:
            value += 10
        self.ids.progress_bar.value = value

# create main class
class Main(App):
    def build(self):
        return MyLayout()

# an instance of main class
if __name__ == "__main__":
    Main().run()