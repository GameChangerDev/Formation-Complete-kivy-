from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from json import load
from kivy.factory import Factory

Builder.load_file("Box.kv")

class Box(BoxLayout):
    def builder(self, config):

        with open("interface.json") as f:
            config = load(f)
        self.root = Factory.get(config.get("root"))(**config.get('properties'))

        # Ajout de widget:
        for child_widget in config.get('children', {}):
            widget = self.create_widget(child_widget)
            self.root.add_widget(widget)

        self.clear_widgets()
        self.add_widget(self.root)

    def create_widget(self, config):

        widget = Factory.get(config.get("widget", Factory.get("Widget")))(**config.get("properties", {}))

        # ajout dynamique d'events
        for event, callback in config.get('events', {}).items():
            widget.bind(**{event: getattr(self, callback)})

        return widget

    def react_press(self, instance, *args):
        if isinstance(instance, Factory.get("TextInput")):
            print(instance)
            if not instance.readonly:
                instance.readonly = True
            else:
                instance.readonly = False
        print("event déclenché !")

class BoxUIAPP(App):
    def build(self):
        root = Box()
        root.builder('interface.json')

        return root

if __name__ == '__main__':
    BoxUIAPP().run()