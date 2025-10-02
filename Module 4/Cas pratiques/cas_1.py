"""
Projet : Application de visualisation de données intéractives avec effets visuels

Objectif:
    Créer une applicatin kivy qui affiche un graphique en barres intéractif basé sur des données, avec des animations fl
    uides, une interface responsive et des fonctionnalités avancées comme les drap-an-drop et des tooltips.
"""
# Fonctionnalités pricipales
# voir dans l'application grok

# Code de l'application

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Ellipse, PushMatrix, PopMatrix, Rotate
from kivy.metrics import dp, sp
from kivy.effects.kinetic import KineticEffect
from kivy.effects.opacityscroll import OpacityScrollEffect
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.animation import Animation
from random import random

class BarGraph(Widget):
    # Propriétés pour les données et les dimension
    data = ListProperty([10, 20, 30, 40, 50])   # Données du graphique
    bar_width = NumericProperty(dp(50))         # Largeur des barres en dp
    max_height = NumericProperty(dp(200))        # Hauteur maximale des barres
    selected_bar = ObjectProperty(None, allownone=True) # Barre sélectionnée pour drag-and-drop
    # nouvelle propriété pour le tooltip
    tooltip = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.effect = KineticEffect()  # effet cinétique pour des animations fluides
        # Relier les changements des position, taille et données à la mise à jour du graphique
        self.bind(pos=self.update_graph, size=self.update_graph, data=self.update_graph)
        # Initialiser le tooltip (invisible au départ)
        self.tooltip = Label(
            size=(dp(200), dp(200)),    # Taille responsive
            font_size=sp(16),           # Police responsive
            color=(1, 1, 1, 0)          # invisible (opacité 0)
            #canvas_before=[PushMatrix(), Rotate(angle=0)], # pour transformation graphiques
            #canvas_after=[PopMatrix()]
        )
        # ajouter un fond au tooltip avec kivy.graphics
        with self.tooltip.canvas:
            Color(1, 1, 0, 0.8) # Fond sombre
            self.tooltip_bg = Rectangle(pos=self.tooltip.pos, size=self.tooltip.size)
        self.add_widget(self.tooltip)   # Ajouter le tooltip Au widget
        # Mettre à jour le fond quand la position /taille du tooltip change
        self.tooltip.bind(pos=self.update_tooltip_bg, size=self.update_tooltip_bg)

    def update_graph(self, *args):
        """Met à jour le canvas pour déssiner les barres."""
        self.canvas.clear()
        with self.canvas:
            for i, value in enumerate(self.data):
                # Calculer la hauteur proportionnelle
                height = (value/max(self.data)) * self.max_height
                x = self.x + i * (self.bar_width + dp(10)) # espacement entre les barres
                y = self.y
                # Déssiner la barre avec une couleur aléatoire
                Color(random(), random(), random(), 1)
                Rectangle(pos=(x, y), size=(self.bar_width, height))

    def update_tooltip_bg(self, *args):
        # Mettre à jour la position et la la taille du fond du tooltip
        self.tooltip_bg.pos = self.tooltip.pos
        self.tooltip_bg.size = self.tooltip.size

    def on_touch_down(self, touch):
        """Détecter quelle barre est touchée pour le drap-and-drop."""
        for i in range(len(self.data)):
            x = self.x + i * (self.bar_width + dp(10))
            height = (self.data[i] / max(self.data)) * self.max_height
            if (x <= touch.x <= x + self.bar_width) and (self.y <= touch.y <= self.y + (self.data[i] / max(self.data)) * self.max_height):
                self.selected_bar = i
                touch.grab(self)    # Capturer l'événement tactile
                self.show_tooltip(i, touch.pos) # Affiche le tooltip
                return True
        self.hide_tooltip() # Cacher si clic hors barre
        return super().on_touch_down(touch)

    def show_tooltip(self, bar_index, pos):
        """Affiche le tooltip avec animation."""
        self.tooltip.text = f"valeur: {self.data[bar_index]:.1f}"
        # positionner le tooltip  près du clic, au-dessus de la barre
        self.tooltip.pos = (pos[0] + dp(10), pos[1] + dp(10))
        # Appliquer un effet d'opacité
        Animation(color=(1, 1, 1, 1), duration=0.3).start(self.tooltip)
        print(f"Tooltip text: { self.tooltip.text}, pos: {self.tooltip.pos}, size: {self.tooltip.size}")

    def hide_tooltip(self):
        """Cacher le tooltip avec animation."""
        Animation(color=(1, 1, 1, 1), duration=0.3).start(self.tooltip)

    def on_touch_move(self, touch):
        """Déplacée la barre sélectionnée."""
        if touch.grab_current == self and self.selected_bar is not None:
            # Calculer la nouvelle position en fonction du déplacement
            new_index = int((touch.x - self.x) / (self.bar_width + dp(10)))
            new_index = max(0, min(new_index, len(self.data) - 1))
            if new_index != self.selected_bar:
                # Echanger les données
                self.data[self.selected_bar], self.data[new_index] = (
                    self.data[new_index], self.data[self.selected_bar]
                )
                self.selected_bar = new_index
                self.update_graph() # Redéssiner immédiatement
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        """relâcher la barre selectionnée."""
        if touch.grab_current == self:
            touch.ungrab(self)
            self.selected_bar = None
        return super().on_touch_up(touch)

class GraphApp(App):
    def build(self):
        """Construire l'interface principale."""
        root = BoxLayout(orientation='vertical')
        self.graph = BarGraph()

        # Bouton pour modifier les données
        bouton = Button(text="Modifier données", size_hint=(1, 0.1), font_size=sp(20))
        bouton.bind(on_press=self.modify_data)

        #  Ajouter les widgets au layout
        root.add_widget(self.graph)
        root.add_widget(bouton)
        return root

    def modify_data(self, instance):
        """Modifier les données avec une animation."""
        new_data = [random() * 100 for _ in range(5)]
        anim = Animation(data=new_data, duration=1)
        anim.start(self.graph)

if __name__ == '__main__':
    GraphApp().run()