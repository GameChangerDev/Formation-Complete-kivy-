#voir la description dans deepseek et grok apk ou le code source
from kivy.network.urlrequest import UrlRequest

# Partie 1: Bases kivy.network
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from random import random
from kivy.graphics import Rectangle, Color

class MyApp(App):
    def build(self):
        self.label = Label(text="Chargement")
        # LAncer une requête GET
        UrlRequest(
            url="https://api.github.com/users/GameChangerDev",
            on_success=self.on_success,
            on_failure=self.on_failure,
            on_error=self.on_error
        )
        Window.bind(on_touch_move=self.update_label_c)
        return self.label

    def on_success(self, request, result):
        self.label.text = f"Réponse : {result}"

    def on_failure(self, request, result):
        self.label.text = f"Echec : {result}"

    def on_error(self, request, error):
        self.label.text = f"Erreur : {error}"

    def update_label_c(self, *args):
        with self.label.canvas:
            Color(random(), random(), random(), 0.1)
            Rectangle(size=self.label.size, pos=self.label.pos)

MyApp().run()

print(h)
# 1.2 Types de requêtes HTTP
# GET :  récupérer des données
# POST :  Envoyer des données
# PUT : Mettre à jour les données
# DELETE : Supprimer des données
from json import dumps
# Requête POST:
headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer YOUR_TOKEN'
}
def on_success():
    pass
def on_error():
    pass
req = UrlRequest(
    url="https://api.github.com/users/GameChangerDev",
    req_headers=headers,
    req_body=dumps({"key": 'value'}),
    on_success=on_success,
    on_error=on_error,
    method='POST'
)

# 2. Gestion des erreurs avancé
def handle_response(request:UrlRequest, result):
    if request.resp_status == 200:
        print('Success:', result)
    elif request.resp_status == 401:
        print("Non authorisé")
    else:
        print(f"Erreur {request.resp_status}: {result}")

req = UrlRequest()
req.url = "https://api.github.com/users/GameChangerDev"
req.on_success=handle_response

# Sécurité et authentification JWT(Json web token) avec kivy:
import jwt
from kivy.storage.jsonstore import JsonStore
import websockets

class AutoManager:
    def __init__(self):
        self.store = JsonStore('auth.json')

    def save_token(self, token):
        try:
            decoded = jwt.decode(token, option={"verify_signature": False})
            self.store.put("auth", token=token, expires=decoded['exp'])
            return True
        except Exception as e:
            print("Erreur de token :", e)
            return False

    def get_token(self):
        if 'auth' in self.store:
            return self.store.get('auth')["token"]
        return None

    def is_authenticated(self):
        if 'auth' not in self.store:
            return False
        try:
            token = self.store.get('auth')['token']
            jwt.decode(token, options={'verify_signature':False})
            return True
        except:
            return True

# HTTPS et Validation SSL
import ssl
from kivy.network.urlrequest import UrlRequest

context = ssl.create_default_context()
context.check_hostname = True
context.verify_mode = ssl.CERT_REQUIRED

req = UrlRequest(
    url = "https://api.github.com/users/GameChangerDev",
    ca_file="/path/to/cert.pem",
    verify=True,
    timeout=30
)


                    # Optimisation des performances
# 1. Mise en cache des requêtes:
from functools import lru_cache

@lru_cache(maxsize=32)
def get_cached_data(url):
    return UrlRequest(url).result

# 2. Compression des données:
import zlib
from kivy.network.urlrequest import UrlRequest

def send_compressed(data):
    compressed = zlib.compress(data.encode())
    headers = {'Content-Encoding': 'deflate'}
    UrlRequest(
        url="https://api.github.com/users/GameChangerDev",
        req_body=compressed,
        req_headers=headers
    )

# Projet Pratique: Chat Application