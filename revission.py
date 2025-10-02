#from kivy.uix.button import Button
#from kivy.event import EventDispatcher
#from kivy.app import App
#from functools import wraps
"""
class MonWidget(EventDispatcher):
    def __init__(self, **kwargs):
        super(MonWidget, self).__init__(**kwargs)

    def __setattr__(self, name, value):
        if name and type(name) != [int, list, tuple,set]:
            self.register_event_type("on_"+name)
            eventement = {"on_"+name:value}
            self.bind(**eventement)

    def on_event1(self, *args):
        pass

    def on_event2(self, *args):
        pass

    def on_event3(self, *args):
        pass
"""


"""
class Eventype:
    def __init__(self, **kwargs):
        pass
    def deco(func):
        @wraps(func)
        def wrapper(self, *args):
            return func.__name__
        return wrapper

    @deco
    def on_event1(self, *args):
        pass
    @deco
    def on_event2(self, *args):
        pass
    @deco
    def on_event3(self, *args):
        pass

eventype = Eventype()
"""
"""
def drappel(func):
    @wraps(func)
    def wrapper(*args):
        print(f"{func.__name__} exécuté avec succès.")
    return wrapper


@drappel
def rappel_event(*args):
    pass

btn1 = MonWidget()
btn1.event3 = rappel_event

btn2 = MonWidget()
btn2.event2 = rappel_event

class MonApp(App):
    def build(self):
        def frappel(bouton:EventDispatcher, event, *args):
            return bouton.dispatch(event)
        bouton1 = Button(text="Déclenchez l'event1")
        bouton1.fbind("on_press", frappel, btn1, "on_event3")

        print(bouton1.is_event_type("on_event3"))

        bouton1 = Button(text="Déclenchez l'event1")
        bouton1.fbind("on_press", frappel, btn2, "on_event2")


        bouton2 = Button(text="Déclenchez l'event1")
        bouton3 = Button(text="Déclenchez l'event1")

        return bouton1

if __name__ == '__main__':
    MonApp().run()
"""
"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.settings import Settings
import json

class RevisionApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Enregistrement des données initiales du fichier de configuration qui seront utilisé comme anciennes valeurs
        # si cette valeur est modifiée
        self.configuration = self.load_config()
        self.an_v_nom = self.configuration.get("User", "nom")
        self.an_v_appr = self.configuration.get("User", "apprentissage")
        self.an_v_niveau = self.configuration.get("User", "niveau")
        self.an_v_exp = self.configuration.get("User", "experience")
        self.an_v_age = self.configuration.get("User", "age")
        self.language = self.configuration.get("Langages/Framework", "langage")
        self.fw_apk = self.configuration.get("Langages/Framework", "fw_apk")
        self.fw_website = self.configuration.get("Langages/Framework", "fw_website")
        self.travail = self.configuration.get("Travail", "occupe")
        self.an_v = {"nom": self.an_v_nom, "apprentissage": self.an_v_appr, "age": self.an_v_age,
                     "niveau": self.an_v_niveau, "experience": self.an_v_exp, "langage": self.language,
                     "fw_apk": self.fw_apk, "fw_website": self.fw_website, "occupe": self.travail}
        
    def save_js(self):
        # enregistrer les anciennes valeurs dans un fichier json
        with open(self.get_application_name()+".json", "w") as f:
            json.dump(self.an_v, f, indent=2)


    # construction de l'interface utilisateur
    def build(self):
        lay = FloatLayout()
        btn_param = Button(text="Paramètres", size_hint=(0.2, 0.1), pos=(100, 100))
        btn_param.bind(on_press=self.open_settings)

        btn_exit = Button(text="Arrêter", size_hint=(0.2, 0.1), pos=(100, 200))
        btn_exit.bind(on_press=self.stop)

        lay.add_widget(btn_param)
        lay.add_widget(btn_exit)
        return lay

    def get_application_name(self):
        return "Illustrator"

    def get_application_icon(self):
        return "AI_Application_Icon.ico"

    # personnalisation du fichier de configuration et intégration dans les paramètres de l'app
    def build_config(self, config):
        config.setdefaults("User", {"nom": "", "apprentissage": "", "niveau": "", "experience": "", "age": 10})
        config.setdefaults("Langages/Framework", {"langage":"", "fw_apk": "", "fw_website": ""})

    def build_settings(self, settings):
        settings.add_json_panel("Utilisateur", self.config, filename="revision.json")
        settings.add_json_panel("Langage de programation et frameworks".title(), self.config, filename="revision2.json")
        settings.add_json_panel("Travail", self.config, filename="revision3.json")

    # vérifie le fichier de configuration et retourne les anciennes valeurs des clés
    def an_config_parser(self, cle):
        return self.an_v[cle]

    # gestion de quelques événements de l'application
    def on_start(self):
        print(f"Démarrage de {self.get_application_name()}")
        print(f"{self.config.get('User', 'nom')} lancement réussit !" if self.config.get("User", "nom") is not None else "")

    def on_stop(self):
        print(f"application fermée".title())

    def on_config_change(self, config, section, key, value):
        print(f"\nconfiguration : \n", f"ancienne : [section= {section}, clé={key}, valeur={self.an_config_parser(key)}]")
        print(f"nouvelle : [section= {section}, clé={key}, valeur={value}]")

    # ouverture des paramètres
    def open_settings(self, *largs):
        self.save_js()
        print("anciens données de Settings enrégistrées !!")
        super().open_settings(*largs)

    # gestion de la fermeture du panneau de paramètre
    def close_settings(self, *largs):
        print("Paramètres fermés")
        super(RevisionApp, self).close_settings(*largs)

# lancement de l'app
if __name__ == '__main__':
    RevisionApp().run()
"""

# premier exemple
"""
from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label

class MonApp(App):
    def build(self):
        accordion = Accordion(orientation="vertical", min_space=60, anim_duration=1.5)

        contenu1 = Label(text="Contenu 1")
        item1 = AccordionItem(title="Panneau 1")
        item1.add_widget(contenu1)
        accordion.add_widget(item1)


        contenu2 = Label(text='contenu 2')
        item2 = AccordionItem(title='Panneau 2')
        item2.add_widget(contenu2)
        accordion.add_widget(item2)

        return accordion
"""

# exemple 2
"""
from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty

class CustomAccordion(AccordionItem):
    is_open = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(collapse=self.event_perso)

    def event_perso(self, instance, valeur):
        self.is_open = not valeur
        print(f"{self.title} est {'ouvert' if self.is_open else 'fermé'}")

class MonApp(App):
    def build(self):
        accor = Accordion(orientation='vertical', anim_duration=1, min_space=70)

        conteneur = BoxLayout(orientation='vertical')
        conteneur.add_widget(Label(text='contenu 1'))
        conteneur.add_widget(Label(text='contenu 2'))
        item1 = CustomAccordion(title='Panneau 1')
        item1.add_widget(conteneur)
        accor.add_widget(item1)

        contenu = Label(text='contenu 1')
        item2 = CustomAccordion(title='Panneau 2')
        item2.add_widget(contenu)
        accor.add_widget(item2)

        return accor

if __name__ == '__main__':
    MonApp().run()
"""

# exemple 3
"""
from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.lang import Builder

kv_string='''
<AccordionItem>:
    min_space: 100
    background_normal: "AI_Application_Icon.ico"
    background_selected: "ps_icon.png"
'''

class MonApp(App):
    def build(self):
        Builder.load_string(kv_string)
        accor = Accordion(orientation='vertical')

        item1 = AccordionItem(title='Panneau 1')
        item1.add_widget(Label(text='contenu 1'))
        item1.add_widget(Label(text='contenu 2'))
        accor.add_widget(item1)

        item2 = AccordionItem(title='Panneau 2')
        item2.add_widget(Label(text='Contenu 2'))
        accor.add_widget(item2)

        return accor

if __name__ == '__main__':
    MonApp().run()
"""


                                            # kivy.uix.actrionBar

# EXEMPLE 1: BARRE D'ACTION DE BASE
#from kivy.app import App
#from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious, ActionButton, ActionGroup, ActionOverflow
"""
class MonApp(App):

    def build(self):
        action_bar = ActionBar()
        action_view = ActionView()

        # Ajouter le titre
        action_previous = ActionPrevious(title="Mon App")
        action_view.add_widget(action_previous)

        # Ajouter les boutons
        action_view.add_widget(ActionButton(text="bouton 1", icon="ps_icon.png"))
        action_view.add_widget(ActionButton(text="bouton 1", icon="AI_Application_Icon.ico"))

        # Ajouter les un Groupe d'action
        groupe = ActionGroup(text="Groupe")
        groupe.add_widget(ActionButton(text="Groupe 1"))
        groupe.add_widget(ActionButton(text="Groupe 2"))
        action_view.add_widget(groupe)


        # débordements
        overflow = ActionOverflow()
        action_view.add_widget(overflow)

        action_bar.add_widget(action_view)

        return action_bar
if __name__ == '__main__':
    MonApp().run()
"""
"""
from kivy.uix.label import Label as la
from kivy.uix.boxlayout import BoxLayout as bol
# CETTE EXEMPLE CRÉE UNE BARRE D'ACTIONS AVEC UN TITRE, DEUX BOUTONS, UN GROUPE UN MENU DE DÉBORDEMENT

class MonApp(App):
    def build(self):
        boxlaout = bol(orientation="vertical")

        action_bar = ActionBar()
        action_view = ActionView()

        # Ajouter le titre
        action_prev = ActionPrevious(title="Mon App")
        action_view.add_widget(action_prev)

        def affiche_msg(instance):
            print(f"{instance.text} préssé")

        # Ajouter les boutons
        action_view.add_widget(ActionButton(text="Bouton 1", icon="ps_icon.png", on_press=lambda x: affiche_msg(x)))
        action_view.add_widget(ActionButton(text="Bouton 1", icon="AI_Application_Icon.ico", on_press=lambda x: affiche_msg(x)))


        # Ajouter groupe
        groupe = ActionGroup(text='Groupe')
        groupe.add_widget(ActionButton(text='Groupe 1', icon="ps_icon.png", on_press=lambda x: affiche_msg(x)))
        groupe.add_widget(ActionButton(text="Groupe 2", icon="AI_Application_Icon.ico", on_press=lambda x: affiche_msg(x)))
        action_view.add_widget(groupe)


        # Ajouter le débordement
        overflow = ActionOverflow()
        action_view.add_widget(overflow)

        action_bar.add_widget(action_view)


        # grouper les contenu
        contenu = la(text="Contenu Principale")
        boxlaout.add_widget(action_bar)
        boxlaout.add_widget(contenu)

        return boxlaout

if __name__ == '__main__':
    MonApp().run()
"""
# ici nous ajoutons des actions aux boutons pour afficher des messages, et intégrons un contenu principal sous la bouton_play.
"""
# exemple 3 : Utilisation du langage kv
from kivy.app import App
#from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious, ActionButton, ActionGroup, ActionOverflow
from kivy.lang import Builder

class MonApp(App):
    def build(self):
        return Builder.load_file(filename="revision.kv")

if __name__ == '__main__':
    MonApp().run()
"""

# voici un exemple simple qui place un bouton au centre d'un AnchorLayout.
"""
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class AnchorApp(App):
    def build(self):

        layout= AnchorLayout(anchor_x='center', anchor_y='center', padding=[10, 20, 10, 10])

        def msg(instance):
            print(f"{instance.text} préssé")
        layout.add_widget(Button(text='centré', size_hint=(0.2, 0.2), on_press=msg))

        return layout

if __name__ == '__main__':
    AnchorApp().run()
"""
# Exemple 2 : Ancrage multiple avec padding
# Cet exemple montre comment utiliser différents points d'ancrage et un padding.
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class AnchorApp(App):
    def build(self):

        layout_principal = BoxLayout(orientation='vertical')
        def msg(instance):
            print(f"{instance.text} préssé")

        layout1 = AnchorLayout(anchor_x='left', anchor_y='top', padding=[10, 20, 10, 20])
        layout1.add_widget(Button(text='Haut à gauche', size_hint=(0.2, 0.1), on_press=msg))
        layout_principal.add_widget(layout1)

        layout2= AnchorLayout(anchor_x='right', anchor_y='bottom', padding=[10, 20, 10, 20])
        layout2.add_widget(Button(text='Bas à droite', size_hint=(0.2, 0.1), on_press=msg))
        layout_principal.add_widget(layout2)

        return layout_principal

if __name__ == '__main__':
    AnchorApp().run()
"""
# EXMEPLE 3 : AnchorLayout  AVEC KV ET PERSONNALISATION

"""
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.lang import Builder
"""
kv_string = '''
<CustomAnchor>:
    anchor_x: 'center'
    anchor_y: 'center'
    padding: [10, 20, 10, 20]
    canvas.before:
        Color: 
            rgba: 0.2, 0.6,0.8, 0.8
        Rectangle:
            pos: self.pos
            size: self.size
    Button:
        text: 'Cliquez ici'
        size_hint: 0.3, 0.3
        
        on_press: app.msg()
'''
"""
Builder.load_string(kv_string)

class CustomAnchor(AnchorLayout):
    pass

class AnchorLayoutApp(App):
    def build(self):
        return CustomAnchor()

    def msg(self):
        print("salut")

if __name__ == '__main__':
    AnchorLayoutApp().run()
"""


from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App


class BoxApp(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxApp, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # afficher les parametres
        self.width_label = Label(text=f"Width : {Config.get('graphics', 'width')}")
        self.height_label = Label(text=f"height : {Config.get('graphics', 'height')}")
        self.fullscreen_label = Label(text=f"Plein Ecran : {"Oui" if Config.getint('graphics', 'fullscreen') == 1 else "Non"}")

        # recupère les entrées de l'utilisateur
        self.width_input = TextInput(text=Config.get('graphics', 'width'))
        self.height_input = TextInput(text=Config.get('graphics', 'height'))
        self.fullscreen_input = TextInput(text=Config.get('graphics', 'fullscreen'))

        # bouton pour appliquer le changement
        self.apply_button = Button(text="Appliquer", on_press=self.apply_change)

        # Ajouter les widget à l'Ecran/ layout
        self.add_widget(self.width_label)
        self.add_widget(self.width_input)
        self.add_widget(self.height_label)
        self.add_widget(self.height_input)
        self.add_widget(self.fullscreen_label)
        self.add_widget(self.fullscreen_input)
        self.add_widget(self.apply_button)

    def apply_change(self, instance):

        # Modifier les valeurs
        Config.set('graphics', 'width', self.width_input.text)
        Config.set('graphics', 'height', self.height_input.text)
        Config.set('graphics', 'fullscreen', self.fullscreen_input.text)

        # Redimensionner la fenêtre
        from kivy.core.window import Window
        Window.size = (int(self.width_input.text), int(self.height_input.text))


class MyApp(App):
    def build(self):
        return BoxApp()
    def on_stop(self):
        Config.write()
        print("fichier de configuration config.ini sauvegardé !!!")

if __name__ == '__main__':
    MyApp().run()
