# voir les descriptions dans grok apk ou Deepseek ou le code source

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.graphics.transformation import Matrix

# 1. 2. 3. 4. 5.

class MyApp(App):
    def build(self):
        scatter = Scatter(size=(200, 200), size_hint=(None, None))
        label = Label(text="Manipulez-moi", size=(200, 200), size_hint=(None, None))

        # utilisation d'une transformation
        mat = Matrix().scale(2, 2, 2) # Scaling 3D, mais 2D suffit
        scatter.apply_transform(mat, anchor=(100, 100)) # Ancrage au centre d'un widget 200x200
        print(scatter.do_translation)

        scatter.add_widget(label)
        return scatter

# 6. Cas Pratique : Editeur de collage intératif
# editeur_collage