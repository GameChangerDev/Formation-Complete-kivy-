from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.vkeyboard import VKeyboard
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.metrics import dp, sp
import os
import hashlib
import secrets

from sqlalchemy.util import ellipses_string

# Config globale pour clavier
Config.set('kivy', 'keyboard_layout', 'numeric.json')
Config.set('kivy', 'keyboard_mode', '')

class SecureCryptoInput(BoxLayout):
    text_input = ObjectProperty()
    keyboard = None
    stored_hash = None # Hash stocké (simulé)
    salt = None        # Sel aléotoire sécurisé

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.text_input = TextInput(multiline=False, password=True, password_mask='+')
        self.add_widget(self.text_input)
        btn_switch = Button(text="Switch Layout / Mode")
        btn_switch.bind(on_press=self.switch_layout_mode)
        self.add_widget(btn_switch)
        btn_set_pass = Button(text="Définir mot de passe (Simulé)")
        btn_set_pass.bind(on_press=self.set_password)
        self.add_widget(btn_set_pass)

        # Bind focus pour afficher clavier
        self.text_input.bind(focus=self.on_focus)

        # Simulation d'un mot de passe stoché hashé (ex: "secret123")
        self.set_password(None) # Initialise avec un mot de passe par défaut

    def set_password(self, instance):
        # Génère un sel aléatoire sécurisé avec secrets
        self.salt = secrets.token_bytes(16) # 16 bytes pour sel fort
        password = "secret123"  # en production, il faut demandez à l'utilisateur
        # Hash avec l'algorithme SHA-256 et sel
        hash_obj = hashlib.sha256(self.salt + password.encode("utf-8"))
        self.stored_hash = hash_obj.hexdigest()
        print(self.stored_hash)
        print("Mot de passe Hashé stocké (simulé).")

    def on_focus(self, instance, value):
        if value:
            self.keyboard = Window.request_keyboard(callback=lambda *args: print(), target=self.text_input)
            print("La configuration ne permet pas que la fenêtre d'envoyer un clavier") if self.keyboard.widget is None else print("c'est bon")
            if self.keyboard.widget:
                kb = self.keyboard.widget   # Accès à vkeyboard
                # Note: Nous ne settons pas target ici, pour gérer manuellement l'insertion
                kb.layout_path = os.path.join(os.getcwd(), "keyboards")     # path Custom
                kb.available_layouts = {"numeric": "numeric.json", "alphanum": "alphanum.json"} # Layouts disponibles
                kb.layout = 'numeric'   # Début avec numeric
                kb.docked = True # Début en Mode docked
                kb.set_mode()   # Applique mode
                # Propriétés pour thème et layout
                kb.background_color = [0.1, 0.1, 0.1, 1]    # Thème dark renforcé
                kb.key_background_color = [0.7, 0.7, 0.7, 1]
                kb.font_size = sp(28)   # Taille de la police ajusté
                kb.margin_hint = [0.08, 0.08, 0.08, 0.08]   # Marge relatives
                kb.key_margin = [4, 4, 4, 4] # Marges touches
                # bind événement pour filtrage crypto et insertion manuelle
                kb.bind(on_key_down=self.on_key_down_custom)

    def close_keyboard(self):
        print("Clavier fermé. Validation Finale...")
        self.validate_password()
        if self.keyboard:
            self.keyboard.release()

    def switch_layout_mode(self, instance):
        if self.keyboard and self.keyboard.widget:
            kb = self.keyboard.widget
            # Switch layout (utilise available_layouts)
            kb.layout = "alphanum" if kb.layout == 'nimeric' else "alphanum"
            # Switch mode docked/free
            kb.docked = not kb.docked
            kb.set_mode()   # Appliquer les changements
            kb.refresh(True)    # refresh forcé pour mise à jour
            # Exemple d'utilisation de collide_margin
            print("Mode Switché. Margin Collision check:", kb.collide_margin(0, 0))    # test Marge

    def on_key_down_custom(self, instance, keycode, text, modifiers):
        print(f"Touche Préssée : {keycode}, Texte: {text}, Modifiers: {modifiers}")
        # Gestion manuel de l'insertion pour contrôle total
        max_length = 12
        current_length = len(self.text_input.text)

        if keycode == "backspace":
            self.text_input.do_backspace()
        elif keycode == "enter":
            self.validate_password()
        elif text:  # Pour les caractères insertables
            if current_length < max_length:
                self.text_input.insert_text(text)
            else:
                print("Limite de longueur atteinte.", len(self.text_input.text), " > ", max_length)
        # Exemple crypto partiel : Hash intermédiare pour débug(non stocké)
        temp_hash = hashlib.sha256(self.text_input.text.encode("utf-8")).hexdigest()
        print(f"Hash intermédiaire (debug): {temp_hash[:10]}...")   # Tronqué pour sécurité
        # pas de return True ou False nécessaire, car gérons tout ici

    def validate_password(self):
        input_pass = self.text_input.text
        if not input_pass:
            print("Aucune saisie.")
            return
        # Hash saisie avec le même sel
        hash_obj = hashlib.sha256(self.salt + input_pass.encode("utf-8"))
        input_hash = hash_obj.hexdigest()
        if input_hash == self.stored_hash:
            print("Mot de passe valide ! Accès accordé.")
        else:
            print("Mot de pase invalide.")
        # Effacer la saisie pour la sécurité
        self.text_input.text = ''

class SecureCryptoApp(App):
    def build(self):
        return SecureCryptoInput()

if __name__ == '__main__':
    SecureCryptoApp().run()