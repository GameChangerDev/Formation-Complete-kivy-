import json
from kivy.app import  App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
#import widgets

Builder.load_string('''
<RootWidget>:
    id: root_widget
''')

Builder.load_file("dynamicui.kv")
for widget, details in Factory.classes.items():
    print(f"{widget} : {details}")

class RootWidget(BoxLayout):
    def build_ui(self, config):
        # Crée le widget racine
        root = Factory.get(config['root'])(**config.get("properties", {}))

        # Ajout recurcif des enfants
        for child_config in config.get('children', []):
            widget = self.create_widget(child_config)
            root.add_widget(widget)

        self.clear_widgets()
        self.add_widget(root)

    def create_widget(self, config):
        # Instanciation dynamique
        widget = Factory.get(config['widget'])(**config.get('properties', {}))

        # Gestion des événements
        for event, callback_name in config.get('events', {}).items():
            widget.bind(**{event: getattr(self, callback_name)})

        return widget

    def validate_input(self, instance):
        print("Validation réussie !")

class DynamicUIApp(App):
    def build(self):
        root = RootWidget()
        with open("ui_config.json", "r") as f:
            config = json.load(f)
        root.build_ui(config)
        return root

if __name__ == '__main__':
    DynamicUIApp().run()