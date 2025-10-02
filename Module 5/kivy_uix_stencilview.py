# kivy.uix.stencilview
# voir grok apk et de  deepseek
# 1, 2, 3

# Exemple utilisation basique de StencilView
# Découper image plus grande dans une zone plus petite avec StencilView

from kivy.app import App
from kivy.uix.stencilview import StencilView
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video

class StencilExemple(App):
    def build(self):
        layout = FloatLayout()
        stencil = StencilView(size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
       # video = Video(source=r'C:\Users\DELL\Videos\entraînements\VID_20250527_190212.mp4', play=True)
        image = Image(source=r'C:\Users\DELL\Pictures\Photos a traiter\IMG_20241222_103307_418.jpg', size_hint=(2, 2), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        stencil.add_widget(image)
        layout.add_widget(stencil)
        return layout

#StencilExemple().run()

# Exemple 2: StencilView imbriqués
from kivy.uix.label import Label

class NestedStencilExample(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        outer_stencil = StencilView(size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        inner_stencil = StencilView(size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        label = Label(text='Ce text est découpé par des stencils imbriqués', font_size=24, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        inner_stencil.add_widget(label)
        outer_stencil.add_widget(inner_stencil)
        layout.add_widget(outer_stencil)
        return layout

#NestedStencilExample().run()

# Exemple 3: StencilView avec Scatter
from kivy.uix.scatter import Scatter

class StencilScatterExample(App):
    def build(self):
        layout = FloatLayout()
        stencil = StencilView(size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        scatter = Scatter(do_rotation=False, do_scale=False)
        image = Image(source=r'C:\Users\DELL\Pictures\Photos a traiter\IMG_20241222_103307_418.jpg', size_hint=(None, None), size=(400, 400))
        scatter.add_widget(image)
        stencil.add_widget(scatter)
        layout.add_widget(stencil)
        return layout

#StencilScatterExample().run()

# 4. Exemple Fondamental : Masque Carré
from kivy.app import App
from kivy.uix.stencilview import StencilView
from kivy.uix.button import Button

class MonStencil(StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            StencilPush()
            Rectangle(pos=self.pos, size=self.size)
            StencilUse()

        self.add_widget(Button(text="Bouton visible", size=(200, 200)))

        with self.canvas.after:
            StencilUnUse()
            StencilPop()

class TestApp(App):
    def build(self):
        return MonStencil(size=(300, 300))

#TestApp().run()

# 5. Cas Avancé : Masque Dynamique Circulaire

from kivy.app import App
from kivy.uix.stencilview import StencilView
from kivy.uix.image import AsyncImage
from kivy.graphics import Ellipse, StencilPush, StencilPop, StencilUse, StencilUnUse
from kivy.animation import Animation

class CircularStencil(StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update_canvas, size=self.update_canvas)
        self.add_widget(AsyncImage(source=r'C:\Users\DELL\Pictures\Photos a traiter\IMG_20241222_103307_418.jpg'))
        self.anim = Animation(radius=150, duration=2) + Animation(radius=250, duration=2)
        self.anim.repeat = True
        self.anim.start(self)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            StencilPush()
            Ellipse(pos=self.pos, size=(self.radius, self.radius))
            StencilUse()

        self.canvas.after.clear()
        with self.canvas.after:
            StencilUnUse()
            StencilPop()

    radius = 50    # propriété dynamique

class CircleApp(App):
    def build(self):
        return CircularStencil(size=(500, 500))

#CircleApp().run()

# Projet Final : Lecteur d'images avec Effets de Masques avancés
from kivy.app import App
from kivy.uix.stencilview import StencilView
from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Ellipse, Rectangle, Color, StencilPush, StencilPop, StencilUse, StencilUnUse
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.properties import NumericProperty, ListProperty
from os import path, listdir

class Thumbnail(ButtonBehavior, StencilView):
    selected = NumericProperty(0) # 0 = non selectionné.
    def __init__(self, source, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (100, 100)
        self.source = source
        with self.canvas.before:
            StencilPush()
            Ellipse(size=self.size)
            StencilUse()

        self.img = AsyncImage(
            source=r'C:\Users\DELL\Pictures\Photos a traiter\IMG_20241222_103307_418.jpg' if not self.source else self.source,
            size=self.size
        )

        self.add_widget(self.img)

        with self.canvas.before:
            StencilUnUse()
            StencilPop()

        self.bind(on_press=self.animate_selection)

    def animate_selection(self, *args):
        anim = Animation(size=(120, 120)) if self.selected == 0 else Animation(size=(100, 100))
        anim.start(self)
        self.selected = 1 - self.selected

class ImageViewer(StencilView):
    current_img = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        folder = r"C:\Users\DELL\Pictures\images de formation"
        self.images = [path.join(folder, image) for image in listdir(folder)]
        self.main_img = AsyncImage(source=self.images[0], allow_stretch=True)
        self.add_widget(self.main_img)
        self.bind(size=self.update_main_img)

    def update_main_img(self, *args):
        self.main_img.size = self.size

    def change_image(self, index):
        self.current_img = index
        self.main_img.source = self.images[index]
        anim = Animation(opacity=0, duration=0.3) + Animation(opacity=1, duration=0.3)
        anim.start(self.main_img)


class GalleryApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Zone d'affichage principale
        self.viewer = ImageViewer(size_hint=(1, 0.8))
        layout.add_widget(self.viewer)

        # Barre de miniatures
        thumb_box = BoxLayout(size_hint=(1, 0.2), padding=10)
        for i, img in enumerate(self.viewer.images):
            thumb = Thumbnail(source=img)
            thumb.bind(on_press=lambda _, idx=i: self.viewer.change_image(idx))
            thumb_box.add_widget(thumb)

        layout.add_widget(thumb_box)
        return layout

GalleryApp().run()