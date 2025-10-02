"""
le module kivy.base est au coeur du fonctionnement de kivy car il fornit des outils pour initialiser, exécuter et gérer les é
vénements dans une application
"""

# Classes principales de kivy.base
"""
EventLoop           => Boucle d'événements principale, gère les entrées et les mises à jour.
EventDispatcher     => Classe de base pour la gestion des événements personnalisés.
runTouchApp         => Lance une application kivy sans utiliser la classe App.
stopTouchApp        => Arrête l'application kivy en cours d'exécution.
"""

# Classe EventLoop ||   kivy.base.EventLoop
"""
Propriétés principales:
    #- window: Référence à la fenêtre principale (kivy.core.window.Window).
    #- input_events: Liste des événements d'entrée en attente.

Méthodes principales:
    -   ensure_window() : S'assure qu'une fenêtre est disponible (crée une fenêtre si nécessaire)
    -   add_input_provider(provider) : Ajouter un fournisseur d'entrées.
    -   remove_input_provider(provider) : Supprime un fournisseur s'entrées.
    -   start() : Démarre la boucle d'événements.
    -   stop() : Arrête la boucle d'événements.
    -   post_dispatch_input(event, value) : envoie un événement d'entrée à la boucle 
Evénements:
    on_start, on_stop, on_pause, on_resume
"""
#from kivy.base import EventLoop, EventDispatcher
#help(EventLoop)

# classe EventDispatcher
# déjà vu dans le module kivy._event
#help(EventDispatcher)
"""
                    # EXEMPLE D'UTILISATION BASIQUE de runTouchApp
from kivy.uix.button import Button
from kivy.base import runTouchApp

# Créer un bouton
bouton = Button(text="Cliquez-moi", size_hint=(0.2, 0.2), pos_hint={"center_x": 0.5, "center_y": 0.5})

# Lancer l'application
runTouchApp(bouton)
"""
# Exemple 2 Gestion des événements avec EventLoop
#cette exemple montre comment intéragir avec EventLoop pour capturer les événements tactiles
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.base import EventLoop

class EventLoopApp(App):
    def build(self):
        self.label = Label(text="Touche ici")
        # Lier un gestionnaire d'événements tactiles
        EventLoop.window.bind(on_touch_down=self.on_touch)
        return self.label
    def on_touch(self, window, touch):
        self.label.text = f"Touche à : {touch.pos}"

if __name__ == '__main__':
    EventLoopApp().run()
"""

# Exemple 3 : Création d'un événement personnalisé avec EventDispatcher
# cette exemple montre commment créer et utiliser un événement personnalisé avec EventDispatcher

from kivy.app import App
from kivy.uix.button import Button
from kivy.base import EventDispatcher
from kivy.properties import StringProperty

class CustomDispatcher(EventDispatcher):
    custom_event = StringProperty("")

    def __init__(self, **kwargs):
        super(CustomDispatcher, self).__init__(**kwargs)
        self.register_event_type("on_custom")

    def trigger_event(self, value):
        self.custom_event = value
        self.dispatch("on_custom", value)

    def on_custom(self, value):
        print(f"Evénement reçu : {value}")
        pass # Evénement par défaut

class DispatcherApp(App):
    def build(self):
        dispatcher = CustomDispatcher()
        dispatcher.bind(on_custom=self.on_custom_event)

        button = Button(text="Déclencher evenement")
        button.bind(on_press=lambda x: dispatcher.trigger_event("Evénement déclenché !"))
        return button

    def on_custom_event(self, instance, value):
        print(f"Evénement reçu : {value}")
if __name__ == '__main__':
    DispatcherApp().run()

# exemple 4 : Gestion de la pause sur mobile avec EventLoop
#cette exemple montre comment gérer les événements on_pause et on_resume pour une application mobile.

from kivy.app import App
from kivy.uix.label import Label
from kivy.base import EventLoop

class MobileApp(App):
    def build(self):
        EventLoop.window.bind(on_pause=self.on_pause, on_resume=self.on_resume)
        return Label(text="Application Mobile")

    def on_pause(self, *args):
        print("Application en pause")
        return True # retourner True pour permettre la pause

    def on_resume(self, *args):
        print("Application reprise")


if __name__ == '__main__':
    MobileApp().run()
