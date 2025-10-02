from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.rst import RstDocument
from kivy.lang import Builder
from kivy.properties import DictProperty
import os

Builder.load_file("app.kv")

class Preload(RstDocument):
    def __init__(self, full_path, **kwargs):
        super().__init__(**kwargs)
        self.source = full_path
    def prelaod_doc(self):
        print(self.toctrees)
        return self.preload(self.full_path)

class RstReader(BoxLayout):
    colors = DictProperty({'background': "0000ff", "title": 'ff0000'})

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.doc_root = "docs/"
        self.current_doc = "intro.rst"
        self.load_doc(self.current_doc)
        self.bind(colors=self.update_theme)

    def load_doc(self, filename):
        full_path = os.path.join(self.doc_root, self.current_doc)
        info = Preload(full_path)
        self.ids.title.text = info.toctrees.get(full_path, [])[0].get('title', 'Sans Titre')

        self.doc = RstDocument(source=full_path)
        self.doc.size = (500, 500)
        self.doc.bind(on_ref_press=self.handle_ref)

        self.ids.content.clear_widgets()
        self.ids.content.add_widget(self.doc)

        # Afficher toctree comme boutons
        toctree = info.toctrees[full_path][0]['children']
        self.ids.nav.clear_widgets()
        for item in toctree:
            btn = Button(text=item, on_press=lambda b, i=item: self.load_doc(i + '.rst'))
            self.ids.nav.add_widget(btn)

    def handle_ref(self, instance, ref):
        print(f"reférence cliquée {ref}")
        # Logique custom : exemple charger un fichier externe

    def update_theme(self, *args):
        if hasattr(self, 'doc'):
            self.doc.colors = self.colors
            self.doc.render() # Refaire le rendu du document

    def search(self, query):
        # Recherche simple : Mettre à jour text avec filtre (avancé : utiliser regex sur RST)
        if hasattr(self, 'doc'):
            original = self.doc.text
            highlighted = original.replace(query, f"**{query}")
            self.doc.text = highlighted
            self.doc.render()

class RstApp(App):
    def build(self):
        return RstReader()

if __name__ == '__main__':
    RstApp().run()