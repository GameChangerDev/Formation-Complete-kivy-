#from kivy.animation import Animation
#from kivy.uix.button import Button
#from kivy.app import App


#           TRAVAIL PRÉSENTAION ET UTILISATON DU MODULE kivy.animation
"""
le module kivy.animation de kivy fournit des outils pour créer des animations fluides , permettant de modifier les propr
iétés d'objets(comme la position, la taille, l'opacité etc.) au fils du temps
il est particulièrement utile pour animer les widgets dans une interface utilisateurs, comme déplacer un bouton faire
apparaître un élément ou changer sa couleur.
la classe principale est Animation mais le module inclut d'autre classes et fonctions pour gérer les animations complex
es ou combinées.
"""
                    # VUE D'ENSEMBLE SUR LE MODULE
"""
Le module kivy.animation contient:
    - classes principales : Animation (pour créer des avnimations simples),
    AnimationTransition (pour définir les courbes de transitions), et compoundAnimation(pour combiner plusieurs animatio
    ns, bien que cette classe soit interne
    
    - Fonctions utilitaires : Aucune fonction autonome n'est exposée directement dans le module, mais les classes inclu
    ent des méthodes statiques ou des attributs pour personnaliser des animations
    
    - Concepts clés :
        - Une animation modifie une propriéte d'un objet (par exemple, pos, opacity) en interpolant entre une valeur in
        itiale et une et une valeur cible.
        - Les animation peuvent être enchaînées, parallelisées, répétées ou annulées
        - les transitions (comme linear, in_out_cubic) contrôlent la vitesse des animations.
"""

# ORDRE DE RÉSOLUTION DE METHODE
    #Builtins.objet
        #kivy._event.ObjetWithUid
            #kivy._event.EventDispatcher
                #Animation

                    #classe et méthodes de kivy.animation


"""
                                                1. CLASSE Animation
    -Rôle générale: crée une animation qui modifie une ou plusieurs propriétés d'un ojet(généralement un widget)
    sur une durée données. par exemple, déplacer un widget de (0, 0) à (100, 100) en 2 secondes
    
    -constructeur : Animation(**kwargs)
    
    Rôle: initialise une transition avec des propriétés cibles et des paramètres
    
    -paramètres : 
        - **kwargs: paires clé-valeur où la clé est le nom de la propriété à animer(par exemple, x, opacity) et la valeur 
        est la valeur cible.
        
        - duration (ou d): durée de l'animation en secondes par défaut 1.0
        -transition (ou t): Type de transition (par exemple, 'linear', 'in_out_cubic') ou une fonction personnalisée (pa
        r défaut 'linear'.
        - step (ou s) : intervalle de temps minimum entre deux mises à jour (par défaut 0 dépend du framerate)
"""
# exemple:
#btn = Button(pos=(0, 0))
#anim = Animation(x=100, y=100, duration=2, t="out_bounce")
#anim.start(btn) # déplace le bouton à (100, 100) en 2 secondes

#méthode de Animation
"""
1. start(self, widget)
    - Rôle : Démarré l'animation sur l'objet spécifié (généralement un widget)
    - Paramètre :
        - widget : l'objet dont les propriétés seront animées. 
"""
# exemple
#anim = Animation(opacity=0, duration=1)
#anim.start(btn)
"""
Rôle détaillé : lie l'animation à l'objet et commence à interpoler les propriétés.
"""

# 2. stop(self, **kwargs)
"""
Role: arrête l'animation en cours pour l'objet spécifié, laissant les propriétés à leur état actuel
    -paramètres :
        - widget : l'objet animé
"""
# exemple :
#anim.stop(btn)# arrête l'animation du bouton
"""
Rôle détaillé :
    interrompt l'animation sans réinitialiser les valeurs des propriétés
"""

# 3. cancel(self, widget)
"""
Rôle : annule l'animation pour l'objet spécifié, réinitialisant les propriétés à leurs valeurs initiales (avant le début
    de l'animation).
    - paramètres : 
        - widget : l'objet animé.
"""
# exemple :
#anim.cancel(btn) # annule et réinitialise les propriétés du bouton
#Rôle détaillé :Utile pour revenir à l'état initial si l'animation est interrompue.

# 4. bind(self, **kwargs)
"""
Rôle et paramètres déjà vu dans le module kivy._event
ici on lié des fonctions de rappel à des événements d'animations, comme 'on_start', 'on_progress', 'on_complete'.

    - Evenements disponibles :
        - on_start: Déclenché au début de l'animation.
        - on_progress : déclenché à chaque mise à jour( avec une valeur de progression de 0 et 1).
        - on_complete : déclenché à la fin de l'animation
"""
# exemple :
"""
def on_complete(animation, widget):
    print("Animation Terminée !!!\n", f"animation : {animation}\n", f"widget : {widget}")
anim = Animation(x=100, duration=1)
anim.bind(on_complete=on_complete)
anim.start(btn)
"""
#Rôle détaillé : Permet d'exécuter des actions spécifiques à des moments clés de l'animation.

# 5. unbind(self, **kwargs)
#Rôle : supprime une liaison d'une fonction de rappel à un événement d'animation
# exemple :
#anim.unbind(on_complete=on_complete)
# Rôle détaillé : Utile pour nettoyer les liaisons d'événements inutiles.

#6. cancel_all(cls, widget, *args) (méthode de classe)
"""
Rôle : Annule toute les animations en cours pour un widget donné, ou seulement celles spécifiées dans args.

paramètres : 
    - widget : l'objet animé
    - args : Noms des propriétés à annuler (optionnel, si omis, toutes les animationns sont annulées)
"""
# Exemple :
"""
Animation.cancel_all(btn)# Annule toutes les Animations du bouton
Animation.cancel_all(btn, 'x', 'y')# annule seulement les animations de x et de y
"""
# Rôle détaillé : permet de Néttoyer toute les animations d'un widget, utile pour éviter les conflits

# 7. stop_all(cls, widget, *args) (méthode de classe)
"""
Rôle : Arrête toutes les animations en cours pour un widget, ou seulement celles, sans réinitialiser les propriétés.

paramètres : 
    - widget : l'objet animé.
    - args : Noms des propriétés à arrêtées (optionnel)
"""
# exemple :
"""
Animation.stop_all(btn)
Animation.stop_all(btn, 'x', 'y')
"""
#Rôle : Similaire à cancel_all, mais laisse les propriétés à leur état actuel

#8. animated_properties(self)  (c'est une propriété donc n'est pas callable)
"""
Rôle : retourne un dictionnaire(clé-valeur: clé est le nom de la propriété et valeur est la valeur de la propriété) des 
    propriétés animées par cette animmation.
Retour : dictionnaire des noms des propriétés (par exemple, {'x': 100, 'y': 100}).
"""
# exemple :
"""
anim = Animation(x=100, y=100, transition="out_bounce")
anim.start(btn)
anim.bind(on_complete=lambda *args: print(anim.animated_properties))# {'x': 100, 'y': 100}
"""
# Rôle détaillé : Utile pour inspecter quelles propriétés sont affectées pour l'animation.


"""
                                        2. Classe AnimationTransition
-Rôle général : Fournit des fonctions de transition pour contrôler la progréssion d'une animation (par exemple, linéaire,
    accélérée, rebondissante). chaque transitiion est une fonction qui prend une valeur de progréssion (entre 0 et 1) et
    retourne une valeur interpolée.
- transitions statique(prédéfinies):
    ° linear : Progréssion linéaire(vitesse constante).
    ° in_quad, out_quad, in_out_quad : transitions quadratiques (accélération et décélération douce).
    ° in_cubic, out_cubic, in_out_cubic : transitions cubiques (plus prononcées)
    ° in_quart, out_quart, in_out_quart : transitions quartiques
    ° in_quint, out_quint, in_out_quint : Transitions Quintiques.
    ° in_sine, out_sine, in_out_sine: Transition sinusoïdale(douces).
    ° in_circ, out_circ, in_out_circ : Transitions basé sur un cercle.
    ° in_expo, out_expo, in_out_expo : Transitions exponentielles(très rapide au debut ou à la fin)
    ° in_elastic, out_elastic, in_out_elastic : Transitions avec éffet élastique (rebond).
    ° in_back, out_back, in_out_back : Transitions avec dépassement (éffet de recul).
    ° in_bounce, out_bounce, in_out_bounce : Transition avec éffet de rebond.
- Rôle détaillé : chaque transition modifie la façon dont la propiété change au fil du temps. par exemple, out_bounce
donne un effet de rebond à la fin de l'animation.
"""
# exemple :
#anim = Animation(x=-100, y=-100, duration=3, transition="out_bounce")# déplace le bouton avec un éffet de rebond
#anim.start(btn)
# Note: vous pouve créez une fonction personnalisée en passant une fonction qui prend une progression (0 et 1) et retourn
# e une valeur interpolée.


"""
                                        3. classe CompoundAnimation
                                (interne non documenté officiellement)
Rôle général : utilisé en interne pour gérer des animations combinées(séquentielle ou parallèles). elle n'est pas destin
ée à être utilisée directement, mais elle est crée implicitement avec les opérateurs + (séquentielle) et & (parallèle).
"""
"""
# exemple d'utilisation :
btn = Button(pos=(0, 0), text="Animation")
anim1 = Animation(x=100, duration=1)
anim2 = Animation(y=100, duration=1)
seq = anim1 + anim2
par = anim1 & anim2
seq.start(btn)# Animation séquentielle
par.start(btn)# Animation parallèle
"""
"""
Rôle détaillé: Permet de combiner des animations pour des effets complexes sans avoir à gérer manuellement la synchroni
sation.
"""

"""
Opérateurs spéciaux pour Animation
° + (addition) : Crée une animation séquentielle où la deuxième commence après la fin de la première
-exemple: anim1 + anim2 -> anim1 s'exécute, puis anim2.
° & (binaire) : Crée une animation parallèle où deux animations s'exécutent simultanément.
-exemple: anim1 & anim2 -> anim1 et anim2 s'exécute simultanement 
Rôle détaillé : simplifie la création d'animation complexe en evitant de manipuler manuellement les delais ou les événe
ments.
"""
'''
class MonApp(App):
    def build(self):
        return btn

if __name__ == '__main__':
    MonApp().run()
'''

                                # EXEMPLE COMPLET DE L'UTILISATION

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

class MonApp(App):
    def build(self):
        layout = FloatLayout()
        btn = Button(text="Animer", size_hint=(0.2, 0.2), pos=(0, 0))
        layout.add_widget(btn)

        # Animation Séquentielle : Déplacer puis changer l'opacité
        anim1 = Animation(pos=(200, 200), duration=2, t="out_bounce")
        anim2 = Animation(opacity=0, duration=1, t="in_out_cubic")
        seq = anim1 + anim2

        # Animation parallèle : changer la taille et la couleur
        anim3 = Animation(size=(100, 100), duration=1, t="out_bounce")
        anim4 = Animation(background_color=(1,0,0,1), duration=3)
        par = anim3 & anim4

        # lier des événements
        def on_complete(animation, widget):
            print("Animation Terminée !!")
            widget.opacity = 1# Réinialisation de l'opacité
            par.start(widget)# Lancer l'animation parallèle

        seq.bind(on_complete=on_complete)

        # Démarrer l'animation au click
        btn.bind(on_press=lambda x: seq.start(btn))
        return layout
if __name__ == '__main__':
    MonApp().run()
