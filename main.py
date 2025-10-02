from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from functools import partial
from kivy.app import App
from kivy.animation import Animation


#partie sur le module kivy.event
import kivy
from kivy.event import EventDispatcher
#methode de _event(Builtins.object => ObjectWithUid => EventDispatcher => Observable)
#toutes les methodes s'appliques sur la classe EventDispatcher
# bind(), create_property(), dispatch()| dispatch_children()|dispatch_generic()
# events(), fbind(),funbind(), unbind(), unbind_uid(), get_properties_observers(), setter(), getter()
# properties(), property(),
"""
class DemoBox(BoxLayout):
    def __init__(self, **kwargs):
        super(DemoBox, self).__init__(**kwargs)
        self.orientation = "vertical"

        # we start with binding to the normal event
        # passed to the callback is the object which we have bound to.
        btn = Button(text="Normal binding to event")
        btn.bind(on_press=self.on_event)

        # Next, we bind to a standard property change event. This typically
        # passes 2 arguments: the object and the value
        btn2 = Button(text="Normal binding to a proprety change")
        btn2.bind(state=self.on_property)

        # Here we use anonymous functions (a.k.a lambdas) to perform binding.
        # Their advantage is that you can avoid declaring new functions i.e.
        # they offer a concise way to "redirect" callbacks.
        btn3 = Button(text="Using anonymous fonctions.")
        btn3.bind(on_press=lambda x: self.on_event(None))

        # that accepts optional positional and keyword arguments.
        btn4=Button(text="Use a fexible fonction")
        btn4.bind(on_press=self.on_anything)

        # Lastly, we show how to use partial functions. They are sometimes
        # difficult to grasp, but provide a very flexible and powerful way to
        # reuse functions.
        btn5 = Button(text="Using partial functions. For hardcores.")
        btn5.bind(on_press=partial(self.on_anything, "1", "2", monthy="puthon"))

        #bonjour franklin
        btn6 = Button(text="salut moi et j'affiche dans le Run")
        btn6.bind(on_press=self.salut)

        for but in [btn, btn2, btn3, btn4, btn5,btn6]:
            self.add_widget(but)

    def on_event(self, obj):
        print("Typical event from", obj)

    def on_property(self, obj, value):
        print("Typical property change from", obj, "to", value)

    def on_anything(self, *args, **kwargs):
        print("The fexible function has *arg of ", str(args), "and **kwargs of ", str(kwargs))

    def salut(self, obj):
        print("bonjour mon developpeur franklin !!!".title())



class DemoApp(App):
    def build(self):
        return DemoBox()
if __name__ == '__main__':
    DemoApp().run()
"""


                                            # FORMATION kivy
                                # Phase 1: Fondation Essentielles
#1. kivy.core
"""
        ° comprende l'architecture modulaire (core.window, core.text, core.image)
        ° Prérequis pour le modules avancés
"""

#2. kivy.base
"""
    ° Gestion de la boucle d'événement
"""

# 3. kivy.clock
"""
    le module kivy.clock repose sur la classe ClockBase et plusieurs fonctions utilitaires pour planifier des tâches.
"""

#4. kivy.properties
"""
    ° Gérer les donnnées dynamiquement
    ° lier les widgets 
    ° valider les données
    ° optimiser les perfomances
voir les description sur twitter-grok
"""

#5. kivy.config
#   ° Personnaliser directement le fichier config.ini, gère les paramètres système(resolution, inputs, logs)
#   ° Doit être appelé avant toute autre importation kivy

# cas pratiques

                    #  Phase 2: UI & Layouts

#6. kivy.uix.layout
#   ° Approfondir les layouts:
#       ° Boxlayout (vertical/ horizontal) : from kivy.uix.boxlayout import BoxLayout
#       ° GridLayout (rows/ cols) : from kivy.uix.gridlayout import GridLayout
#       ° FloatLayout (Posisitionnement libre) : from kivy.uix.floatlayout import FloatLayout
#       ° RelativeLayout (coordonnées relative) : from kivy.uix.relativelayout import RelativeLayout
#       ° PageLayout (swipe entre les pages) :  from kivy.uix.pagelayout import PageLayout
#       ° ScatterLayout :   from kivy.uix.scatterlayout import ScatterLayout
#       ° StackLayout   :   from kivy.uix.stacklayout import StackLayout

#7. kivy.uix.scrollview
#   ° Afficher le contenu dépassant la zone Gérer le défilement du contenu long

#8. kivy.uix.screenmanager
#   ° propriété haute ! Navigation entre ecrans
#   ° créer les application multi-interface


#                   PHASE/ MODULE 3 : Widgets Intéractifs

#9. kivy.uix.button & kivy.uix.togglebutton
#   °button:  Widget cliquable déclenchant une action
#   °togglebutton:  bouton avec l'état "activé/Désactivé" persistant comme un interrupteur

#   ° Gestion des cliques(on_press)

#10. kivy.uix.slider & kivy.uix.progressbar
#   ° Barre intéractive(Slider) et feedback visuel(ProgressBar)

# 11. kivy.uix.textinput
#      ° saisie et validation de texte

# 12. kivy_uix_checkbox & kivy_uix_switch
#   1. Checkbox : Widget classique avec  une case à cocher.
#   2. Switch : Widget interactif de type interrupteur (glissant).
#   les deux servent à représenter des états binaires (actif/ inactif)

# 13. kivy_uix_dropdown & kivy_uix_spinner
#   ° Dropdown : menus personnnalisés.
#   ° Spinner : version simplifiée

#       AUTRES :
#   kivy.uix.filechooser
#       ° Explorateur de fichier

#   kivy.uix.scatter    et  kivy.uix.popup
#       ° le Scatter rend maléable le widget (possibilité de roter, translater, pincer-déplacer)
#       ° Popup : afficher ou manipuler les données hors de l'interface utilisateur principale

#   kivy.uix.splitter   et  kivy.uix.treeview
#       ° Splitter : Créer un interface redimensionnable à l'aide d'un séparateur
#       ° Treeview : Créer une affichage en arborescence

#   kivy.uix.rst    et  kivy.uix.sandbox et kivy.uix.settings
#       ° Utile pour intégrer du contenu documentaire riche dans les applications comme : des manuels, tutoriels, ou aide
#         en lignes
#

#           kivy.uix.videoplayer  &  kivy.uix.camera  &  kivy.uix.tabbedpanel  &  kivy.uix.modalview
#           VideoPlayer : Lecteur video avec options de manipulation de vidéo dejà prêt à l'emploi
#           Camera : Acceder à la camera utilisateur pour recupérer des photos
#           TabbedPanel : panel avec onglets
#           ModalView : Créer les vues modulaires(Popup, et autres)

                        # PHASE 4 : Graphismes Avancés & Performance

# 14. kivy.graphics
#   ° Noyou graphique:
#       ° Canvas, Rectangle, Ellipse, Line
#       ° Rotate, Scale, Translate
#   ° Optimisation via Fbo(Frame Buffer Object)

# 15. kivy.effects
#   ° Effets visuels(
#       - animations de défilement
#       - réponses tactiles
#       - transformation visuelles
#       - Optimisés pour les performances
#   )

# 16. kivy.metrics
#   ° Gérer les unités pour le responsive


                        # PHASE 5 : Multimédia & UI Avancée

# 17. kivy.uix.video & kivy.core.video
#   ° Intégration vidéo

# 18. kivy.uix.carousel
#   ° Galerie d'image

# 19. kivy.uix.recycleview
#   ° Critique sur les données dynamiques(Listes/grilles optimisées)

# 20. kivy.uix.stencilview
#   ° Clipping Graphique(masque)

                        # Phase  6 : Outils Spécialisés
# 21.   kivy.lang
#   ° Maîtriser l'UI/logique

# 22. kivy.factory
#   ° Enregistrer des composants personnalisés

# 23. kivy.storage
#   ° Stockage local

# 24. kivy.network
#   ° Requêtte http


                        # Phase 7 : Modules Spécifique

# 25. kivy.uix.codeinput
#   ° Editeur de code (syntaxe highlighting)

# 26. kivy.uix.colorpicker
#   ° SSelecteur de couleurs

# 27. kivy.uix.bubble
#   ° Tooltips contextuels

# 28. kivy.uix.vkeyboard
#   ° Clavier virtuel personnalisé

# 29. kivy.gesture                      & kivy.uix.gesturesurface
#   ° Reconnaissance de gestes