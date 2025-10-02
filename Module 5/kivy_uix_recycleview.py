# voire grok apk et deepseek pour les description
# 1, 2, 3
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout

# les données sont une liste de dictionnaires ou chaque dictionnaire represente un élément
data = [{'text': str(x)} for x in range(100)]

# Exemple complet:

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.effects.opacityscroll import OpacityScrollEffect
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout

#KV = '''
'''
<RV>:
    viewclass: 'Label'
    RecycleBoxLayout:
        default_size: None, dp(50)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
'''
"""
class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]

class TestApp(App):
    def build(self):
        Builder.load_string(KV)
        return RV()
"""
#if __name__ == '__main__':
#    TestApp().run()


# 3. Fonctionnalités avancées de RecycleView
# Exemple pour selection multiple :

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

KV = '''
<SelectableLabel>:
    canvas.before:
        Color:
            rgba: (0.0, 0.9, 0.1, 0.3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
<RV>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        touch_multiselect: True
'''

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    pass

class SelectableLabel(RecycleDataViewBehavior, Label):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super().refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if super().on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return  self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected

class RV(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]

class TestApp(App):
    def build(self):
        Builder.load_string(KV)
        return RV()

if __name__ == '__main__':
    TestApp().run()