from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.settings import Settings, SettingItem, SettingOptions, SettingsWithTabbedPanel
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.config import ConfigParser
from kivy.properties import ListProperty, NumericProperty, BooleanProperty, StringProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
import json
import os

# Créer un configparser avec notre fichier
conf = ConfigParser(name='conf')
conf.read(filename="app_config.ini")

s = SettingsWithTabbedPanel()

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

class TodoApp(App):
    tasks = ListProperty([])
    font_size = NumericProperty(15)
    dark_mode = BooleanProperty(False)
    bg_color = ListProperty([1, 1, 1, 1])
    welcome_msg = StringProperty("Bienvenue !")

    def build(self):
        self.settings_cls = SettingsWithTabbedPanel # paramètres avec bouton de menu succéssif au dessus
        self.use_kivy_settings = True   # Pas de panel kivy

        layout = BoxLayout(orientation="vertical")
        self.welcome_label = Label(text=self.welcome_msg, font_size=self.font_size)
        layout.add_widget(self.welcome_label)

        input_box = TextInput(hint_text="Nouvelle Tâche")
        self.add_btn = Button(text="Ajouter")
        self.add_btn.bind(on_press=lambda x: self.add_task(input_box.text))
        self.add_btn.bind(on_press=self.open_settings)
        layout.add_widget(input_box)
        layout.add_widget(self.add_btn)

        self.task_list = GridLayout(cols=1, size_hint_y=None)
        scroll = ScrollView()
        scroll.add_widget(self.task_list)
        layout.add_widget(scroll)
        self.layout = layout

        return layout

    def build_config(self, config):
        conf.setdefaults("ui", {'dark_mode': 0, "font_size":15, 'theme':"Clair", 'welcome_msg': "bienvenue !", "bg_color": "red"})
        conf.setdefaults("files", {'task_dir': os.path.expanduser('-')})
        conf.setdefaults('tasks', {'priorities': "Moyenne"})

    def build_settings(self, settings):
        #settings.register_type(tp="scroll_option", cls=SettingScrollableOptions) # pour les settings céer hormis celui de l'app
        with open("settings.json", "r") as f:
            json_data = f.read()
        settings.add_json_panel("Todo Settings", conf, data=json_data)
        settings.bind(on_close=self.on_settings_close)

    def on_config_change(self, config, section, key, value):
        if section == "ui":
            if key == "dark_mode":
                self.dark_mode = bool(int(value))
                Window.bg_color = [0, 0, 0, 1] if self.dark_mode else [1, 1, 1, 1]
            elif key == "font_size":
                self.font_size = float(value)
                self.welcome_label.font_size = self.font_size
            elif key == "welcome_msg":
                self.welcome_msg = value
                self.welcome_label.text = self.welcome_msg
            elif key == "bg_color":
                from kivy.utils import rgba, platform
                self.bg_color = rgba(value)
                print(self.bg_color, platform)
                def color(dt):
                    self.add_btn.background_color = self.bg_color
                Clock.schedule_once(color, 0)
            elif key =="theme":
                print(f"thème : {value}")

    def on_settings_close(self, *args):
        print("Settings fermés")

    def add_task(self, text):
        if text:
            btn = Button(text=text, font_size=self.font_size)
            self.task_list.add_widget(btn)
            self.tasks.append(text)

if __name__ == '__main__':
    TodoApp().run()