
#                                  INTRODUCTION A  kivy.uix.accordion

"""
Le widget Accordion dans kivy est un conteneur qui organise ses enfants (widgets) sous forme de panneau déroulants. Chaq
ue panneau est représenté par un AccordionItem, qui peut être ouvert ou fermé pour afficher ou masquer son contenu.
ce widget est particulièrement utilisé pour organiser des interfaces où l'espace est limité comme les applications mobil
es, en permettant à l'utilisateur de naviguer entre plusieurs sections sans surcharger l'écran.

CARATERISTIQUE PRINCIPALES :
    °  Structure hiérachique : un Accordion contient plusieurs AccordionItem.
    ° Animation : les panneaux s'ouvrent et se ferment avec une animation fluide(configurable).
    ° Personnalisation : Les titres et le contenu des panneaux sont entièrement personnalisables.
    ° Evénéments : Possibilité de réagir à l'ouverture et à la fermeture des panneaux.

CLASSES PRINCIPALES :
    ° Accordion : Le conteneur principal qui gère les AccordiçonItem.
    ° AccordionItem : un panneau individuel avec un titre et un contenu

"""
"""
order de resolution des méthodes
    <= Accordion
        <= kivy.uix.widget.Widget
            <= kivy.uix.widget.WidgetBase
                <= kivy._event.EventDispatcher
                    <= kivy._event.ObjectWithUid
                        <= builtins.object
"""

#1. Classe Accordion
"""
La classe Accordion (situé dans kivy.uix.accordion) est un widget de type Widget qui organise ses enfants (AccordionItem)
 dans une disposition verticale ou horizontale.
 
Propriétés principales :
    ° orientation (str) : Définit l'orientation des panneaux. valeurs possibles : 
        ° 'vertical' par (défaut) : Les panneaux sont empilés verticalement.
        ° 'horizontal' : les panneaux sont empilés horizontalement
    ° anim_duration (float) : Durée de l'animation d'ouverture/fermeture des panneaux(en secondes, par défaut 0.25)
    ° min_space (float) : Taille minimale du titre de chaque AccordionItem lorsqu'il est fermé (en pixels, par défaut 44)
"""

    # Méthodes principales :
"""
° add_widget(widget, *args, **kwargs) : Ajoute un AccordionItem à l'accordéon. seuls les widgets de type AccordionItem
sont acceptés.
° remove_widget(widget, *args, **kwargs) : supprime un accordion AccordionItem de l'accordéon.
° clear_widgets(*args, **kwargs) : Supprime tous les AccordionItem de l'accordéon
"""
    # EVÉNEMENTS
"""
° on_touch_down(touch) : Déclenché lorsqu'un utilisateur touche l'accordéon.
° on_touch_move(touch) : Déclenché lors du déplacement du toucher.
° on_touch_up(touch) : Déclenché lorsque le toucher est relâché.
"""

# Classe AccordionItem
"""
la classe AccordionItem représente un panneau individuel dans l'accordéon. Elle contient un titre (affiché en permanence)
et un contenu (affiché lorsque le panneau est ouvert).

Propriétés principales :
° title (str) : Texte affiché dans l'en-tête du panneau.
° collapse (bool) : Indique si le panneau est ouvert (False) ou fermé (True, par défaut).
° min_space (float) : Taille minimale du titre (par défaut, hérite de Accordion.min_space).
° background_normal (str) : Chemin vers l'image de fond du titre lorsqu'il est fermé.
° background_selected (str) : chemin vers l'image de fond du titre lorsqu'il est ouvert.
° container (Widget): Widget conteneur pour le contenu du panneau (peut-être personnalisé).
"""

#           Méthodes principales :
"""
 ° add_widget(widget, *args, **kwargs) : ajoute un widget comme contenu du panneau. un seul widget est généralement ajou
 ter au container
 ° remove_widget(widget, *args, **kwargs) : Supprime un widget du contenu du panneau.
 ° on_touch_down(touch) : Déclenché quand on touche l'en-tête du panneau. Ouvre ou ferme le panneau si le toucher est va
 lide.
 ° on_collapse(value) : Evénément déclenché lorsque la propriété collapse change (panneau ouvert ou fermé).
"""


# EXEMPLE 1 : Création d'un Accordéon simple
#exemple de base pour créer un Accordion avec  Trois AccordionItem, chacun contenant un contenu différent.
"""
from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.button import Button

class AccordionApp(App):
    def build(self):
        # Créer l'accordéon
        accordion = Accordion(orientation="vertical", size_hint=(0.5, 0.5))

        # Premier panneau
        item1 = AccordionItem(title="Panneau 1")
        item1.add_widget(Label(text="Contenu du panneau 1"))
        accordion.add_widget(item1)

        # Deuxième panneau
        item2 = AccordionItem(title='Panneau 2', background_normal="../AI_Application_Icon.ico")
        item2.add_widget(Label(text='Contenu du panneau 2'))
        accordion.add_widget(item2)

        # Troisième panneau
        item3 = AccordionItem(title='Panneau 3')
        item3.add_widget(Label(text="Contenu du panneau 3"))
        accordion.add_widget(item3)

        return accordion

if __name__ == '__main__':
    AccordionApp().run()
"""


# exemple 2 : Personnalisation de l'accordéon
# cette expérience montre comment personnaliser l'apparence et gérer les événements de l'accordéon.

"""
from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty

class CustomAccordionItem(AccordionItem):
    is_open = BooleanProperty(False)# crèe une propriété

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(collapse=self.on_collapse_state)

    def on_collapse_state(self, instance, value):# gestionnaire de l'événement on_collapse
        self.is_open = not value # convertir is_open qui etait une variable de classe en variable d'instance et on inver
        # se la valeur de value avec not
        print(f"Panneau '{self.title}' est {'ouvert' if self.is_open else 'fermé'}")

class AccordionApp(App):
    def build(self):
        accordion = Accordion(orientation='vertical', anim_duration=0.5)# anim_duration ralentit l'animation  à 0.5
        # seconde pour un effet plus visible.

        # panneau 1 avec contenu personnalisé
        item1 = CustomAccordionItem(title="Paramètres")
        layout1 = BoxLayout(orientation='vertical')# s'utilisera comme conteneur pour organiser plusieurs widgets-
        # dans l'AccordionItem
        layout1.add_widget(Label(text='Option 1'))
        layout1.add_widget(Label(text='Option 2'))
        item1.add_widget(layout1)
        accordion.add_widget(item1)

        # Panneau 2
        item2 = CustomAccordionItem(title='Profile')
        item2.add_widget(Label(text='Informations Utilisateurs'))
        accordion.add_widget(item2)

        return accordion

if __name__ == '__main__':
    AccordionApp().run()
"""

# Exemple 3 : Accordéon Sorizontal avec Style
#  Cet exemple montre un accordéon horizontal avec une personnalisation du style des panneaux

from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.lang import Builder

# Définir le style avec kv
Builder.load_string('''
<AccordionItem>:
    background_normal: '../AI_Application_Icon.ico'
    background_selected: '../AI_Application_Icon.ico'
    min_space: '60'
''')
#Builder.load_file(filename="../exemple.kv")
class AccordionApp(App):
    def build(self):
        accordion = Accordion(orientation="horizontal", anim_duration=0.3)

        # Panneau 1
        item1 = AccordionItem(title='Section 1')
        item1.add_widget(Label(text='Contenu horizontal 1'))
        accordion.add_widget(item1)

        # Panneau 2
        item2 = AccordionItem(title='Section 2')
        item2.add_widget(Label(text="Contenu horizontal 2"))
        accordion.add_widget(item2)

        return accordion

if __name__ == '__main__':
    AccordionApp().run()


