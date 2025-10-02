from kivy.core.window import Window
from kivy.uix.codeinput import CodeInput


# 1, 2, 3 voir la descriptions dans grok apk et deepseek

# Projet Pratique : Editeur de code KV Intégré
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.extras.highlight import KivyLexer
from kivy.lang import Builder
from kivy.clock import Clock
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String
from pygments.style import Style

import os

class CustomStyle(Style):
    default_style = ""
    styles = {
        Keyword: "bold #ff0000", # Rouge pour keyword
        Name: '#00ff00',         # vert pour noms
        Comment: "italic #0000ff",# bleu italique pour commentaires
        String: "#ffff00"        # jaune pour strings
    }

class AdvancedCodeInput(CodeInput):
    def __init__(self, app_class,**kwargs):
        super().__init__(**kwargs)
        self.lexer = KivyLexer()    # Propriété lexer
        self.style = CustomStyle    # Propriété style custom
        self.app_class = app_class

    def insert_text(self, substring, from_undo=False):
        if substring == '\n' and self.text.endswith(':'):
            substring += '    ' # Auto-tabulation (override methode)
        return super().insert_text(substring, from_undo)

    def on_text(self, instance, value):
        # Debounce pour performances
        Clock.unschedule(self.update_preview)
        Clock.schedule_once(self.update_preview, 0.5)
        #super().on_text(instance, value)

    def update_preview(self, dt):
        try:
            # parse KV et update preview
            widget = Builder.load_string(self.text)
            self.app_class.clear_widgets()
            self.app_class.add_widget(widget)

        except Exception as e:
            print(f"Erreur de parse: {e}")  # L'Linting basique

class EditorLayout(BoxLayout):
    def __init__(self, preview, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.preview = preview  # pour la preview live
        self.add_widget(self.preview)

        self.code_input = AdvancedCodeInput(app_class=self.preview, text='# Editer votre code KV ici\nButton:\n     text: "Hello"')
        self.add_widget(self.code_input)

        btn_layout = BoxLayout(size_hint_y=0.1)
        save_btn = Button(text="Sauvegarder")
        save_btn.bind(on_press=self.save_file)
        load_btn = Button(text="Charger")
        load_btn.bind(on_press=self.load_file)
        btn_layout.add_widget(save_btn)
        btn_layout.add_widget(load_btn)
        self.add_widget(btn_layout)

    def save_file(self, btn):
        content = BoxLayout(orientation='vertical')
        filechooser = FileChooserListView()
        save_btn = Button(text="Sauvegarder ici")
        save_btn.bind(on_press=lambda x: self.do_save(filechooser.path, filechooser.selection))
        content.add_widget(filechooser)
        content.add_widget(save_btn)
        popup = Popup(title="Choisir dossir", content=content, size_hint=(0.9, 0.9))
        popup.open()

    def do_save(self, path, selection):
        print(path)
        if selection:
            filepath = os.path.join(path, selection[0])
        else:
            filepath = os.path.join(path, 'code.kv')
        with open(filepath, 'w') as f:
            f.write(self.code_input.text)

    def load_file(self, instance):
        content = BoxLayout(orientation='vertical')
        filechooser = FileChooserListView(filters="*.kv")
        load_btn = Button(text="Charger")
        load_btn.bind(on_press=lambda x: self.do_load(filechooser.path, filechooser.selection))
        content.add_widget(filechooser)
        content.add_widget(load_btn)
        popup = Popup(title="Choisir fichier", content=content, size_hint=(0.9, 0.9))
        popup.open()

    def do_load(self, path, selection):
        if selection:
            filepath = os.path.join(path, selection[0])
            print(selection, selection[0])

            with open(filepath, "r") as f:
                self.code_input.text = f.read()

class EditorApp(App):
    preview = BoxLayout() # Accès à preview
    def build(self):
        return EditorLayout(preview=self.preview)

if __name__ == '__main__':
    EditorApp().run()