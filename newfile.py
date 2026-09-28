main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from datetime import datetime

class ZoyaApp(App):
    def build(self):
        self.memory = {}

        layout = BoxLayout(orientation='vertical')

        self.input = TextInput(hint_text="Type here")
        self.output = Label(text="Zoya AI Ready")

        btn = Button(text="Send")
        btn.bind(on_press=self.reply)

        layout.add_widget(self.input)
        layout.add_widget(btn)
        layout.add_widget(self.output)

        return layout

    def reply(self, instance):
        text = self.input.text.lower()

        if "hello" in text or "hi" in text:
            ans = "Hello! Main Zoya hoon."
        elif "time" in text:
            ans = datetime.now().strftime("%H:%M:%S")
        else:
            ans = "Mujhe samajh nahi aaya."

        self.output.text = ans

ZoyaApp().run()