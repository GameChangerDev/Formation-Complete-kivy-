import os.path
from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.datamodel import RecycleDataModel
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.stencilview import StencilView
from kivy.uix.image import Image, AsyncImage
from kivy.graphics import StencilPush, StencilUse, StencilUnUse, StencilPop, Rectangle, Ellipse
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from os import path, listdir



KV = '''
<RV>:
    viewclass: 'PersoButton'
    Box:
        default_size: None, dp(25)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        spacing: 5
        padding: [10, 0, dp(20), 0]
        bar_width: dp(15)
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
'''
def fichier():
    folders = []
    folders_files = {}
    folder = ""
    files_finals = []
    while not folder.isdigit():
        folder = input('chemin du dossier :')
        if not (folder.isdigit()):
            folders.append(folder)

    for folder in folders:
        folders_files[folder] = listdir(folder)

    for folder, files in folders_files.items():
        liste = [path.join(folder, file) for file in files if path.isdir(folder) and path.isfile(path.join(folder, file))]
        files_finals.extend(liste)
    return files_finals

#files_final = fichier()
#print(files_final)
"""
class PersoButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_press=self.react_press)

    def react_press(self, button:Button):
        texte = self.fouille(button.text)
        son = SoundLoader.load(texte)
        if son:
            son.play()

    def fouille(self, element):
        for file in files_final:
            if element in file:
                return file

class Box(RecycleBoxLayout, LayoutSelectionBehavior, FocusBehavior):
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if super().keyboard_on_key_down(window, keycode, text, modifiers):
            return True
        if self.select_with_key_down(window, keycode, text, modifiers):
            return True
        return False

    def keyboard_on_key_up(self, window, keycode):
        if super().keyboard_on_key_up(window, keycode):
            return True
        if self.select_with_key_up(window, keycode):
            return True
        return False

    def select_node(self, node):
        node.background_color = (0, 1, 0, 1)
        return super().select_node(node)

    def deselect_node(self, node):
        node.background_color = (1, 1, 1, 1)
        return super().deselect_node(node)

    def add_widget(self, widget, *args, **kwargs):
        widget.bind(on_touch_down=self.react_touch_down, on_touch_up=self.react_touch_up)
        return super().add_widget(widget, *args, **kwargs)

    def react_touch_down(self, button:Button, touch):
        if button.collide_point(*touch.pos):
            self.select_with_touch(button, touch)

    def react_touch_up(self, button:Button, touch):
        if not (button.collide_point(*touch.pos) or self.touch_multiselect):
            self.deselect_node(button)

    def apply_selection(self, index, view, is_selected):
        print(is_selected)


class RV(RecycleView, RecycleDataModel):
    data = [{'text': file.split("\\")[-1]} for file in files_final]


class RVApp(App):
    def build(self):
        Builder.load_string(KV)
        return RV()
"""
#RVApp().run()


from kivy.uix.floatlayout import (FloatLayout)

class StencilPerso(StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (248, 248)
        self.size_hint = (None, None)
        #self.pos = (300, 10)
        if self.parent:
            self.pos = self.parent.x/2
        self.orientation = 'vertical'
        with self.canvas.before:
            StencilPush()
            self.cercle = Ellipse(size=(self.size[0]/1.5, self.size[1]/1.5))
            StencilUse()
        self.img = AsyncImage(source=os.path.join(r"C:\Users\DELL\Pictures\Photos a traiter", "IMG_20241222_103433_242.jpg"), size=self.size, pos_hint= self.pos_hint)
        self.add_widget(self.img)
        with self.canvas.after:
            StencilUnUse()
            StencilPop()

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        x, y = touch.pos
        self.cercle.size = (64, 64)
        self.cercle.pos = (x, y)

        print(self.cercle.size, self.cercle.pos)
    def on_touch_move(self, touch):
        self.cercle.pos = touch.pos
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        from kivy.core.window import Window
        Window.screenshot(r"C:\Users\DELL\Pictures\Photos a traiter\masque.png")


class StencilApp(App):
    def build(self):
        layout = FloatLayout()
        stencil = StencilPerso()
        #stencil.add_widget(AsyncImage(source=os.path.join(r"C:\Users\DELL\Pictures\Photos a traiter", "IMG_20241222_103433_242.jpg")))

        layout.add_widget(stencil)
        print(stencil.size_hint, stencil.size,stencil.parent)
        return layout

StencilApp().run()