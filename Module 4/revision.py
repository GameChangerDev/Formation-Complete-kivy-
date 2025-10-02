# exercice:
# Objectif : creer un espace de dessus ou on peut changer de couleur de dessin
from kivy.app import App, runTouchApp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Line, Color
from kivy.properties import NumericProperty, ColorProperty, ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder

modif_ep = Builder.load_file("ep.kv")

class CustomWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Color_line = ObjectProperty()
        self.line = ObjectProperty()
        self.couleur = None
        self.hauteur = Window.height-100
        self.width = 0


    def on_touch_down(self, touch):
        with self.canvas:
            if not self.couleur:
                self.couleur = (0, 0, 1)
            if self.width == 0:
                self.width = 2
            self.Color_line = Color()
            self.Color_line.r, self.Color_line.g, self.Color_line.b = self.couleur
            self.line = Line(points=[touch.x, touch.y], width=self.width)

    def on_touch_move(self, touch):
        self.line.points += [touch.x, touch.y]


class BoxWidget(BoxLayout):
    btn1 = ObjectProperty()
    btn0 = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 20
        self.padding = 40

        self.espace_dessin = CustomWidget(size_hint=(None, None), height=Window.height-100)
        barre_coleurs = BoxLayout(size_hint_y=None,height=100)
        self.add_widget(self.espace_dessin)

        self.bleue = Button(text="Bleue", color=(0, 0, 1))
        self.bleue.bind(on_press=self.react_bleue)
        self.vert = Button(text="vert", color=(0, 1, 0))
        self.vert.bind(on_press=self.react_vert)
        self.rouge = Button(text="rouge", color=(1, 0, 0))
        self.rouge.bind(on_press=self.react_rouge)
        self.efface = Button(text="efface", color=(0, 0, 0))
        self.efface.bind(on_press=self.react_efface)
        barre_coleurs.add_widget(self.bleue)
        barre_coleurs.add_widget(self.vert)
        barre_coleurs.add_widget(self.rouge)
        barre_coleurs.add_widget(self.efface)
        self.add_widget(barre_coleurs)

        self.btn0 = modif_ep.ids['btn_moins']
        self.btn0.bind(on_press=self.react_btn0)
        self.btn1 = modif_ep.ids['btn_plus']
        self.btn1.bind(on_press=self.react_btn1)
        Window.add_widget(modif_ep)


    def react_bleue(self, instance):
        self.espace_dessin.couleur = (0, 0, 1)
        print(instance.text)
    def react_vert(self, instance):
        self.espace_dessin.couleur = (0, 1, 0)
        print(instance.text)
    def react_rouge(self, instance):
        self.espace_dessin.couleur = (1, 0, 0)
        print(instance.text)
    def react_efface(self, instance):
        self.espace_dessin.couleur = (0, 0, 0)
        print(instance.text)

    def react_btn0(self, btn):
        self.espace_dessin.width -= 2
    def react_btn1(self, btn):
        self.espace_dessin.width += 2



class BoxApp(App):
    def build(self):
        return  BoxWidget()

if __name__ == '__main__':
    BoxApp().run()


