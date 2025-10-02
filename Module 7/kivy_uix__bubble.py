from kivy.uix.boxlayout import BoxLayout
from kivy.uix.bubble import Bubble
# voirs les descriptions dans grok apk ou Deepseek

# Cas Pratique : Application de dessin simple
from kivy.app import App
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import ListProperty, ObjectProperty
from kivy.core.window import Window


class DrawingCanvas(Widget):
    lines = ListProperty([])
    bubble = ObjectProperty()

    def recardre(self):
        self.bubble.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #self.bubble.pos = (Window.width-self.bubble.width, Window.height-self.bubble.height)

    def on_touch_down(self, touch):
        try:
            if self.bubble in self.parent.children:
                self.parent.remove_widget(self.bubble)
        except Exception as e:
            print(e)
        if touch.button == "left": # Clic droit pour menu
            self.bubble = self.show_bubble(touch)
            return True

        with self.canvas:
            self.couleur = Color(1, 0, 0, 1)   # Couleur par défaut
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            self.ligne = Line(points=(touch.x, touch.y))

        self.lines.append(touch.ud['line'])
        if touch.is_double_tap:
            print(f"Double Clic validé , angle: {touch.button}")

    def on_touch_move(self, touch):
        try:
            if self.bubble in self.parent.children:
                self.parent.remove_widget(self.bubble)
        except Exception as e:
            print(e)
        self.bubble = self.show_bubble(touch)
        if 'line' in touch.ud:
            #touch.ud['line'].points += touch.pos#(touch.x, touch.y)
            self.ligne.points += touch.pos

        Window.bind(on_cursor_leave=lambda *args: self.recardre())

    def on_touch_up(self, touch):
        self.bubble = self.show_bubble(touch)

    def show_bubble(self, touch):
        bubble = CustomBubble(pos=(touch.x, touch.y), content_size=(100, 100))
        lay = BoxLayout(orientation="vertical", size_hint=(0.3, 0.3))
        lay.add_widget(BubbleButton(text='changer couleur', on_press=self.change_color, size_hint_y=None, height=40))
        lay.add_widget(BubbleButton(text='Effacer', on_press=self.clear_canvas, size_hint_y=None, height=40))
        lay.add_widget(BubbleButton(text="Sauvegarder", on_press=self.save_canvas, size_hint_y=None, height=40))


        bubble.add_widget(lay)
        bubble.background_color = [0.1, 0.1, 0.1, 0.9]
        bubble.arrow_pos = 'bottom_mid'
        bubble.orientation = 'horizontal'

        # Animation
        bubble.scale = 0.5
        anim = Animation(scale=1, duration=0.2)
        anim.start(bubble)

        self.parent.add_widget(bubble)
        return bubble


    def change_color(self, instance):
        # Logique pour changer la couleur
        import random
        self.canvas.before.clear()
        with self.canvas.before:
            Color(random.random(), random.random(), random.random(), 1)
        self.close_bubble(instance.parent)

    def clear_canvas(self, instance):
        self.canvas.clear()
        self.lines = []
        self.close_bubble(instance.parent)

    def save_canvas(self, instance):
        # Exemple: exporter en PNG
        self.export_to_png("drawing.png")
        self.close_bubble(instance.parent)

    def close_bubble(self, bubble):
        if bubble.parent:
            bubble.parent.remove_widget(bubble)

class CustomBubble(Bubble):
    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            self.parent.remove_widget(self)
            return True
        return super().on_touch_move(touch)

class DrawingApp(App):
    def build(self):
        root = FloatLayout()
        canvas = DrawingCanvas()
        root.add_widget(canvas)
        return root
if __name__ == '__main__':
    DrawingApp().run()