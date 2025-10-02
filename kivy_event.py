# EXPLICATIONs ET UTILISATIONS DES METHODES Du module de kivy.event
#methode de _event(Builtins.object => ObjectWithUid => EventDispatcher => Observable)
#toutes les methodes s'appliques sur la classe EventDispatcher
from kivy.event import EventDispatcher
from kivy.uix.button import Button
from kivy.app import App

# 1. __init__(self, **kwargs)
"""
Rôle: constructeur de la class EventDispatcher. initialise un objet capable de gérer des évènements.
les arguments kwargs permettent de passer des valeurs initiales pour les propriétés de l'objet
"""
# exemple:
class MonEvenement(EventDispatcher):
    def __init__(self, **kwargs):
        super(MonEvenement, self).__init__(**kwargs)
"""
Note: cette méthode est généralement appelée implicitement lorsque vous créez un widget ou une classe dérivée
"""

# 2. bind(self, **kwargs)
"""
Rôle: lier une fonction de rappel(callback) à un événement ou à une propriété spécifique. Lorsqu'un événemenet est
déclenché ou qu'une propriété change, la fonction liée est appelée
    .paramètres:
        kwargs : paires clé-valeur où la clé est le nom de l'événement(par exemple, on_press) et la valeur est la foncti
        on de rappel
"""
"""
# exemple:
class MonWidget(EventDispatcher):
    def __init__(self, **kwargs):
        super(MonWidget, self).__init__(**kwargs)
        self.register_event_type("on_mon_evenement")
        self.bind(on_mon_evenement=self.callback)

    def callback(self, *args):
        print("Evénement déclenché !!")

    def on_mon_evenement(self, *args):
        pass
widget = MonWidget()
widget.dispatch("on_mon_evenement")# déclenche l'événement qui va afficher Evenement déclenché
"""

"""
Rôle détaillé : permet de connecter une action à un événement, comme un clic sur un bouton ou un changement de proprié
té. la fonction bind utilise une WeakMethod pour éviter les fuites de mémoire 
"""


# 3. fbind(self, name, func, *args, **kwargs)
"""
Rôle: c'est un version plus avancé de bind pour une liaison rapide, souvent utilisée en interne par kivy(par exemp
le dans le langage KV). contrairement à bind, elle ne vérifie pas si une fonction est déjà lié et stocke directement 
la fonction (sans WeakMethod) à moins que ref=True ne soit spécifié.
    :paramètre
        - name : Nom de l'événement où de la propriété (par exemple, 'on_press')
        - func : Fonction de rappel a exécutée.
        - args : Argumentqs positionnels à passer à la fonction.
        - kwargs : Arguments nommés à passer à la fonction.
    retour: un identifiant unique (UID) pour la liaison, utilisable pour ma désinscription avec unbind_uid
"""
# exemple:
btn = Button()
btn.fbind('on_press', lambda instance: print("Bouton pressé"))

"""
Rôle: utilisé pour les liaisons performantes dans les fichiers KV. Attention il faut utiliser funbind ou unbind_uid
pour supprimer la liaison.
"""

# 4. unbind(self, **kwargs)
"""
Rôle: supprime une liason à une fonction ou une propriété spécifique. supprime toutes les instances de la fonction
pour cette événement
    :paramètres:
        - kwargs : paires clé-valeur où la clé est le nom de l'événement et la valeur est la fonction à supprimée.
"""
# exemple:
def callback(instance):
    print("Evénement déclenché !!")

btn = Button()
btn.bind(on_press=callback)
btn.unbind(on_press=callback)#supprime la liaison # supprime l'événement on_press lié à callback
"""
Rôle détaillé : utile pour arrêter de réagir à un événement, par exemple si un widget n'a plus besoin de repondre à
un clic
"""

# 5. funbind(self, name, func, *args, **kwargs)
"""
Rôle: Version avancée de unbind, utilisée pour supprimer une liaison créee avec fbind, Ne supprime que la première inst
ance correspondant aux arguments données.
     :paramètre:
        - name : Nom de l'événement ou de la propriété.
        - func : Fonction à supprimer.
        - args et kwargs doivent correspondre à ceux utilisés dans fbind
"""
# exemple:
btn = Button()
btn.fbind("on_press", lambda x: print("préssé"), "arg1")
btn.funbind("on_press", lambda x: print("préssé"), "arg1")
"""
Rôle détaillé: Précis pour supprimer des liaison spécifiques créées avec fbind.
souvent utilisé dans les contextes internes et complexes
"""

# 6. unbind_uid(self, name, uid)
"""
Rôle : Supprime les liaisons spécifiques en utilisant l'identifiant unique (UID) retourné par fbind.
    :paramètres:
        - name : Nom de l'énénement ou de la propriété.
        - uid : identifiant unique de la liaison.
"""
# exemple:
btn = Button()
uid = btn.fbind("on_press", lambda x: print("préssé"))
btn.unbind_uid("on_press", uid)
"""
Rôle détaillé: Permet une suppréssion précise sans avoir à spécifié la fonction, utile por gérer les liaison dynamiq
ues
"""

# 7. dispatch(self, event_type, *args, **kwargs)
"""
Rôle: déclenche un événement donné , appelant toutes les fonctions de rappel liées à cet événement. l'exécution s'arrête
si un gestionnaire retourne True.
    :paramètres:
        - event_type : nom de l'événement à déclenché(par exemple,  on_mon_evenemenet).
        - args : Arguments positionnels à passés aux gestionnaires
        - kwargs : Arguments nommées  à psssés aux gestionnaires
"""
# exemple:
"""
class MonWidget(EventDispatcher):
    def __init__(self, **kwargs):
        super(MonWidget, self).__init__(**kwargs)
        self.register_event_type("on_mon_evenement")
        self.bind(on_mon_evenement=lambda x: print("Evénement !"))
        self.dispatch("on_mon_evenement")# Affiche Evénement!
"""
"""
Rôle détaillé: Permet de déclencher manuelolement un événement , utile pour les événements personnalisés ou pour simuler
les intéractions
"""

#8. register_event_type(self, event_type)
"""
Rôle : Enregistre un nouveautype d'événement personnalisé pour l'object,.le nom de kl'événement doit commencer
    par 'on_'.
    :paramètres:
        - event_type : nom de l'événement(par exemple, 'on_mon_evenement').
"""
# exemple:
"""
class MonWidget(EventDispatcher):
    def __init__(self, **kwargs):
        super(MonWidget, self).__init__(**kwargs)
        self.register_event_type('on_mon_evenement')

    def on_mon_evenement(self, *args):
        pass# gestionnaire par défaut
"""
"""
Rôle détaillé: Nécessaire pour créer des événements personnalisés que vous pouvez déclencher et lier.
"""

# 9. unregister_event_type(self, event_type)
"""
Rôle: Supprime un type d'événement personnalisé précédemment enregistré.
    :paramètres:
        - event_type : Nom de l'événement à supprimer
"""
# exemple:
"""
widget = MonWidget()
widget.unregister_event_type("on_mon_evenement")
"""
"""
Rôle détaillé: Utile pour nettoyer des événements personnalisés qui ne sont plus nécessaire.
"""

# 10. is_event-type(self, event_type)
"""
Rôle: vérifie si un type d'événement est enregistré pour l'objet
        :paramètres:
            - event_type : Nom de l'événement à vérifier.
        retour:
            True si l'événement est enregistré, False sinon
"""
# exemple:
"""
widget = MonWidget()
print(widget.is_event_type("on_mon_evenement")) # True si enregistré
"""
"""
Rôle détaillé: permet de vérifier si un événement est disponible avant de le declencher ou de le lier
"""

# 11. get_property_observers(self, name, args=False)
"""
Rôle: Retourne la liste des fonctions de rappel liées à un événement ou une propriété
    :paramètres:
        - name : Nom de l'événement ou de la propriété
        - args : si True, il retourne les arguments associés aux liaisons
    retour: liste des gestionnaires (ou tuples avec arguments si args=True).
"""
# exemple:
btn = Button()
btn.bind(on_press=lambda  x: print("Pressé"))
print(btn.get_property_observers('on_press'))
"""
Rôle détaillé: Utile pour déboguer ou inspecter les liaison d'événements.
"""

# 12. events(self)
"""
Rôle: Retourne la liste de tous les types d'événements enregistrés pour l'objet.
    retour: liste des noms d'événements.
"""
# exemple:
"""
widget = MonWidget()
widget.register_event_type("on_mon_evenement")
print(widget.events())
"""
"""
Rôle détaillé: Permet l'instrospection des événements disponibles  pour un objet
"""

# 13. getter(self, name)
"""
Rôle: Retourne la fonction getter d'une propriété donnée.
    :paramètres:
        - name : Nom de la propriété.
    retour : Fonction getter
"""
# exemple :
"""
btn = Button()
getter = btn.getter("text")
print(getter())# Affiche le text du bouton
"""
"""
Rôle détaillé: utilisé pour accéder programmatiquemment  aux valeurs des propriétés
"""

# 14. setter(self, name)
"""
Rôle: Retourne la fonction setter d'une propriété donnnée.
    :paramètres:
        - name : Nom de la propriété
    retour: Fonction setter
"""
# exemple:
"""
btn = Button()
setter = btn.setter("text")
setter("Nouveau text")# change le texte du bouton
"""
"""
Rôle détaillé: Permet de modifier programmatiquement les valeurs des propriétés
"""


                                #  EXERCICE EXEMPLE COMPLET D'UTILISATION


def rappel(*args):
    print("evenement rappel eexécuté avec succès".capitalize())
def on_mon_event(*args):
    pass

bouton = Button(text="Cliquez pour déclencher")
bouton.bind(on_press=rappel)




class MonWidget(EventDispatcher):
    def __init__(self, **kwargs):
        super(MonWidget, self).__init__(**kwargs)
        self.register_event_type("on_mon_evenement")
        self.bind(on_mon_evenement=self.fonction_rapple)

    def fonction_rapple(self, *args):
        print("evenement rappel eexécuté avec succès".capitalize())

    def on_mon_evenement(self, *args):
        pass

class MonApp(App):
    def build(self):
        btn = Button(text="Cliquez pour déclencher")
        btn.bind(on_press=lambda x: bouton.dispatch("on_press"))
        return btn
if __name__ == '__main__':
    MonApp().run()

