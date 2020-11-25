from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        button_name = open('button.txt').read()
        screen.add_widget(
            MDRectangleFlatButton(
                text=button_name,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen


MainApp().run()
