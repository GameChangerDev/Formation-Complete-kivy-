#. 1. introduction
# voir deepseek pour les descriptions

# 2. propriétés communes
# active
# disabled

# 3. Evénements communs
# on_active
# on_release

# Partie 1: kivy.uix.checkbox
# Exemple 1: CheckBox Basique

from kivy.app import App, runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

class CheckBoxApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Création du CheckBox
        self.checkbox = CheckBox(active=False)
        self.label = Label(text="CheckBox : Désactivé")

        # Lier l'événement
        self.checkbox.bind(active=self.on_checkbox_active)

        layout.add_widget(self.label)
        layout.add_widget(self.checkbox)
        return layout

    def on_checkbox_active(self, instance, value):
        self.label.text = f"CheckBox : {"Activé" if value else "Désactivé"}"


#Exemple 2: Groupe de CheckBox (Exclusif comme RadioButtons)

class CheckBoxGroupApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Options et groupe
        options = ["Option 1", "Option 2", "Options 3"]
        self.labels = {}

        for option in options:
            box = BoxLayout(spacing=10)
            checkbox = CheckBox(group="options") # Même groupe pour l'exclusivité
            label = Label(text=option)

            checkbox.bind(active=lambda inst, val, opt=option: self.on_select(opt, val))
            self.labels[option] = label

            box.add_widget(checkbox)
            box.add_widget(label)
            layout.add_widget(box)

        return layout

    def on_select(self, option, value):
        print(f"{option} sélectionné : {value}")


# Partie 2: kivy.uix.switch
# Exemple 1: Switch Basique

from kivy.uix.switch import Switch

class SwitchApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.switch = Switch(active=False)
        self.label = Label(text="Switch: OFF")

        self.switch.bind(active=self.on_switch_active)

        layout.add_widget(self.label)
        layout.add_widget(self.switch)
        return layout

    def on_switch_active(self, instance, value):
        self.label.text = f"Switch: {'ON' if value else 'OFF'}"


# Exemple 2: Switch avec Actions spéciphiques

class AdvancedSwitchApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.switch = Switch(active=False)
        self.switch.bind(active=self.toggle_feature)

        layout.add_widget(Label(text="Activer la fonctionnalité:"))
        layout.add_widget(self.switch)
        return layout

    def toggle_feature(self, instance, value):
        if value:
            print("Fonctionnalitée activée: Lancement du procéssus...")
            #Code pour activer
        else:
            print("Fonctionnalitée désactivée.")
            # Code pour désativer


# 4. Différences Clés
# voir deepseek pour les descriptions

# 5. Bonnes Pratiques
# voir deepseek pour les descriptions

# 6. Exercice Pratiques
# objectif : Créer un formulaire avec :
# 1 Switch pour activer les notifications.
# 3 CheckBox pour "Email", "SMS", "Push" (visibles seulement si le Switch est activé
"""
class ExerciceApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.switch = Switch(active=False)
        self.switch.bind(active=self.update_layout)
        self.layout.add_widget(self.switch)
        self.labels = {}

        return self.layout

    def update_layout(self, instance, value):
        if value:
            notifs = ["Email", "SMS", "Push"]
            self.box1 = BoxLayout(orientation='vertical', spacing=10)

            for notif in notifs:
                self.box = BoxLayout()
                label = Label(text=notif)
                checkbox = CheckBox(group="notifications")
                checkbox.bind(active=self.reacts_notifs)

                self.box.add_widget(label)
                self.box.add_widget(checkbox)

                self.box1.add_widget(self.box)

            self.layout.add_widget(self.box1)

        else:
            self.layout.remove_widget(self.box1)

    def reacts_notifs(self, instance, value):
        print(f"{value}")

if __name__ == '__main__':
    ExerciceApp().run()
"""
# version corrigée
class NotificationForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10, **kwargs)

        # Switch pour activer/désactiver les notifications
        self.switch = Switch(active=False)
        self.switch.bind(active=self.toggle_notifications)
        self.add_widget(Label(text="Activer les notifications:"))
        self.add_widget(self.switch)

        # layout pour les options (désativé initialement)
        self.options_layout = BoxLayout(orientation='vertical', spacing=5)
        self.options_layout.disabled = True
        self.options_layout.opacity = 0.5 # Rendre semi-transparent

        options = ["Email", "SMS", "Notifications Push"]
        self.checkboxes = {}
        for option in options:
            cb = CheckBox()
            self.checkboxes[option] = cb
            row = BoxLayout(spacing=10)
            row.add_widget(cb)
            row.add_widget(Label(text=option))
            self.options_layout.add_widget(row)

        self.add_widget(self.options_layout)

    def toggle_notifications(self, instance, value):
        self.options_layout.disabled = not value
        self.options_layout.opacity = 1.0 if value else 0.5

class NotificationApp(App):
    def build(self):
        return NotificationForm()

if __name__ == '__main__':
    NotificationApp().run()
