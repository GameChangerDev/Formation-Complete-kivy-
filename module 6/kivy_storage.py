# Formation avancée sur kivy.storage

# 1. introduction
#voir la description dans deepseek et grok apk

# 2. Fonctionnalités Avancées

# a.  JsonStore - Méthodes principales:
from kivy.storage.jsonstore import JsonStore

store = JsonStore("data.json")

# Ecrire des données
store.put("user1", name="Alice", score=100, achievements=["boss", "explorer"])

# Lire des données
user = store.get("user1")
print(user["name"]) # "Alice"

# Mise à jour
store.put("user1", score=150)   # concerve les autres champes

# Supprimer
store.delete("user1")

# Vérifier l'existance
if store.exists("user1"):
    print("Utilisateur existe")

# b. Gestion des erreurs:
try:
    store.get('invalid_key')
except KeyError:
    print(f"Clé inexistante")

# Erreurs d'E/S (fichier corrompu)
try:
    store = JsonStore("corrupted.json")
except Exception as e:
    print(f"Erreur: {e}")

# c. Transactions :
# Sauvegarde manuelle avant modifications
backup = store._data.copy()
try:
    store.put('temp', data=123)
    # Opération risqué...
    store.put("temp", data=456)
except:
    store._data = backup    # Rollback
    #store._save()

# 3. Cas pratique : Projet "TaskMaster"
"""
Description: Application de gestion des tâches avec :
    ° Création et suppression de tâches
    ° Catigorisation par projets
    ° Synchronisation automatique dans JsonStore
"""

# 3.2 DictStore
from kivy.storage.dictstore import DictStore

# Créer un DictStore
store = DictStore("data.db")

# Ajouter des données
store.put("user1", name="Bob", age=25, custom_obj={'x': 1, 'y':2})

# Récupérer des données
user_data = store.get("user1")
print(user_data) # {'name': 'Bob', 'age': 25, 'custom_obj': {'x': 1, 'y': 2}}

# supprimer
store.delete('user1')

# Utilisez DictStore pour les données non-JSON (ex: objets pythons)