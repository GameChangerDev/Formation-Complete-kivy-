                            # introductiopn à kivy.uix.anchorlayout
"""
AnchorLayout est un widget de disposition qui permet de positionner ses enfants (widgets) par rapport à un point d'ancrage
défini dans sa zone. Contrairement à d'autres layouts comme Boxlayout ou Gridlayout, il ne dimensionne pas automatiqueme
nt les widgets pour remplir l'espace, mais les placces à un endroit précis (par exemple, en haut à gauche ou au centre).
Cela le rend idéale pour les interfaces ou vous souhaitez un contrôle précis sur le positionnement comme dans des applic
ations mobiles avec des éléments fixes.

    Caractéristiques principales:
     ° Positionnement flexible : Placez les widgets à des points d'ancrages spécifiques (haut, bas, gauche, droite,centre)
     ° Tailles des widgets : les widgets enfants conservent leur taille définie(via size ou size_hint).
     ° Simplicité : utile pour des interfaces minimalistes fixes comme des boutons ou des labels.
"""

        # ORDE DE RÉSOLUTION DES MÉTHODES
#=>AnchorLayout
#=>     kivy.uix.layout.Layout
#=>         kivy.uix.widget.Widget
#=>             kivy.uix.widget.WidgetBase
#=>                 kivy._event.EventDispatcher
#=>                     kivy._event.ObjectWithUid
#=>                         builtins.object

from kivy.uix.anchorlayout import AnchorLayout

                                            # Classe AnchorLayout
"""
La classe AnchorLayout (située dans kivy.uix.anchorlayout) herite de Widget et est le coeur du module. Elle gère le posi
tionnement des widgets enfants en fonction de deux propriétés principales: anchor_x et anchor_y.

Propriétés principales:
    °anchor_x (str): Définit l'ancrage horizontal des widgets enfants. Valeurs possibles:
        ° 'left' : Ancre à gauche.
        ° 'center': Ancre au centre Horiszontalement.
        ° 'right' : Ancre à droite. 
    ° anchor_y (str): Définit l'ancrage vertical des widgets enfants. Valeurs possible:
        ° 'top': ancre en haut
        ° 'center' : ancre au centre verticalement.
        ° 'bottom' : Ancre en bas.
    ° padding (list ou float): Espacement interne entre les bords du layout et le widget enfant , peut être spécifier co
    mme :
        ° un float (ex: 10) pour un padding uniforme.
        ° une liste [left, top, right, bottom] pour des valeurs spécifiques (ex : [10, 20, 10, 20]).
    ° size_hint et size : Contrôle la taille du layout lui-même, comme pour tout widget kivy. par défaut, size_hint=(1, 1)
    fait en sorte que l'AnchorLayout occupe tout l'espace de son parent.
"""
# Méthodes principales :
"""
- add_widget(widget, *args, **kwargs): Ajoute un widget enfant à l'AnchorLayout. Le widget est positionné selon les propri
étés anchor_x et anchor_y.
- remove_widget(widget, *args, **kwargs) : Supprime un widget enfant .
- clear_Widgets(*args, **kwargs): Supprime tous les widgets enfants.
"""
# Evenements :
# même événement que kivy.uix.accordion
# on_touch_down(touch), on_touch_move(touch), on_touch_up(touch)

                        # EXEMPLE 1 : AnchorLayout DE BASE
# voici un exemple simple qui place un bouton au centre d'un AnchorLayout.
"""
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class AnchorLayoutApp(App):
    def build(self):
        # Créer un AnchorLayout avec un ancrage au centre
        layout = AnchorLayout(anchor_x="center", anchor_y = "center")

        # Ajouter un bouton
        button = Button(text="centré", size_hint=(0.2, 0.1))
        layout.add_widget(button)
        return layout

if __name__ == '__main__':
    AnchorLayoutApp().run()
"""

# Exemple 2 : Ancrage multiple avec padding
# Cet exemple montre comment utiliser différents points d'ancrage et un padding.
'''
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class AnchorLayoytApp(App):
    def build(self):
        # Layout principal (Boxlayout pour organiser plusieurs AnchorLayout)
        main_layout = BoxLayout(orientation='vertical')

        # AnchorLayout 1 : ancrage en haut à gauche
        layout1 = AnchorLayout(anchor_x='left', anchor_y='top', padding=[20, 20, 20, 20])
        layout1.add_widget(Button(text='Haut Gauche', size_hint=(0.3, 0.3)))
        main_layout.add_widget(layout1)

        # AnchorLayout 2 : Ancrage en bas à droite
        layout2 = AnchorLayout(anchor_x='right', anchor_y='bottom', size_hint=(0.3, 0.3), padding=[10, 10, 10, 10])
        layout2.add_widget(Button(text='Bas Droite', size_hint=(0.3, 0.3)))
        main_layout.add_widget(layout2)

        return main_layout
if __name__ == '__main__':
    AnchorLayoutApp().run()
'''

                        # EXMEPLE 3 : AnchorLayout  AVEC KV ET PERSONNALISATION
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.lang import Builder

# définir l'interface avec kv
Builder.load_string('''
<CustomAnchorLayout>:
    anchor_x: 'center'
    anchor_y: 'center'
    padding: [20, 20, 20, 20]
    canvas.before:
        Color:
            rgba: 0.2, 0.6, 0.8, 1 # fond bleu clair
        Rectangle:
            pos: self.pos
            size: self.size
    Button:
        text: 'Cliquez-moi'
        size_hint: 0.3, 0.3
        on_press: app.on_button_press()  
              
''')
class CustomAnchorLayout(AnchorLayout):
    pass

class AnchorLayoutApp(App):
    def build(self):
        return CustomAnchorLayout()

    def on_button_press(self):
        print("Bouton Cliqué")

if __name__ == '__main__':
    help(AnchorLayout)
    AnchorLayoutApp().run()