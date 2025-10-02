"""
    Prochaînes étapes : Projet avancé (mini-jeu de particules)
        ° Concept : des particules (cercle) tombent du haut de l'écran. un clic déclenche une explosion qui repousse
            les particules avec un effet cinétique.
"""
# voir certaines descriptions dans grok apk

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.metrics import dp, sp
from kivy.effects.kinetic import KineticEffect
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.animation import Animation
from random import random
import math



class Particle:
    """Classe pour représenter une particule."""
    def __init__(self, x, y, size, vx, vy):
        self.x = x
        self.y = y
        self.size = size,
        self.vx = vx    # Vélovité horizontal
        self.vy = vy    # Vélocité verticale

class ParticleSystem(Widget):
    particles = ListProperty([]) # Liste des particules
    explosion_strength = NumericProperty(dp(150))   # Portée de l'explosion
    score = NumericProperty(0)  # Score du joueur
    score_label = ObjectProperty(None)   # Label pour Afficher le score

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.effect = KineticEffect()   # Effet cinétique pour les animations
        # Initialiser le label du score
        self.score_label = Label(
            text=f"score: {self.score}",
            font_size=sp(20), # Taille de police responsive
            size=(dp(150), dp(40)),
            size_hint=(None, None),
            pos=(dp(10), self.height - dp(50)), # Coin supérieur gauche
            color=(1, 1, 1, 1)
        )
        with self.score_label.canvas.before:
            Color(0, 0, 0, 0.8) # Fond sombre pour le score
            self.score_label_bg = Rectangle(pos=self.score_label.pos, size=self.score_label.size)
        self .add_widget(self.score_label)
        self.score_label.bind(pos=self.update_score_bg, size=self.update_score_bg)
        # Lancer la mise à jour des particules
        Clock.schedule_interval(self.update, 0.033) # -30 FPS

    def update_score_bg(self, *args):
        """Mettre à jour le fond du score."""
        self.score_label_bg.pos = self.score_label.pos
        self.score_label_bg.size = self.score_label_bg.size

    def update(self, dt):
        """Mettre à jour les particules."""
        # Ajouter une nouvelle particule
        self.particles.append(Particle(
            x=self.width * random(),
            y=self.height,
            size=dp(10 + random() * 10), # Taille entre 10 et 20dp
            vx=random() * 4 - 2, # Vélocité horizontale aléatoire
            vy=random() * 5 -2 # Vélocité verticale (vers le bas)
        ))
        # Mettre à jour les positions
        for p in self.particles:
            p.x += p.vx * dt * 60 # Ajouter pour fluidité
            p.y += p.vy * dt * 60
            # Rebond sur les bords
            if p.x < p.size / 2 or p.x > self.width - p.size / 2:
                p.vx *= -1
            # Supprimer les particules hors écran (haut)
            if p.y < -p.size:
                self.particles.remove(p)
        self.update_canvas()

    def update_canvas(self):
        """Redessiner les particules."""
        self.canvas.clear()
        with self.canvas:
            for p in self.particles:
                Color(random(), random(), random(), 1) # Couleur aléatoire
                Ellipse(
                    pos=(p.x - p.size / 2, p.y - p.size / 2),
                    size=(p.size, p.size)
                )

    def on_touch_down(self, touch):
        """Déclencher une explosion au clic."""
        particles_affected = 0
        for p in self.particles:
            dx, dy = p.x - touch.x, p.y - touch.y
            distance = math.sqrt(dx**2 + dy**2)
            if distance < self.explosion_strength:
                # Appliquer une force proportionnelle
                force = (1 - distance / self.explosion_strength) * dp(20)
                p.vx += (dx / distance) * force if distance != 0 else 0
                p.vy += (dy/ distance) * force if distance != 0 else 0
                particles_affected += 1
        # Mettre à jour le score
        self.score += particles_affected
        self.score_label.text = f"Score: {self.score}"
        # Animation d'explosion (effet visuel)
        self.effect.start(touch.pos)
        # Ajouter un cercle temporaire pour l'explosion
        with self.canvas:
            Color(1, 1, 0, 0.5) # Jaune semi-transparent
            explosion = Ellipse(
                pos=(touch.x - self.explosion_strength / 2, touch.y - self.explosion_strength / 2),
                size=(self.explosion_strength, self.explosion_strength)
            )
        # Animer la disparition du cercle
        Animation(opacity=0, duration=0.5).start(explosion)
        Clock.schedule_once(lambda  dt: self.canvas.remove(explosion), 0.5)

class ParticleApp(App):
    def build(self):
        return ParticleSystem()

if __name__ == '__main__':
    ParticleApp().run()