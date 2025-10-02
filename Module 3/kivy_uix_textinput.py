# voir dans deepseek pour certaines descriptions

# 1. importation de base &&
#2. Création d'un TextInput Simple

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class SimpleTextInput(App):
    def build(self):
        return TextInput(text="Saisissez ici")
#SimpleTextInput().run()

# Propriétés Clés
# # voir dans deepseek pour certaines descriptions

# 4. Exemples Avancés
# Exemple 1: Validation de texte(Entrée)

class ValidatedInput(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.text_input = TextInput(
            hint_text="Appuyez sur Entrée",
            multiline=False,
            size_hint_y=None,
            height=50
        )
        self.text_input.bind(on_text_validate=self.validate)# événement déclenché quand on appui sur entrée avec multiline = False

        layout.add_widget(self.text_input)
        return layout

    def validate(self, instance):
        print("Texte validé :", instance.text)
        instance.text = "" # Réinitialisation

#ValidatedInput().run()

# Exemple 3: Filtrage de saisie
class NumericInput(App):
    def build(self):
        ti = TextInput(hint_text="Chiffres uniquement")
        ti.input_filter = "float"
        return ti
#NumericInput().run()

# Exemple 4 : Activer/Désactiver Dynamiquement

class ToggleInput(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        self.ti = TextInput(text="Cliquez sur le bouton")
        btn = Button(text="Activer/Désactiver")
        btn.bind(on_press=self.toggle)

        box.add_widget(self.ti)
        box.add_widget(btn)
        return box

    def toggle(self, instance):
        self.ti.readonly = not self.ti.readonly

#ToggleInput().run()

# Exemple 5 : Focus et Style
class StyleedInput(App):
    def build(self):
        return TextInput(
            hint_text="Style Personnalisée",
            background_color=(0.9, 0.9, 1, 1),  #   arrière plan Bleue clair
            foreground_color=(0, 0, 0.5, 1),    #   texte bleu foncé
            font_size=20,
            padding=[20, 10]
        )
#StyleedInput().run()

#5. Gestion des événements : on_focus, on_text_validate, on_text
class EventInput(App):
    def build(self):
        ti = TextInput(base_direction="rtl")
        ti.bind(
            focus=self.on_focus, # quand le champ gagne/perd le focus
            text=self.on_text_change # quand la valeur de text change
        )
        return ti

    def on_focus(self, instance, value):
        print(f"Focus : {value}")

    def on_text_change(self, instance, value):
        print(f"Nouveau texte : {value}")

#EventInput().run()

#6. Astuces Pro
    #1. accès au texte
#textinput_instance.text
    #2. Curseur :
#ti.cursor = (0, 0) # Position (row, col)
    #4. Sélection :
#ti.select_all() # selectionner tout
    #5. Défilement automatique
#ti.scroll_x = 0 # Réinitialiser le défilement

#Exemple Complet : Formulaire de Connexion

class LoginForm(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)

        # Champs de saisie
        self.username = TextInput(hint_text="Nom d'utilisateur")
        self.password = TextInput(hint_text="Mot de passe" ,password=True)

        # Bouton de soumission
        submit = Button(text="Connexion")
        submit.bind(on_press=self.login)

        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(submit)
        return layout

    def login(self, instance):
        print(f"Connexion : {self.username.text}/{self.password.text}")
        # Réinitialisation des valeurs
        self.username.text = ""
        self.password.text = ""

#LoginForm().run()

#8. Bonne pratiques
# voir dans deepseek