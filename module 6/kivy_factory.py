#voir la description dans deepseek
# Partie 1: Comprendre kivy.factory.Factory

# Partie 2: Fonctuionnalités avancées

from kivy.uix.label import Label
# 1. enregistrement de classes:
from kivy.factory import Factory, FactoryException

# enregistrement explicite
Factory.register('MonBouton', cls=CustumButton, module='mon_module')

# via décorateur
@Factory.register
class CustomLAbel(Label):
    pass

# 2. Alias et surcharge :
Factory.register('SuperButton', alias='Button') # Alias
Factory.register('Button', cls=CustomButton) # Surcharge

# 3. Instanciation dynamique :
widget = Factory.get('MonBouton')() # instanciation

# 4. Gestion d'Erreurs :
try:
    Factory.get('WidgetInexistant')
except FactoryException:
    print("classe non enregitrée")

# Partie 3: Projet pratique: "dynamique UI Builder"
# Objectif: Créer une application qui génère dynamiquement une interface utilisateur basée sur un fichier Json