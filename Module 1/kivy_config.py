# voir les descriptions dans deepseek

#1. introduction au module kivy.config
# le module kivy.config permet de configurer kivy au niveau global, avant même  l'initialisation de l'application.

# 2. Structure du Fichier
# voir deepseek et grok

# 3. API principale(Config) et utilisation.
# voir grok et deepseek

# importer Config depuis kivy.config
from kivy.config import Config
#Config.set(section, key, value) Définir une valeur avant l'import une valeur avant l'import des autres modules de kivy


# récuperer la largeur de la fenêtre
window_with = Config.get('graphics', 'height')
print(f"Hauteur de la fenêtre : {window_with}")
#Recupéré les éléments avec une convertion directe de valeur
#Config.getint(section, key)
#Config.getfloat(section, key)
#Config.getboolean(section, key)


# Modifier les paramètres dynamiquement
# on peut modifier les paramètres à l'exécution avec Config.set(section, key, value):
Config.set("graphics", "width", "1024")
Config.set("graphics", "height", '768')
#.Enrégistrer les modifications
Config.write()# pour sauvegarder les modifications dans le fichier

# Exemple complet Lecture et modification
from kivy.config import Config

# les paramètres actuels
print("Paramètres actuels :")
print(f"Largeur : {Config.get('graphics', 'width')}")
print(f"Hauteur : {Config.get('graphics', 'height')}")

# Modifier les paramètres
Config.set('graphics', "width",'1280')
Config.set('graphics', 'height', '720')
Config.set('graphics', 'fullscreen', '0')

# Enregistrer les modifications
Config.write()

print("Nouveaux paramètres enregistrés : ")
print(f"Largeur : {Config.get('graphics', 'width')}")
print(f"Hauteur : {Config.get('graphics', 'height')}")


#4. Principales sections et options de configuration
# voir grok ou le fichier source du module kivy.config qui est config.py pour les descriptions
#a. section [kivy]
#b. section [graphics]
#b. section [input]
#d. section [modules]
#e. section [postproc]# Cas d'utilisation

# 2. Configuration des entrées (Clavier, souris)
# Déactivé le multi-touch simulé (points rouge)
Config.set('input', 'mouse', 'mouse,disable_multitouch')
# Configurer un périphérique personalisé
Config.set('input', 'my_touchpad', 'hidinput,/dev/input/event2')

    #3. Logging et Performance
# Niveau de logs (debug, info, warning, error)
Config.set('kivy', 'log_label', 'warning')
    # Désactiver les logs dans la console
Config.set('kivy', 'log_enable', '1')
# Optimisation OpenGL
Config.set('graphics', 'maxfps', '60')
Config.write()

    #4. Confifuration avancée
#a. Activer/Désactiver les modules internes:
Config.set("modules", 'notify', "")
# Charger un modules personnalisé
Config.set('modules', 'my_modules', 'path/to/module')

#b. Fichier de config personnalisé
# Lire un fichier spécifique
Config.read(r"C:\Users\DELL\Documents\config.ini")
Config.set('modules', 'notify', 'message')# modifier l'option/Clé notify avec la valeur message dans le module modules
# Ecrire(enrégistrer ou rendre persistant) les modifications
Config.write()# Config.write() pour sauvegarder le fichier par défaut

#c. Gestion des Ecrans  Multiple
# Forcer l'utilisation d'un Ecran spécifique
Config.set('graphics', 'display', "1")


#5. Exemple pratique : personnalisation d'une Application
# Exemple d'application kivy qui utilise kivy.config pour permettre à l'utilisateur de modifier la taille de la fenêtre
# et le mode plein Ecran via interface graphique

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config

class ConfigApp(BoxLayout):
    def __init__(self, **kwargs):
        super(ConfigApp, self).__init__(**kwargs)
        self.orientation ='vertical'

        # Afficher les paramètres actuels
        self.width_label = Label(text=f"Largeur : {Config.get('graphics', 'width')}")
        self.height_label = Label(text=f"Hauteur : {Config.get('graphics', 'height')}")
        self.fullscreen_label = Label(text=f"Plein écran : {Config.get('graphics', 'fullscreen')}")

        # Champs de saisie pour modifier les paramètres
        self.width_input = TextInput(text=Config.get('graphics', 'width'), multiline=False)
        self.height_input = TextInput(text=Config.get('graphics', 'height'), multiline=False)
        self.fullscreen_input = TextInput(text=Config.get('graphics', 'fullscreen'), multiline=False)

        # Bouton pour appliquer les changements
        self.apply_button = Button(text='Appliquer', on_press=self.apply_change)

        # Ajouter les widgets à la mise en page
        self.add_widget(self.width_label)
        self.add_widget(self.width_input)
        self.add_widget(self.height_label)
        self.add_widget(self.height_input)
        self.add_widget(self.fullscreen_label)
        self.add_widget(self.fullscreen_input)
        self.add_widget(self.apply_button)

    def apply_change(self, instance):
        # Appliquer les nouvelles valeurs
        Config.set('graphics', 'width', self.width_input.text)
        Config.set('graphics', 'height', self.height_input.text)
        Config.set('graphics', 'fullscreen', self.fullscreen_input.text)
        Config.write()

        # Mettre à jour l'affichage
        self.width_label.text = f"Largeur : {Config.get('graphics', 'width')}"
        self.height_label.text = f"Hauteur : {Config.get('graphics', 'height')}"
        self.fullscreen_label.text = f"Plein écran : {Config.get('graphics', 'fullscreen')}"

        # Redimentionnemer la fenêtre(nécessite un redémarrage pour fullscreen)
        from kivy.core.window import Window
        Window.size = (int(self.width_input.text), int(self.height_input.text))

class MyApp(App):
    def build(self):
        return ConfigApp()

if __name__ == '__main__':
    MyApp().run()





