# 1. Comprendre les Concepts Clés
# voir deepseek pour les descriptions

#2. kivy.uix.dropdown
# voir deepseek pour les descriptions

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout


class DropdownDemo(App):
    def build(self):
        layout = BoxLayout(padding=50)

        # bouton principal
        main_button = Button(
            text="Ouvrir le Menu",
            size_hint=(None, None),
            height=40
        )

        # Création du dropdown
        dropdown = DropDown()

        # Ajout d'options
        options = ["Python", "kivy", "Django", "PyQt"]
        for option in options:
            btn = Button(
                text=option,
                size_hint_y=None,
                height=40
            )
            # Lier l'événementde sélection
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        # Ouvrir le dropdown au clic
        main_button.bind(on_release=dropdown.open)

        # Mettre à jour le texte du bouton après sélection
        def update_main_button(instance, value):
            main_button.text = f"Choix : {value}"
            print(f"Option sélectionnée: {value}")

        dropdown.bind(on_select=update_main_button)

        layout.add_widget(main_button)
        return layout
if __name__ == '__main__':
    DropdownDemo().run()


# 3. kivy.uix.spinner
# voir deepseek pour les descriptions

# Exemple Complet :
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label

class SpinnerDemo(App):
    def build(self):
        layout = BoxLayout(
            orientation='vertical',
            padding=50,
            spacing=20
        )

        # Création du spinner
        spinner = Spinner(
            text='choisir un langage',
            values=("Python", 'JavaScript', 'C++', 'Rust', 'Go'),
            size=(200, 44),
            pos_hint={"center_x": 0.5}
        )

        # Label pour afficher la selection la selection
        self.selection_label = Label(
            text="Aucune Selection",
            font_size=20
        )

        # Gestion de la selection
        spinner.bind(text=self.on_spinner_select)

        layout.add_widget(spinner)
        layout.add_widget(self.selection_label)
        return layout

    def on_spinner_select(self, spinner, text):
        self.selection_label.text = f"Sélection: {text}"
        print(f"Spinner sélectionné: {text}")
if __name__ == '__main__':
    SpinnerDemo().run()

# 5. Best Pratiques et pièges courants
# voir deepseek pour les descriptions

# 6. Cas Avancé : Dropdown dynamique
# Créez des options dynamiquement basée sur des données externes :

# dans une méthode de classe
def build_dynamique_dropdown(self, data):
    dropdown = DropDown()
    for item in data:
        btn = Button(text=str(item), height=40, size_hint_y=None)
        btn.bind(on_release=lambda b: dropdown.select(b.text))
        dropdown.add_widget(btn)
    return dropdown

# Utilisation
data = [f"Item {i}" for i in range(10)]
dropdown = self.buil_dynamic_dropdown(data)
button.bind(on_release=dropdown.open)

#. Exercices pratiques
# voir deepseek pour les descriptions

# 8. Ressources supplémentaire