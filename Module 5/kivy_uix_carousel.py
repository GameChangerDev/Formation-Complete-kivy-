# voire grok apk et deepseek pour les description
from kivy.animation import Animation
# Mise en Pratique : Les Bases
from kivy.app import App, runTouchApp
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label

class SimpleCarouselApp(App):
    def build(self):
        carousel = Carousel(direction="right", loop=True)
        for i in range(3):
            label = Label(text=f'Slide {i+1}', font_size=50)
            carousel.add_widget(label)
        return carousel
#if __name__ == '__main__':
#    SimpleCarouselApp().run()

# 1. Chargement dynamique des contenus
import os
from kivy.uix.image import Image

class DynamicCarousel(App):
    def build(self):
        carousel = Carousel(direction='right', loop=True)
        image_folder = r'C:\Users\DELL\Pictures\photos à traiter'
        for filname in os.listdir(image_folder):
            if filname.endswith(('img','.jpg', '.png')):
                image = Image(source=os.path.join(image_folder, filname))
                carousel.add_widget(image)
        return carousel
#if __name__ == '__main__':
#    DynamicCarousel().run()

# 2. Ajouter des contrôles personnalisés
# Ajouter des boutons pour naviguer manuellement dans le carrousel.
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import RoundedRectangle, Color

class ControlledCarouselApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        # 3. Effet de Transition
        carousel = Carousel(direction='right', loop=True, anim_type='in_out_bounce')

        # Ajouter des slides
        for i in range(3):
            carousel.add_widget(Label(text=f'Slide {i+1}', font_size=50))

        # Ajouter des contrôles
        btn_prev = Button(text='précédent', color=(0, 0, 0, 1))
        btn_next = Button(text='Suivant')
        btn_prev.bind(on_press=lambda instance: carousel.load_previous())
        btn_next.bind(on_press=lambda instance: carousel.load_next())

        # Ajouter au layout
        controls = BoxLayout(size_hint=(1, 0.1))
        controls.add_widget(btn_next)
        controls.add_widget(btn_prev)
        main_layout.add_widget(carousel)
        main_layout.add_widget(controls)

        # 4. interaction utilisateur
        carousel.bind(current_slide=lambda instance, value: print(f"Slide Actuel {value.text}"))

        return main_layout

#if __name__ == '__main__':
#    ControlledCarouselApp().run()

# 5. Transitions Personnalisées
# Exemple Effets de zoom
"""
class ZoomCarousel(Carousel):
    def on_touch_up(self, touch):
        if self._touch != touch: return
        if abs(touch.ox - touch.x) > self.scroll_distance:
            # Animation personalisée
            self.animation_transition(
                self.load_next(),
                offset=self._offset,
                anim_duration=0.7
            )
        super().on_touch_up(touch)

runTouchApp(ZoomCarousel())
"""

# 6. Performance avec Grand datasets
# 7. integration avec d'autres widgets
# Carousel + TabbedPanel

from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.image import AsyncImage, Image
class TabbedCarousel(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(3):
            tab = TabbedPanelItem(text=f"Tab {i+1}")
            carousel = Carousel()
            carousel.add_widget(AsyncImage(source=Image[i]))
            tab.content = carousel
            self.add_widget(tab)


# 8. Bonnes pratiques
# 9. débogage Avancé

#   Cas Pratique Pratique Complet : Galerie d'Images intéractive
# Objectif : créer une galerie d'images avec un carrousel, des contôles personnalisés, et un indicateur de slide

from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import os

class GalerieApp(App):
    def build(self):
        # layout principal
        main_layout = BoxLayout(orientation='vertical')

        # Créer le carrousel
        self.carousel = Carousel(direction='right', loop=True, anim_type='in_out_cubic')

        # Charger les images dynamiquement
        image_folder = r'C:\Users\DELL\Pictures\photos à traiter'
        if not os.path.exists(image_folder):
            os.makedirs(image_folder, exist_ok=True)
        # Simuler les images si le dossier est vide
        images_files = os.listdir(image_folder) if os.listdir(image_folder) else [f"url/image{i+1}" for i in range(10)]

        for img_path in images_files:
            if isinstance(img_path, str) and img_path.startswith("https:"):
                image = Image(source=img_path)
            else:
                image = Image(source=os.path.join(image_folder, img_path))
            self.carousel.add_widget(image)

        # Indicateur de slide
        self.slide_indicator = Label(text=f"Slide 1/{len(self.carousel.slides)}", size_hint=(1, 0.1))
        self.carousel.bind(index=self.update_indicator)

        # Bouton de contrôle
        btn_prev = Button(text='Précédent', size_hint=(1, 0.1))
        btn_next = Button(text='Suivant', size_hint=(1, 0.1))
        btn_prev.bind(on_press=lambda x: self.carousel.load_previous())
        btn_next.bind(on_press=lambda x: self.carousel.load_next())

        # Layout des contrôles
        controls = BoxLayout(size_hint=(1, 0.1), spacing=20)
        controls.add_widget(btn_prev)
        controls.add_widget(btn_next)

        # Assembler tout
        main_layout.add_widget(self.carousel)
        main_layout.add_widget(controls)
        main_layout.add_widget(self.slide_indicator)

        return main_layout

    def update_indicator(self, instance, value):
        self.slide_indicator.text = f"Slide {value + 1}/{len(self.carousel.slides)}"

if __name__ == '__main__':
    GalerieApp().run()