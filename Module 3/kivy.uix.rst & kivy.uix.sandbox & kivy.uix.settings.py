#                   kivy.uix.rst
#  ===> Utile pour intégrer du contenu documentaire riche dans les applications comme : des manuels, tutoriels, ou aide
#  en lignes
import os.path
from configparser import ConfigParser

from kivy.uix.rst import RstDocument

# Cas pratique : Lecteur de Documentation RST
# voire le dossier lecteur_de_document_rst

#                   kivy.uix.sanbox
#  ===> utile pour pour contenir les enfants et empêcher que l'application crash quand un enfant lève une exception


# 1., 2., 3.
"""Création d'un handler personnaliqer"""
from kivy.uix.sandbox import Sandbox, SandboxExceptionManager
from kivy.app import runTouchApp, App
from kivy.clock import Clock
from kivy.uix.button import Button

for key, value in Sandbox()._context.items():
    print(f'{key}: {value}')

class Manager(SandboxExceptionManager):
    def handle_exception(self, e):
        super().handle_exception(e)
        print(f"Exception levée : {e}")
        return e

class Csandbox(Sandbox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._context["ExceptionManager"] = Manager(self)

    def on_exception(self, exception, _traceback=None):
        print(exception)
        return True

class ErrApp(App):
    def build(self):
        s = Csandbox()
        btn = Button(text="bouton")
        s.add_widget(btn)
        def mj(dt):
            btn.text = "fait"
            btn.wrap = "ooh"# Erreur consciente le andbox doit gérer

        Clock.schedule_once(mj, 2)
        return s
#
# if __name__ == '__main__':
#     ErrApp().run()


#           kivy.uix.settings
# ===> Créer et ajouter les interfaces de configuration(settings) dans l'application
# voir Module 1/ kivy_config.py pour les rappels sur Config
# 1., 2., 3.,

# Exemple Création d'un fichier de configution et un panneau setting puis création de panel de parramètre
# avec gestion de changement des paramètre
from kivy.uix.settings import Settings, SettingsWithSpinner, SettingsWithNoMenu, SettingsWithTabbedPanel
from kivy.config import ConfigParser
from json import dumps
panel_json =[
    {
        "type": "string",
        "title": "Nom d'utilisateur",
        "section": "Franklin",
        "key": "nom"
    }
]

conf = ConfigParser(name="conf")
conf.read(filename="conf.ini")
conf.set("Franklin", 'age', value="32")
conf.write()

s = SettingsWithTabbedPanel()
s.add_json_panel("Franklin", conf, data=dumps(panel_json))
s.add_kivy_panel()

def print_config_change(inst, config, section, key, value):
    print(f"{section}==>{key}==>{value}")

s.bind(on_config_change=print_config_change)
#runTouchApp(s)

#  pour enregistrer un type de donner personnalisée on utilise register_type
#==> s.register_type(tp="type", cls=MaClassPerso)

# 4. Creation de SettingItem personnalisé
# pour des réglages avancés héritez de SettingItem et surchargez.

from kivy.uix.settings import SettingItem, SettingOptions
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.popup import Popup

class SettingScrollableOptions(SettingOptions):
    def _create_popup(self, instance):
        # Surcharger pour un popup scrollable
        popup_width = min(0.95 * Window.width, dp(500))
        popup = Popup(title=self.title, content=ScrollView(), size_hint=(None, None), size=(popup_width, '400dp'))

        layout = GridLayout(cols=1, spacing='5dp', size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))
        print(self.options)
        for option in self.options:
            btn = Button(text=option, size_hint_y=None, height=dp(56))
            btn.bind(on_release=lambda x: self.select_and_dismiss(option, popup))
            layout.add_widget(btn)

        popup.content.add_widget(layout)
        popup.open()

    def select_and_dismiss(self, value, popup):
        self.value = value
        popup.dismiss()

# Enregistrez le type
s.register_type('scroll_options', SettingScrollableOptions)

scrol_option= [
    {
        "type": "scroll_options",
        "title": "Lettre Aleatoire",
        "section": "Franklin",
        "key": "lettre_a",
        "options": ["p", "a", "r", "q", "j", "c"]
    }
]
s.add_json_panel("Aléatoire", config=conf, data=dumps(scrol_option))
runTouchApp(s)


# Projet Pratique : App de Gestion de tâches avec Settings Complets
