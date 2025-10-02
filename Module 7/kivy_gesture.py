# voir les descriptions dans grok apk ou Deepseek ou le code source

# 1. Gesture
from kivy.gesture import Gesture, GesturePoint

# Création d'un geste simple (triangle approximatif)
g1 = Gesture(tolerance=0.1) # Tolerance laxiste pour tests
g1.add_stroke([(100, 100), (200, 300), (300, 100), (100, 100)])
g1.normalize(stroke_samples=64) # Haute définition pour précision

# Geste similaire mais rotated/scaled
g2 = Gesture()
g2.add_stroke([(150, 150), (250, 350), (350, 150), (150, 150)])
g2.normalize(stroke_samples=64)

score = g1.get_score(g2, rotation_invariant=True)
print(f"Score de Similarité: {score}")  # Typiquement > 0.9 si similaires

# 2. GestureStroke  : represente un trait individuel dans un geste. Gère les points bruts et leur transformation.
from kivy.gesture import GestureStroke

stroke = GestureStroke()
for i in range(10):
    stroke.add_point(i * 10, i * 10)    # Ligne diagonale
stroke.normalize_stroke(sample_points=16)
print(stroke.stroke_length()) # Longueur normalisée

# 3. GestureDatabase

from kivy.gesture import Gesture, GestureDatabase

gdb = GestureDatabase()

# Ajout d'un geste
g = Gesture()
g.add_stroke([(0, 0), (100, 100)])
g.normalize()
gdb.add_gesture(g)

# Sérialisation
gest_str = gdb.gesture_to_str(g)    # chaîne de caractères en bytes
with open('gesture.txt', 'w') as f:
    f.write(gest_str.hex()) # convertir le bytes en hexadécimal avant de l'enrgeristrer

# Chargement et recherche
with open('gesture.txt', 'r') as f:
    loaded_g = gdb.str_to_gesture(bytes.fromhex(f.read())) # retransformer la chaîne hexadécimale en bytes

new_g = Gesture() # Supposez un nouveau geste similaire
new_g.add_stroke([(0, 0), (90, 90)])
new_g.normalize()

matches = gdb.find(new_g, minscore=0.8)
if matches:
    print(f"Meilleur Match: score {matches[0]}")
    print(loaded_g, g, g.get_score(loaded_g))

# 4. GestureSurface
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gesturesurface import GestureSurface
from kivy.gesture import GestureDatabase

gdb = GestureDatabase()

class MySurface(GestureSurface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text="bonjour"))

    def on_gesture_complete(self, gesture):
        # gesture est un Gesture prêt à être comparé
        print("Geste capturé")
        print(gesture)
        gdb.add_gesture(gesture)
        print(gdb.db)

# Dans votre app
class MyApp(App):
    def build(self):
        return MySurface()

#MyApp().run()

# Projet Pratique : Application de Reconnaissance de geste pour contrôle d'un Canvas de Dessin

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.gesture import Gesture, GestureDatabase
from kivy.uix.gesturesurface import GestureSurface
from kivy.graphics import Color, Line
import os

class DrawingCanvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lines = []
        self.color = (1, 0, 0)  # Rouge par défaut

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.color)
            touch.ud['line'] = Line(points=(touch.x, touch.y))
        return True

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        return True

    def on_touch_up(self, touch):
        self.lines.append(touch.ud['line'])

    def undo(self):
        if self.lines:
            self.canvas.remove(self.lignes.pop())

    def clear(self):
        self.canvas.clear()
        self.lines = []

    def change_color(self):
        self.color = (0, 1, 0) if self.color == (1, 0, 0) else (1, 0, 0)

class GestureDrawer(GestureSurface):
    def __init__(self, db, canvas, **kwargs):
        super().__init__(**kwargs)
        self.gdb = db
        self.canvas_widget = canvas

    from kivy.gesture import GesturePoint
    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        if self.canvas_widget.on_touch_down(touch):
            touch.ud["points"] = [(touch.x, touch.y)]

    def on_touch_move(self, touch):
        super().on_touch_move(touch)
        if self.canvas_widget.on_touch_move(touch):
            touch.ud["points"].append((touch.x, touch.y))

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        if self._gestures:   # Gestes capturés
            geste1 = self._gestures[0]   # Prenez le premier (uni-touch)
            self.init_stroke(geste1, touch)

            points = GesturePoint(geste1._strokes[geste1.id].points[0], geste1._strokes[geste1.id].points[1])

            g = Gesture()
            g.add_stroke([(points.x, points.y)])
            g.normalize(stroke_samples=64)

            matches = self.gdb.find(g, minscore=0.85, rotation_invariant=True)
            print(matches)
            if matches:
                score, matched_g = matches
                # Associez à des actions (ex: base sur un ID ou non)
                if matched_g ==  self.gdb.gestures[0]:   # Supposez cercle = undo
                    print(1)
                    self.canvas_widget.undo()
                elif matched_g == self.gdb.gestures[1]: # Ligne = clear
                    self.canvas_widget.clear()
                    print(2)
                elif matched_g == self.gdb.gestures[2]: # Triangle = color
                    self.canvas_widget.change_color()
                    print(3)
            print(touch.ud["points"])

class GestureApp(App):
    def build(self):
        gdb = GestureDatabase()
        # Enregistrez des gestes (en production, chargez de fichier)
        # Ex: Cercle
        circle = Gesture()
        circle.add_stroke([(100, 100), (100, 200), (200, 100), (100, 100)])
        circle.normalize()
        gdb.add_gesture(circle)

        # Ligne Horizontale
        line = Gesture()
        line.add_stroke([(50, 100), (250, 100)])
        line.normalize()
        gdb.add_gesture(line)

        # Triangle
        triangle = Gesture()
        triangle.add_stroke([(100, 100), (200, 200), (300, 100), (100, 100)])
        triangle.normalize()
        gdb.add_gesture(triangle)

        # Sauvegarde exemple
        with open('gestures.db', 'w') as f:
            for g in gdb.db:
                f.write(gdb.gesture_to_str(g).hex() + "\n")

        canvas = DrawingCanvas()
        surface = GestureDrawer(gdb, canvas)
        surface.add_widget(canvas)  # Imbriqué pour capture
        return surface

if __name__ == '__main__':
    GestureApp().run()