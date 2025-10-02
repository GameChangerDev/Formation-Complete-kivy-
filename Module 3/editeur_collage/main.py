from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.graphics.transformation import Matrix
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("collage.kv")

class ScatterPlane(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

    def on_touch_down(self, touch):
        # Personnalisation : Si 3 doigts, reset les scatters
        if len(self.parent.touches) == 3:
            for child in self.children:
                child.scale = 1.0
                child.rotation = 0
                child.pos = (0, 0)
            return True
        return super().on_touch_down(touch)

class CollageEditor(BoxLayout):
    plane = ObjectProperty(None, allownone=True)
    #plane = ScatterPlane()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plane = self.ids.plane

    def add_image(self):
        content = BoxLayout(orientation='vertical')
        filechooser = FileChooserIconView(filters=['*.png', '*.jpg', '*.img'])
        btn = Button(text="Choisir", size_hint_y=None, height=50)
        content.add_widget(filechooser)
        content.add_widget(btn)
        popup = Popup(title='Choisir Image', content=content, size_hint=(0.9, 0.9))
        btn.bind(on_press=lambda *args: self._load_image(filechooser.selection, popup))
        popup.open()

    def _load_image(self, selection, popup):
        if selection:
            img_path = selection[0]
            scatter = Scatter(
                size_hint=(None, None),
                size=(200, 200),
                do_rotation=True,
                do_scale=True,
                do_translation=True,
                translation_touches=1, # un doigt pour déplacer
                scale_min=0.5,
                scale_max=3,
                auto_bring_to_front=True
            )
            img = Image(source=img_path, size=(200, 200), size_hint=(None, None))
            scatter.add_widget(img)
            # Bind événement pour log
            scatter.bind(on_tranform_with_touch=self.on_transform)
            # Appliquer une transformation initiale
            mat = Matrix().rotate(0.1, 0, 0, 1) # Légère rotation
            scatter.apply_transform(mat, anchor=(100, 100))
            self.plane.add_widget(scatter)
        popup.dismiss()

    def on_transform(self, instance, touch):
        print(f"Transformation sur {instance}: scale={instance.scale}, rotate={instance.rotation}")

    def save_collage(self):
        # Simulation de Sauivegarde : Imprimez les états
        for child in self.plane.children:
            if isinstance(child, Scatter):
                print(f"Image : pos={child.pos}, scale={child.scale}, rotation={child.rotation}")
        # Pour une vraie Sauvegarde, utilisez kivy.graphics pour exportez en image

class CollageApp(App):
    def build(self):
        return CollageEditor()

if __name__ == '__main__':
    CollageApp().run()