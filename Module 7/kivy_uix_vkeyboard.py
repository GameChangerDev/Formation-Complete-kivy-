# voir la descriptions dans grok apk et deepseek
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.vkeyboard import VKeyboard
from kivy.core.window import Window

# 1 . introduction
# Exemple basique
from kivy.app import App
'''
class MyApp(App):
    def build(self):
        self.kb = VKeyboard()
        self.kb.width = Window.width
        self.kb.height = Window.height/3
        return self.kb

MyApp().run()
'''
# 2. Propriétés avancées
# la documentation du Vkeyboard dans le code source

# 3. Methodes avancées
# la documentation du Vkeyboard dans le code source

class Custom(VKeyboard):
    def on_key_down(self, *largs):
        print(f'touche pressée: {largs[0]}')
        print(largs)
        super().on_key_down(*largs)


# 4. Evénements
class MyApp(App):
    def build(self):
        #self.kb = Custom()
        self.kb = VKeyboard()
        self.kb.bind(on_key_down=self.pression)
        return self.kb
    def pression(self, *largs):
        print(f'touche pressée: {largs[0]}')
        print(largs)

#MyApp().run()

# 5. Personnalisation avancée
# exemple de variation de style de clavier après un triple tap
class CustomVkeyboard(VKeyboard):
    def on_touch_down(self, touch):
        if touch.is_double_tap or touch.button == "right":
            self.layout = "azerty" if self.layout == "qwerty" else "qwerty"
            Window.maximize()
            self.size = (Window.width, Window.height / 3)
        elif touch.button == 'scrollup':
            Window.maximize()
            self.size = (Window.width, Window.height / 3)
        elif touch.button == "scrolldown":
            Window.minimize()
            self.size = (Window.width, Window.height / 3)
        return super().on_touch_down(touch)

class CustomApp(App):
    def build(self):
        self.kb = CustomVkeyboard()
        return self.kb
#CustomApp().run()

# 6. intégration et meilleures pratiques
# intégration avec TextInput
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', spacing=50)
        self.texte = TextInput(hint_text="Entrez quelques choses", multiline=False)
        self.clavier = VKeyboard(callback=self.react_key, target=self.texte)
        self.clavier.bind(on_key_down=self.react_key)
        self.clavier.width = Window.width

        self.texte.bind(on_double_tap=lambda inst, *args: self.add_keyboard())
        self.texte.bind(cursor=self.on_cursor)
        self.root.add_widget(self.texte)
        return self.root

    def add_keyboard(self, *args):
        #self.clavier.bind(on_key_down=self.react_key)
        try:
            self.root.add_widget(self.clavier)
        except:
            pass


    def react_key(self,inst, key, *args):
        print(key, args)
        if key == "backspace":
            #self.texte.text = self.texte.text[:self.texte.cursor_col-1]
            # liste  = list(self.texte.text)
            # if liste:
            #     del liste[self.texte.cursor_col-1]
            # text = "".join(liste)
            self.texte.do_backspace()
        print(self.clavier.target)

    def on_cursor(self, inst, cursor):
        print(cursor, self.texte.cursor_col)

MyApp().run()


# Projet Pratique : Clavier sécurisé





#                       Fin de parcours de tous les widgets du module uix de la version 2.3.1