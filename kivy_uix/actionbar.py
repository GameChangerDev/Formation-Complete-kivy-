from kivy.uix.actionbar import ActionBar


#introduction:
# ce module est concu pour créer des barres d'actions, un composant éssentiel dans les application mobile et desktop.

                                # ORDRE DE RÉSOLUTION DES MÉTHODES
# =>ActionBar
#       => kivy.uix.boxlayout.BoxLayout
#           => kivy.uix.layout.Layout
#               => kivy.uix.widget.Widget
#                   => kivy.uix.widget.WidgetBase
#                       => kivy._event.EventDispatcher
#                           => kivy._event.ObjectWithUid
#                               => builtins.objet

    # STRUCTURE ET CLASSES PRINCIPALES

# classe                                Description                         Rôle principal

# ActionBar   =>        Conteneur principale, gère le style principal =>      détermine l'apparence globale et gère les
#                        et contient ActionView.                               événements

# ActionView  =>        conteneur pour les éléments d'actions, doit     =>     Affiche les boutons, groupes et gère les
#                         inclure ActionPrevious.                               débordements

# ContextualActionView => Sous-classe de ActionView, pour des vues contextu =>  Extension de ActionView pour des cas
#                         elles spécifiques.                                     particuliers.

# ActionPrevious        => Affiche le titre et l'icône de l'application et une =>  Gère la navigation et le titre de l'app
#                           icône "précédent".                                  lication

# ActionItem       => Classe abstraite, base pour tous les widgets d'action  => Permet de créer les widgets personnalés.

# ActionButton      => Bouton standard avec texte et icône optionelle.      => Ajoute des actions interactives comme des
#                                                                               boutons

# ActionToggleButton => Bouton bascule (interrupteur) pour l'ActionBar => Permets des états activés/désactivés.

# ActionCheck       => Case à cocher pour l'ActionBar               =>      Ajoute des options booléennes

# ActionSeparator   => Séparateur visuel entre les éléments.    => Organise visuellement les éléments.

# ActionDropdown    => Menu déroulant pout l'ActionBar.         => Fournit des menus contextuels.

# ActionGroup   => Groupe d'éléments d'action, peut être    =>  Regroupe les actions sous un titre.
#                   en mode "normal" ou "spinner"

# ActionOverflow => Gère les éléments de débordement,           =>  Affiche les actions supplémentaire dans un menu
#                   visible quand l'espace est insuffisant.


                            # EXEMPLE 1: BARRE D'ACTION DE BASE
from kivy.app import App
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious, ActionButton, ActionGroup, ActionOverflow

class ActionBarApp(App):
    def build(self):
        action_bar = ActionBar()
        action_view = ActionView()

        # Ajouter ActionPrevious
        action_previous = ActionPrevious(title='Mon Application')
        action_view.add_widget(action_previous)

        # Ajouter Des boutons
        action_view.add_widget(ActionButton(text='Bouton 1', icon='../ps_icon.png'))
        action_view.add_widget(ActionButton(text='Bouton 2', icon='../AI_Application_Icon.ico'))

        # Ajouter un groupe
        group = ActionGroup(text='Groupe')
        group.add_widget(ActionButton(text="Groupe 1"))
        group.add_widget(ActionButton(text="Groupe 2"))
        action_view.add_widget(group)

        # Ajouter le déboudement
        overflow = ActionOverflow()
        action_view.add_widget(overflow)

        action_bar.add_widget(action_view)

        return action_bar

    def get_application_name(self):
        return "FranklinDev"
if __name__ == '__main__':
    ActionBarApp().run()


# cette exemple crée une bouton_play d'actions avec un titre, deux boutons, un groupe un menu de débordement

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyActionBarApp(App):
    def build(self):
        layout=BoxLayout(orientation='vertical')

        action_bar = ActionBar()
        action_view = ActionView()

        # ActionPrevious
        action_previous = ActionPrevious(title="Ma Super App")
        action_view.add_widget(action_previous)

        # Boutons avec actions
        def show_message(instance):
            print(f"Bouton {instance.text} cliqué !!!")

        action_view.add_widget(ActionButton(text="Bouton 1", icon="../ps_icon.png"))
        action_view.add_widget(ActionButton(text="Bouton 2", icon="../AI_Application_Icon.ico"))

        # Groupe avec boutons
        group = ActionGroup(text="Options")
        group.add_widget(ActionButton(text="Option 1", on_press=lambda x: show_message(x)))
        group.add_widget(ActionButton(text="Option 2", on_press=lambda x: show_message(x)))
        action_view.add_widget(group)

        # Débordement
        overflow = ActionOverflow()
        action_view.add_widget(overflow)

        action_bar.add_widget(action_view)

        # contenu principal
        content = Label(text="Contenu principale")
        layout.add_widget(action_bar)
        layout.add_widget(content)

        return layout

if __name__ == '__main__':
    MyActionBarApp().run()

# ici nous ajoutons des actions aux boutons pour afficher des messages, et intégrons un contenu principal sous la bouton_play.

# exemple 3 : Utilisation du langage kv

from kivy.lang import Builder

kv_string = '''
ActionBar:
    pos_hint: {'top': 1}
    ActionView:
        use_separator: True
        ActionPrevious:
            text: "Ma App"
            app_icon: "../AI_Application_Icon.ico"
        ActionButton:
            text: "Bouton 1"
            icon: "../ps_icon.png"
        ActionButton:
            text: "Bouton 2"
            icon: "../ps_icon.png"
        ActionGroup:
            text: "Groupe"
            ActionButton:
                text: "Groupe 1"
            ActionButton:
                text: "Groupe 2"
        ActionOverflow:
'''

class KvActionBarApp(App):
    def build(self):
        return Builder.load_string(kv_string)

if __name__ == '__main__':
    KvActionBarApp().run()

