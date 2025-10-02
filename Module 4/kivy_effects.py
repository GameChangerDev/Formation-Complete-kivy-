# 1. introduction
# voir deepseek et grok pour les détails
#2. Effets intégrés en profondeur
# a. kinetic
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.effects.kinetic import KineticEffect
from kivy.properties import ObjectProperty

class CustomScroll(ScrollView):
    effect_y = KineticEffect(friction=0.02)

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(100):
            btn = Button(text=f"Bouton {i+1}", size_hint_y=None, height=100)
            layout.add_widget(btn)
        scroll = CustomScroll()
        scroll.add_widget(layout)
        return scroll

MyApp().run()

# Cas avancé : Ajustement dynamiquement


class MyApp(App):
    scroll=ObjectProperty()
    def build(self):
        layout = GridLayout(cols=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(100):
            btn = Button(text=f"Bouton {i + 1}", size_hint_y=None, height=100)
            if i == 50:# bouton spécial au milieu
                btn.bind(on_press=self.reduce_friction)
            layout.add_widget(btn)

        self.scroll = ScrollView()
        self.scroll.add_widget(layout)
        return self.scroll

    def reduce_friction(self, instance):
        self.scroll.effect_y.friction = 0.15 # Défilementtrès fluide temporairement
        print("Friction réduite !")
        print(self.scroll.effect_y)

MyApp().run()


#b. DampedScollEffect
# comportement physique réaliste:
from kivy.effects.dampedscroll import DampedScrollEffect
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import runTouchApp
from kivy.core.window import Window
"""
"""
class CustomScroll(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.effect_cls = DampedScrollEffect
        self.effect_y = CustomDampedEffect() # Personnalisation

class CustomDampedEffect(DampedScrollEffect):
    spring_constant = 0.2 # Raideur du ressort
    friction = 0.8        # Coefficient de friction

class CustomBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        #scroll = CustomScroll(bar_width=20, bar_color="red")
        scroll2 = CustomScroll(bar_width=2, bar_color="red")

        box = BoxLayout(orientation="vertical", size_hint_y=None, spacing=20, padding=[5, 5, 30, 5])
        box2 = BoxLayout(size_hint_x=None, spacing=20, padding=[5, 5, 30, 5])
        box.bind(minimum_height=box.setter('height'))
        box2.bind(minimum_width=box.setter('width'))

        for i in range(1000):
            btn = Button(text=f"Bouton {i+1}", size_hint_y=None, height=150)
            box.add_widget(btn)
        scroll.add_widget(box)
        for i in range(1000):
            btn = Button(text=f"Bouton {i+1}", size_hint_x=None, width=200)
            box2.add_widget(btn)
        scroll2.add_widget(box2)

        self.add_widget(scroll)
        self.add_widget(scroll2)

class App(ScrollView):
    def __init__(self, **kwargs):
        self.size_hint = (None, None)
        self.size = (Window.width, Window.height)
        super().__init__(**kwargs)
        self.add_widget(CustomBox())

#runTouchApp(App())

# c. OpacityScrollEffect
# Opacité variable pendant le défilement:
from kivy.effects.opacityscroll import OpacityScrollEffect

scroll = ScrollView(effect_cls=OpacityScrollEffect)

"""
<CustomWidget@Widget>:
    effect_opacity: 0.5 # Opacity minimale
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.effects.opacityscroll import OpacityScrollEffect
"""
"""
class MyApp(App):
    def build(self):
        layout = GridLayout(cols=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(100):
            btn = Button(text=f"Bouton {i}", size_hint_y=None, height=40)
            layout.add_widget(btn)
        scrollview = ScrollView()
        scrollview.effect_y = OpacityScrollEffect()
        scrollview.add_widget(layout)
        return scrollview
MyApp().run()

# exemple avancé Combinaison de DampedScollEffect et OpacityScrollEffect
from  kivy.effects.dampedscroll import DampedScrollEffect
from kivy.effects.opacityscroll import OpacityScrollEffect

class DampedOpacityScrollEffect(OpacityScrollEffect):
    pass# combine les comportement des deux classes



class MyApp(App):
    def build(self):
        layout = GridLayout(cols=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(100):
            btn = Button(text=f"Bouton {i}", size_hint_y=None, height=40)
            layout.add_widget(btn)
        scrollview = ScrollView()
        scrollview.effect_y = DampedOpacityScrollEffect(
            friction=0.02,           # Défilement fluide
            velocity=0.2,        # vitesse du scroll
        )
        scrollview.add_widget(layout)
        return scrollview

MyApp().run()
print('dernier')
