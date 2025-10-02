# Projet Final : Tableau de bords intéractif
"""
Object :
    Créer un tableau de bord avec :
        ° Gestion dynamique des widgets
        ° interactions complexes
        ° Personnalisation via KV
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder



Builder.load_file('components/widgets.kv')
Builder.load_file('components/styles.kv')


commander="""
CustomCard:
    title: "Widget Dynamique"
    value: str(app.root.counter)
"""

class Dashboard(BoxLayout):
    counter = NumericProperty(0)
    data_points = ListProperty([25, 40, 35, 60, 30])
    status = StringProperty("Actif")

    def add_widget_dynamically(self):
        new_widget = Builder.load_string(commander)
        self.ids.widget_container.add_widget(new_widget)

    def update_graph(self, inst, touch):
        if self.collide_point(*touch.pos):
            self.data_points = [d + 5 for d in self.data_points]

class DashboardApp(App):
    def build(self):
        return Dashboard()

if __name__ == '__main__':
    DashboardApp().run()