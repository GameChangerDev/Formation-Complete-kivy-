# Créer un tableau de bord de contrôle pour un systeme domotique
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch
from kivy.uix.spinner import Spinner
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.clock import Clock

class DomotiqueDashbord(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # Titre
        self.add_widget(Label(text='SYSTEME DOMOTIQUE MAISON', font_size=24, bold=True))

        # Conteneur principal
        main_grid = GridLayout(cols=2, spacing=20)

        # colonne de gauche - Contrôles
        left_column = BoxLayout(orientation='vertical', spacing=15)

        # 1. Section Lumière (toggleButton)
        light_box = BoxLayout(orientation="vertical", spacing=5)
        light_box.add_widget(Label(text="Contrôle Lumière"))
        self.light_toggle = ToggleButton(text='Lumière ÉTEINTE', group='light')
        self.light_toggle.bind(on_press=self.toggle_light)
        light_box.add_widget(self.light_toggle)
        left_column.add_widget(light_box)

        # 2. Section Température (Slider + ProgressBar)
        temp_box = BoxLayout(orientation='vertical', spacing=5)
        temp_box.add_widget(Label(text='Température:', bold=True))
        self.temp_slider = Slider(min=15, max=30, value=20, step=1)
        self.temp_slider.bind(value=self.update_temp)
        temp_box.add_widget(self.temp_slider)
        self.temp_display = ProgressBar(max=30, value=20)
        temp_box.add_widget(self.temp_display)
        self.temp_label = Label(text='20°C')
        temp_box.add_widget(self.temp_label)
        left_column.add_widget(temp_box)

        # 3. Section Sécurité (TextInput + CheckBox)
        security_box = BoxLayout(orientation='vertical', spacing=5)
        security_box.add_widget(Label(text='Système de Sécurité:', bold=True))

        # Code d'accès
        code_box = BoxLayout(spacing=10)
        code_box.add_widget(Label(text='Code:', bold=True))
        self.code_input = TextInput(password=True, multiline=False, hint_text="Exemple@123")
        code_box.add_widget(self.code_input)
        self.validate_btn = Button(text="Valider", size_hint_x=0.4)
        self.validate_btn.bind(on_press=self.check_code)
        code_box.add_widget(self.validate_btn)
        security_box.add_widget(code_box)

        # options sécurité
        options_box = GridLayout(cols=2, spacing=10)
        self.alarm_check = CheckBox(active=True)
        options_box.add_widget(Label(text='Alarme Activé:'))
        options_box.add_widget(self.alarm_check)

        self.camera_switch = Switch(active=False)
        options_box.add_widget(Label(text='Caméras:'))
        options_box.add_widget(self.camera_switch)
        security_box.add_widget(options_box)
        left_column.add_widget(security_box)

        # Colonne de droite - Monitoring
        right_column = BoxLayout(orientation='vertical', spacing=15)

        # 4. Section Appareils (Spinner)
        devices_box = BoxLayout(orientation='vertical', spacing=5)
        devices_box.add_widget(Label(text='Appareils Connectés:', bold=True))
        self.device_spinner = Spinner(
            text='Sélectionnez un appareil',
            values=('TV Salon', 'Four', 'Lave-linge', 'Aspiration Robot')
        )
        self.device_status = Label(text='Statut: Inconnu')
        self.device_spinner.bind(text=self.show_device_status)
        devices_box.add_widget(self.device_spinner)
        devices_box.add_widget(self.device_status)
        right_column.add_widget(devices_box)

        # 5. Section sénarios (Dropdown)
        scenario_box = BoxLayout(orientation='vertical', spacing=5)
        scenario_box.add_widget(Label(text='Scénarios Domotiques:', bold=True))

        # Menu déroulant
        self.scenario_dropdown = DropDown()
        scenarios = ['Maison Vide', 'Soirée Cinéma', 'Retour Travail', 'Nuit']
        for scenario in scenarios:
            btn = Button(text=scenario, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.select_senario(btn.text))
            self.scenario_dropdown.add_widget(btn)

        self.scenario_btn = Button(text='Choisir un scénario')
        self.scenario_btn.bind(on_release=self.scenario_dropdown.open)
        self.scenario_dropdown.bind(on_select=lambda instance, x: setattr(self.scenario_btn, "text", x))
        scenario_box.add_widget(self.scenario_btn)
        right_column.add_widget(scenario_box)


        #6. Section consommation (Progressbar dynamique)
        energy_box = BoxLayout(orientation='vertical', spacing=5)
        energy_box.add_widget(Label(text="Consommation Energétique:", bold=True))
        self.energy_bar = ProgressBar(max=100)
        energy_box.add_widget(self.energy_bar)
        self.energy_label = Label(text="Charge: 0%")
        energy_box.add_widget(self.energy_label)
        right_column.add_widget(energy_box)

        # Simulation de consommation
        self.energy_level = 0
        Clock.schedule_interval(self.update_energy, 1)

        # Assemblage des colonnes
        main_grid.add_widget(left_column)
        main_grid.add_widget(right_column)
        self.add_widget(main_grid)

        # Journal des événements
        self.log_label = Label(text="Journal: Système initialisé", size_hint_y=0.2)
        self.add_widget(self.log_label)

    def toggle_light(self, instance):
        if instance.state == 'down':
            instance.text = "Lumière ALLUMEE"
            self.log_label.text += "\nLumière: Désactivée"
        else:
            instance.text = 'Lumière ETEINTE'
            self.log_label.text += "\nLumière: Désactivée"

    def update_temp(self, instance, value):
        self.temp_display.value = value
        self.temp_label.text = f"{int(value)}°C"

    def check_code(self, instance):
        code = self.code_input.text
        if code == "1234":
            self.log_label.text += "\nCode VALIDE - Sécurité désactivée"
            self.alarm_check.active = False
        else:
            self.log_label.text += "\nCode INVALIDE - Accès refusé"

    def show_device_status(self, instance, device):
        statues = {
            'TV Salon': 'Statut: Allumé',
            'Four': 'Statut: Eteint',
            'Lave-linge': 'Statut: En programme',
            'Apirateur Robot': 'Statut: En charge'
        }
        self.device_status.text = statues.get(device, "Statut: Inconnu")

    def select_senario(self, scenario):
        self.log_label.text += f"\nSénario activé: {scenario}"
        if scenario == 'Soirée Cinéma':
            self.light_toggle.state = 'down'
            self.light_toggle.text = 'Lumière ALLUMEE'
            self.temp_slider.value = 22

    def update_energy(self, dt):
        self.energy_level = (self.energy_level + 2) % 100
        self.energy_bar.value = self.energy_level
        self.energy_label.text = f"Charge: {self.energy_level}%"

class DomotiqueApp(App):
    def build(self):
        Window.clearcolor = (0.9, 0.9, 0.95, 1)
        return DomotiqueDashbord()

if __name__ == '__main__':
    DomotiqueApp().run()