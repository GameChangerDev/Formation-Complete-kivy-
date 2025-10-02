# 1. Introduction
# voir dans deepseek
import kivy.uix.togglebutton

#2.Configuration de Base
from kivy.app import App, runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label

Builder.load_string("""
<MainLayout>:
    orientation: 'vertical'
    padding: 20
    spacing: 10
""")

#3. kivy.uix.button.Button
# exemple 1: Bouton simple
class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = Button(text="Cliquez-moi", background_color=(0.2, 0.7, 0.3, 1), font_size=24)# couleur verte
        btn.bind(on_press=self.button_action)
        self.add_widget(btn)

    def button_action(self, instance):
        print("Bouton pressé")


# Exemple 2: Bouton avec image
btn_img = Button(
    background_normal=r"C:\Users\DELL\PycharmProjects\kivy_apprentissage\Module 1\kivy_core\png_boutons\FERME.png",
    background_down=r"C:\Users\DELL\PycharmProjects\kivy_apprentissage\Module 1\kivy_core\png_boutons\OUVERT.png",
    size_hint=(0.3, 0.3)
)

# 4. kivy.uix.togglebutton.ToggleButton
# Exemple 3 : Groupe  ToggleButton simple
class SampleToggle(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        toggle = ToggleButton(
            text="Activer",
            group=None # Groupe indépendant
        )
        toggle.bind(state=self.toggle_action)
        self.add_widget(toggle)

    def toggle_action(self, instance, state):
        print(f"Etat : {'Activé' if state =='down' else 'Désactivé'}")

# Exemple 4: Groupe de ToggleButton (Radio Buttons)

class RadioButtons(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout()
        group_name = "options"

        for option in ["Option 1", "Option 2", "Option 3", "Option 4"]:
            toggle = ToggleButton(
                text=option,
                group=group_name
            )
            toggle.bind(state=self.radio_action)
            layout.add_widget(toggle)

        self.add_widget(layout)

    def radio_action(self, instance, state):
        if state == 'down':
            print(f"Option sélectionnée : {instance.text}")


#5. personnalisation Avancée ||
    # style dynamique avec kv
"""
<CustomButton@Button>:
    background_color: (0.1, 0.5, 0.8, 1) if self.state=='normal' else (0.8, 0.2, 0.2, 1)
    font_size: 18
"""
    #ToggleButton avec icone
toggle = ToggleButton(
    background_normal=r"C:\Users\DELL\PycharmProjects\kivy_apprentissage\Module 1\kivy_core\png_boutons\FERME.png",
    background_down=r"C:\Users\DELL\PycharmProjects\kivy_apprentissage\Module 1\kivy_core\png_boutons\OUVERT.png"
)
layout = BoxLayout()

# Ajouter une icone + texte
layout.add_widget(Label(text=r"[color=00ff00][/color]", markup=True))
layout.add_widget(Label(text="Activer"))

toggle.add_widget(layout)


#6. Applications intégrées
# Exemple Complet : panneau de contrôle

class ControlPanel(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=20)

        # Bouton Standard
        btn_run = Button(text="Exécuter", size_hint_y=0.2)
        btn_run.bind(on_press=self.run_command)

        # groupe de toggles
        toggle_box = BoxLayout(size_hint_y=0.4)
        modes=["Mode 1", "Mode 2", "Mode 3", "Mode 4"]
        for mode in modes:
            toggle = ToggleButton(text=mode, group="modes")
            toggle.bind(state=self.set_mode)
            toggle_box.add_widget(toggle)

        # Toggle avec feedback visuel
        self.status = Label(text="Statut: Désactivé")
        toggle_status = ToggleButton(text="Activer Service")
        toggle_status.bind(state=self.toggle_service)

        root.add_widget(btn_run)
        root.add_widget(toggle_box)
        root.add_widget(self.status)
        root.add_widget(toggle_status)
        return root

    def run_command(self, instance):
        print(f"commande exécutée !!")

    def set_mode(self, instance, state):
        if state == "down":
            print(f"Mode {instance.text} sélectionné")

    def toggle_service(self, instance, state):
        self.status.text = f"Statut: {'Activé' if state == 'down' else 'Désactivé'}"

if __name__ == '__main__':
    ControlPanel().run()