#from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.button import Button
#from kivy.uix.settings import Settings

                    #VUE D'ENSEMBLE SUR LE MODULE kivy.app

"""
le module kivy.app contient principalement:
    -Classe App : La classe de base pour créer une application kivy, elle gère l'iniatialisation, le rendu de l'inter
    face, et les événements du circle de vie.
    
    - Fonctions utilitaires : quelques fonctions mineurs pour gérer les paramètres ou les ressources, mais la class
    e App est le coeur du module .
    
    -Concepts clés :
        ° Une application kivy hérite de App et définit la méthode build pour construire l'interface(retourne un widget
        racine).
        ° Elle gère les événements comme on_start, on_stop, on_pause, etc.
        ° Elle permet de configurer des propriétés globales (titre, icône, répertoire, etc).
"""

# ordre de résolution des méthodes :
#       => builtins.object
#           => kivy._event.ObjectWithUid
#               => kivy._event.EventDispatcher
#                   => App

# Classe App
"""
Rôle général : La classe App est utilisé pour créer une application kivy. En héritant de cette classe vous définissez le
comportement de votre application. Elle fournit des méthodes pour initialiser l'application, gérer son cycle de vie et 
intéragir avec les paramètres ou les ressources.
- Contructeur : App(**kwargs)
    ° Rôle : initialise l'application avec des options facultatives.
    ° Paramètres : **kwargs pour des configurations spécifique(rarement utilisé directement).
"""
# exemple :
"""
class MonApp(App):
    def build(self):
        return Label(text="Bonjour kivy !")
"""

                                # Méthode principale de App

#voici une liste complète des méthodes de la classe App, avec leur Rôle en français,basée sur la Documentation officiell

#1. build(self)
"""
Rôle : Définit l'interface utilisateur de l'application en retournant le widget racine(par exemple, un Label, Button,
ou un layout comme FloatLayout).
-Retour : un widget  (instance de kivy.uix.widget.widget ou une sous classe).
"""
# exemple :
"""
class MonApp(App):
    def build(self):
        return Button(text="Cliquez ici")
Rôle détaillé : cette méthode est appelée automatiquement au démarrage de l'application pour constriure l'arbre des wid
gets. Elle es obligatoire à redéfinir dans votre classe.
"""

# 2. run(self)
# Rôle : Démarre l'application lançant la boucle de kivy (gestion des événements, rendu graphique, etc).
# exemple :
"""
if __name__ == '__main__':
    MonApp().run()

#Rôle détaillé : Cette méthode initialise la fenêtre, charge les ressources, et exécute l'application. elle bloque juqu
# a ce que l'application soit fermée.
"""


# 3. stop(self)
# Rôle : Arrête l'application proprement , déclenchant l'événement on_stop et fermant la fenêtre.
# Exemple :
"""
class MonApp(App):
    def build(self):
        btn = Button(text="Arrêter")
        btn.bind(on_press=self.stop)
        return btn
"""
# Rôle détailé : Utile pour fermer l'application dépuis un bouton ou un autre événement.

#4. on_start(self)
# Rôle : Evénement appelé juste après le démarrage de l'application, une fois l'interface initialisée.
# Exemple :
"""
class MonApp(App):
    def build(self):
        return Button(text="Démarré")
    def on_start(self):
        print(f"l'application a démarré")
    def on_stop(self):
        print("App fermée/ Application s'arrête !")
    def on_pause(self):
        print("Application est en pause !")
        return True
    def on_resume(self):
        print("Application reprise")
"""
# Rôle détaillé : Permet d'exécuter des tâches au démarrage, comme charger les données ou initialiser les composants

#5. on_stop(self)
# Rôle : Evénement appelé lorsque l'application se ferme(via stop() ou en quittant).
# Exemple : voire #4.
# Rôle détaillé : Idéal pour sauvegarder l'etat, libérer des ressources ou éffectuer des tâches de néttoyage.

#6. on_pause(self)
"""
Rôle : evénément appelé lorsque l'application est mise en pause, par exemple, sur mobile quand l'utilisateur passe à une
autre application
Retour : True pour autoriser la pause, False pour l'empêcher (si possible).
"""
# exemple : voire #4.
# Rôle détaillé : utile sur les plateformes mobiles pour sauvegarder l'état avant la mise en pause.

#7. on_resume(self)
# Rôle : Evénement appelé lorsque l'application reprend après une pause.
# Exemple : voire #4
# Rôle détaillé : Permet de restaurer l'état ou de rafraîchir l'interface après une pause.

#8. load_config(self)
"""
Rôle : Charge le fichier de configuration(par défaut, un fichier .ini dans le repertoire de l'application).
Retour : une instance de kivy.config.ConfigParser
"""
# exemple :
'''
class MonApp(App):
    def build(self):
        config = self.load_config()
        print(config.get("section", "key"))# erreur
        return Label(text="Config chargé")
'''
# Rôle détaillé: permet de lire les paramètres personnalisés stockés dans un fichier .ini

# 9. get_application_name(self)
"""
-Rôle : Retourne le nom de l'application, utilisé comme titre de fenêtre ou dans les métadonnées.
-Retour : Une chaîne de caractère par défaut, le nom de la classe sans 'App').
"""
"""
# exemle
class MonApp(App):
    def get_application_name(self):
        return "Mon Application"
    def get_application_icon(self):
        return "AI_Application_Icon.ico"# chemin vers l'icôn de l'application
    def get_application_config(self, defaultpath='%(appdir)s/%(appname)s.ini'):
        return defaultpath# config/mon_app.ini
"""
# Rôle détaillé : Permet de personnaliser le titre de la fenêtre .

#10. get_application_icon(self)
"""
-Rôle : Retourne le chemin vers l'icône de l'application.
- Retour : une chaîne de caractère par défaut, data/icon.png dans le repertoire kivy
"""
# exemple : voire #9

#11. get_application_config(self)
"""
- Rôle : Retourne le chemin du fichier de configuration de l'application.
- Retour : Une chîne de caractères (par défaut , -/.kivy/config/<nom_app>.ini
"""
# exemple : voire #9.
# Rôle : permet de spécifier un fichier de configuration personnalisé.

#12. open_settings(self, *largs)
#Rôle : Ouvre l'interface des paramètres de l'application (si configuré).
# exemple :
"""
class MonApp(App):
    def build(self):
        btn = Button(text="Ouvrir Paramètres")
        btn.bind(on_press=self.open_settings)
        return btn
"""
# Rôle détaillé : Affiche un panneau de configuration(souvent utilisé avec build_settings).

#13. close_settings(self, *largs)
#- Rôle : Ferme l'interface des paramètres.
# exemple:
"""
class MonApp(App):
    def close_settings(self, *largs):
        print("Paramètre fermés")
        super(MonApp, self).close_settings(*largs)
"""
# Rôle détaillé : Utile pour personnaliser la fermeture du panneau des paramètres.

#14. build_settings(self, settings)
"""
- Rôle : Construit l'interface des paramètres en ajoutant des sections et des champs à un objet Settings.
-:paramètres : 
    - settings : instance de kivy.uix.settings.Settings.
"""
"""
# Exemple :
class MonApp(App):
    def build(self):
        btn = Button(text="param", size_hint=(1/15, 1/20))
        btn.bind(on_press=self.open_settings)
        return btn
    def build_settings(self, settings):
        settings.add_json_panel("Paramètres", self.config, data='[{"type": "string", "title": "Nom", "section":"General", "key": "name"}]')
"""
# Rôle détaillé : Permet de définir une interface de paramètres personnalisée (par exemple, avec json).

# 15. on_config_change(self, config, section, key, value)
"""
Rôle : Evénement appelé lorsqu'une valeur dans la configuration change
-paramètres : 
    - config : instance de ConfigParser.
    - section : section du fichier .ini
    - key : Clé à modifiée.
    - value : Nouvel valeur.
"""
"""
# Exemple
class MonApp(App):
    def on_config_change(self, config, section, key, value):
       print(f"Config changée : {section}, {key} = {value}")
"""
# Rôle détaillé : Permet de réagir aux modifications des paramètres.

#16. root_window (propriété, lecture seule)
# Rôle : Retourne la fenêtre principale de l'application (instance de kivy.core.window.window).
# exemple :
"""
class MonApp(App):
    def build(self):
        print(self.root_window.size)#erreur
        return Label(text="Fenêtre")
"""
# Rôle détaillé : permet d'accéder aux propriétés de la fenêtre(taille, plein ecran, etc).

# Propriétés de App
"""
Les propriétés suivantes sont définies dans la classe App et peuvent être utilisées ou animées (si applicable):
    - name (StringProperty):
        ° Rôle : Nom de l'application, utilisé pour le fichier de configuration et d'autres métadonnées.
        ° valeur par défaut : Nom de la classe sans "App".
        ° exemple : app.name = "mon_app" définit le nom pour le fichier .ini.
    - icon [StringProperty)
        ° Rôle : chemin vers l'icône de l'application
        ° Valeur par défaut : data/icon.png
        ° Exemple : app.icon = "mon_icon.png".
    
    - title (StringProperty)
        ° Rôle : Titre de la fenêtre de l'application.
        ° Valeur par défaut : Valeur retournée par get_application_name().
        ° Exemple : app.title = "Ma Super App".
    
    - config(ObjectProperty):
        ° Rôle : Instance de ConfigParser contenant les paramètres des applications.
        ° exemple : app.config.get("section", "key")
    - directory (StoringProperty)
        ° Rôle : Répertoire de l'application (où sont stockées les ressources).
        ° Valeur par défaut : Répertoire du fichier par défaut.
        ° Exemple : app.directory = "ressource/".
    - user_data_dir (StringProperty, lecture seule) : 
        - Rôle : Répertoire où les données utilisateur sont stockées (par exemple, ~/kivy/<mon_app>/).
        - Exemple :
            print(app.user_data_dir).
"""

# Evénements de App
"""
la classe App utilise le mécanisme de EventDispatcher les événements sont (on_start, on_stop, on_pause, on_res
me, on_config_change)
"""

"""
if __name__ == '__main__':
    MonApp().run()
"""

                                    # EXEMPLE COMPLE D'UTILISATION

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.config import ConfigParser

class MonApp(App):
    def build(self):
        layout = FloatLayout()
        btn = Button(text="Ouvrir pramètres", size_hint=(0.2, 0.1), pos=(100, 100))
        btn.bind(on_press=self.open_settings)
        stop_btn = Button(text="Arrêter", size_hint=(0.2, 0.1), pos=(100, 200))
        stop_btn.bind(on_press=self.stop)
        layout.add_widget(btn)
        layout.add_widget(stop_btn)
        l_options = self.load_config().options("General")
        print(self.load_config().has_option("General", l_options[0]))
        return layout
    def get_application_name(self):
        return "Illustrator"

    def get_application_icon(self):
        return "AI_Application_Icon.ico"

    def build_config(self, config):
        config.setdefaults("General", {'name': 'Utilisateur', 'volume': 50, "pk": True})
        config.setdefaults("Users", {'nom_user': 'franklin', 'apk': True, 'niveau': 'interm-avance', 'age': 19})
        config.setdefaults("Jon", {"erreur": False})

    def build_settings(self, settings):
        settings.add_json_panel("Paramètres", self.config, data='''
        [
            {"type": "string", "title": "Nom", "section": "General", "key": "name"},
            {"type": "numeric", "title": "Volume", "section": "General", "key": "volume"}
        ]
        ''')
        settings.add_json_panel("Users", self.config,data='''[{"type": "string", "title": "Nom d' user", "section": "Users", "key": "nom_user"},
            {"type": "bool", "title": "Apk", "section": "Users", "key": "apk"},
            {"type": "string", "title": "Niveau d'espérience", "section": "Users", "key": "niveau"},
            {"type": "numeric", "title": "âge", "section": "Users", "key": "age"}]''')
        settings.add_json_panel("Jon", self.config, filename="panel.json")

    def on_config_change(self, config, section, key, value):
        print(f"Config changée : {section}, {key} = {value}")

    def on_start(self):
        print(f"Démarrage de {self.get_application_name()}")
        print(f"Config : {self.config.get("General", "name")}")

    def on_stop(self):
        print("Arrêt de l'application")

    def close_settings(self, *largs):
        print("Paramètres fermés !!")
        super().close_settings(largs)


if __name__ == '__main__':
    MonApp().run()


