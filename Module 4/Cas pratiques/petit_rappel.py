from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import RoundedRectangle, Color
from kivy.clock import Clock
from kivy.core.window import Window
from random import random

cercle = Button(text="Cliquez ici", size=(Window.width, Window.height))


with cercle.canvas:
    color = Color(1, 1, 1, 1)
    rectangle = RoundedRectangle(pos=cercle.pos, size=cercle.size, radius=[(45, 45) for i in range(4)])

    def update_rect(dt):
        width, height = rectangle.size
        if width > 300 and height > 250:
            width -= 3
            height -= 3
            rectangle.size = (width, height)
        else:
            rectangle.size = cercle.size
    def update_color(dt):
        color.rgb = [random() * 100 for i in range(3)]
        print(color.rgba)

    Clock.schedule_interval(update_color, 0.5)
    Clock.schedule_interval(update_rect, 1)


class MyApp(App):
    def build(self):
        return cercle

if __name__ == "__main__":
    MyApp().run()