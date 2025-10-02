from kivy.uix.splitter import Splitter
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout as blt
from kivy.app import runTouchApp
from random import choice

def on_sizable(instance):
    print(instance)
    instance.sizable_from = choice(["right", "bottom"])

splt = Splitter(size_hint=(1, None), height='90dp', sizable_from='bottom', pos_hint={"top": 1}, orientation='horizontal')
bx = blt(orientation='vertical', size_hint=(1, None), height='90dp')

for i in range(5):
    bx.add_widget(Button())

splt.strip_size = '5dp'
splt.bind(on_release=on_sizable)
splt.add_widget(bx)

#runTouchApp(splt)

# kivy.uix.treeview
# regarder la documentation, le code source ou [deepseek, grok apk]
from kivy.uix.treeview import TreeView
# 1. Usage basique
from kivy.app import App
from kivy.uix.treeview import TreeView, TreeViewLabel

class TestApp(App):
    def build(self):
        tv = TreeView(hide_root=True, size_hint=(1, 1))

        # Noeud racine invisible
        root = tv.add_node(TreeViewLabel(text="Racine"))

        # Enfants niveau 1
        child1 = tv.add_node(TreeViewLabel(text='Enfant 1', is_open=True), root)
        child2 = tv.add_node(TreeViewLabel(text="Enfant 2"), root)

        # Enfants niveau 2
        tv.add_node(TreeViewLabel(text="Sous-Enfant 1"), child1)
        tv.add_node(TreeViewLabel(text="Sous-Enfant 2"), child1)

        # Enfants pour le child 2
        tv.add_node(TreeViewLabel(text="Sous-Enfant"), child2)
        tv.add_node(TreeViewLabel(text="Sous-Enfant"), child2)

        return tv

TestApp().run()

# 2., 3.,4., 5.

# Cas pratique: SplitEditor-Editeur de texte avec panneaux redimentionnable

from kivy.app import App
from kivy.uix.splitter import Splitter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.properties import ObjectProperty
from json import dump

dispo = JsonStore("disposition.json", indent=2)

# KV pour stylisation custom
Builder.load_string("""
<CustomStrip@Button>:
    background_color: 0.2, 0.2, 0.5, 1  # Barre bleue
    text: "||"  # Icône simple
    size_hint: None, None
    width: 15 
    height: 15
""")

class CustomSplitter(Splitter):
    strip_cls = Factory.get("CustomStrip")
    toggle_btn = ObjectProperty()
    root = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.min_size = 150 # Propriétés min/max
        self.max_size = 800
        self.rescale_with_parent = True # Auto-Rescale
        self.keep_within_parent = True
        self.bind(size=self.on_size_change) # Binding à size

    def on_press(self, *args):
        print("Splitter pressé")
        anim = Animation(opacity=0.5, duration=0.2) # Animation sur press
        anim.start(self._strip)
        super().on_press(*args)

    def on_release(self, *args):
        print("Splitter relâché !")
        anim = Animation(opacity=1, duration=0.2)
        anim.start(self._strip)
        super().on_release(*args)

    def on_size_change(self, instance, size):
        print(f"Taille changé en {size}")
        self.size = size
        print(self.width)

    def on_touch_move(self, touch):
        super().on_touch_move(touch)
        def update_pos(dt):
            self.toggle_btn.x = self.width

        from kivy.clock import Clock
        Clock.schedule_once(update_pos, 0.001)
        #Clock.schedule_once(update_witdh, 0.002)

    def on_touch_up(self, touch):
        tree={
            "splitter_width":self.width,
            "toggle_with": Window.width - self.width
        }
        dispo.put("disposition", **tree)


class SplitEditorApp(App):
    def build(self):
        root = BoxLayout()
        # bouton pour toggle (ex. clear_widget ou remove)
        self.toggle_btn = Button(text="Toggle Output", size_hint_y=None, height=50)
        self.toggle_btn.x = dispo.get("disposition")["toggle_with"]

        # Splitter vertical pour arborescence vs. éditeur
        vertical_splitter  = CustomSplitter(sizable_from="right", strip_size=15, toggle_btn=self.toggle_btn)

        # box Pour le contenu
        box = BoxLayout(orientation="vertical")
        file_tree = TreeView(root_options=dict(text='Fichiers'))
        for i in range(3):
            node = file_tree.add_node(TreeViewLabel(text=f"Fichier {i}"))
        box.add_widget(file_tree)

        # Editeur de code
        code_editor = TextInput(hint_text="Écrivez du code ici ...")
        box.add_widget(code_editor)
        vertical_splitter.add_widget(box)

        # Splitter horizontal principal
        horizontal_splitter = CustomSplitter(sizable_from="top", orientation="vertical", toggle_btn=self.toggle_btn)
        horizontal_splitter.add_widget(vertical_splitter)   # Imbrication

        # Output panel
        output = Label(text='Output ici', size_hint_y=None, height=200)
        horizontal_splitter.add_widget(output)

        self.toggle_btn.bind(on_press=self.toggle_output)
        horizontal_splitter.bind(size=self.size)
        self.output = output    # pour Accès
        self.horizontal_splitter = horizontal_splitter

        root.add_widget(horizontal_splitter)
        root.add_widget(self.toggle_btn)
        self.root = root

        return root

    def toggle_output(self, btn):
        if self.output in self.horizontal_splitter.children:
            self.horizontal_splitter.remove_widget(self.output)
        else:
            self.horizontal_splitter.add_widget(self.output)

    def size(self, inst, val):
        self.horizontal_splitter.toggle_btn = self.toggle_btn
        self.horizontal_splitter.root = self.root

if __name__ == '__main__':
    SplitEditorApp().run()