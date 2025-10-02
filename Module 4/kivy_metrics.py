# description sur deepseek et groktwitter

# 1. Comprendre les Problématiques
# 2. unités Clés et leurs Cas d'usage

#3. fonctions et propriétés avancés
from kivy.metrics import dp, sp, Metrics

# Conversion de Base
dp_value = dp(10)   # 10 dp en pixels
sp_value = sp(15)   # 15 sp en pixels

# Propriétés système critiques
density = Metrics.density       # Facteur d'echelles  (ex: 2.0 pour HD)
dpi = Metrics.dpi               # points par pouces
fontscale = Metrics.fontscale   # Echelle de police utilisateur

# 4. Technique Avancées
# a. Création d'unités personnalisées

from kivy.metrics import sp

# exemple : unité em relative à l'unité actuelle
def em(value, base_font_size=15):
    return value * sp(base_font_size)

# Utilisation
title_size = em(2.5)    # 2.5x la taille de base

# b. Gestion Dynamique des changements d'Ecran
from kivy.core.window import Window
from kivy.app import App, runTouchApp

class MyApp(App):
    def build(self):
        def on_resize(window, width, height):
            new_width_up = width / Metrics.density
            print(f"Nouvelle largeur  en dp: {new_width_up}")
            #print(dp(new_width_up))
            #print(window.width)
        Window.bind(on_resize=on_resize)
#MyApp().run()

# c. Calculs de Ratios Multi-Ecrans
# Ratio largeur/hauteur en dp
def screen_ratio():
    return (Window.width / Metrics.density) / (Window.height / Metrics.density)

# 5. Bonnes pratiques d'Optimisation :
# ° cache d'optimisation
[dp(x) for x in range(1000)] # Lent

# Solution: pré-calculer
cache_up = [dp(x) for x in range(1000)]

# ° Combinaison avec kiv.properties:
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from time import sleep
from kivy.graphics import Rectangle, Color

class ResponsiveWidget(Widget):
    padding_dp = NumericProperty(10)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        # changer la position et déclencher les événements
        sleep(2)
        self.pos=(self.pos[0]+1, self.pos[1]+1)

    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            # Conversion dynamique mais optimisée
            Rectangle(pos=self.pos, size=(dp(self.padding_dp), dp(20)))

#runTouchApp(ResponsiveWidget())

# pièges courants et Corrections
# Problème : Discontinuités lors des rotations d'ecran
# Solution :
from kivy.config import Config
Config.set('graphics', 'resizable', '1') # permet le recalcul automatique
# polices trop petites sur tablettes
# Solution :
# Adapter dynamiquement avec sp et une taille minimale
font_size = max(sp(20), 15) # jamais en dessous de 15px

# 7. Cas Réel : Création d'un Layout Responsive
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp

class AdaptiveGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = self.calculate_cols()

    def calculate_cols(self):
        width_dp = Window.width / Metrics.density
        return  4 if width_dp > 800 else (2 if width_dp > 480 else 1)

    # Recalcul lors du dimentionnement
    Window.bind(width=lambda *args: self.setter('cols')(self, self.calculate_cols()))

#runTouchApp(AdaptiveGrid())

# benchmarking avancé
import timeit

# Test de performance des conversion
print(timeit.timeit("dp(10)", setup="from kivy.metrics import dp", number=10000))
# Resultat typique : -0.0016 pour 10k d'appels (Optimiser si > 0.1s)

# 9. Intégration avec d'Autres Modules kivy avec kivy.graphics:
from kivy.graphics import Line
from kivy.uix.button import Button
from kivy.animation import Animation as an

class MyWidget(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_touch_down=self.update_width)

        with self.canvas:
            # Ligne de 1dp d'épaisseur
            self.line = Line(points=[100, 100, 400, 450], width=dp(1))

    def update_width(self, widget, touch):
        # avec aniomation
        anim = an(width=dp(300), duration=1)
        anim.start(self.line)

runTouchApp(MyWidget())