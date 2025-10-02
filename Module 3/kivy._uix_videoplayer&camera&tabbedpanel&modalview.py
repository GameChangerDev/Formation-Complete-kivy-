
# kivy.uix.videoplayer

from kivy.uix.videoplayer import VideoPlayer
import os
from kivy.base import runTouchApp

url = os.path.join(r"C:\Users\DELL\Videos\FORMATION DE TRADING ICT & SMC", "COMPRENDRE LES ANNONCES ÉCONOMIQUES EN TRADING (comme un pro).mp4")

def on_fullscreen(inst, v):
    print(v)

video = VideoPlayer(source=url)
video.bind(on_fullscreen=on_fullscreen)

#runTouchApp(video)
# Exercice : Transformer une ProgressBar simple en ProgressBar manipulable
from kivy.uix.progressbar import ProgressBar

class Progess(ProgressBar):
    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return
        touch.grab(self)
        return True

    def on_touch_move(self, touch):
        if touch.grab_current is not self:
            return
        self.value_(touch.x)
        return True

    def value_(self, x):
        pos_x = max(self.x, min(self.right, x)) - self.x
        self.value = pos_x/self.width
        video.seek(self.value)
        print(self.value)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            print(self.right, self.pos, touch.pos)

barre = Progess(max=1, value=video.position/video.duration)

def position(inst, v):
    barre.value=v/video.duration

def touch(inst, t):
    video.state='play'

barre.bind(on_touch_down=touch)
video.bind(position=position)
video.play = True

#runTouchApp(barre)

#                                                   kivy.uix.Camera
# from kivy.uix.camera import Camera
# from kivy.uix.image import Image
#
# cam = Camera(resolution=(320,240), index=0)# camera avec une resolution, index 0 pour la camera arrière
# cam.play = True
# runTouchApp(cam)

# pour gérer les permissions sur Android
# from android.permission import request_permission, Permission
#
# # demander les permissions Android
# def request_android_permisions():
#     request_permission([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE])

# 4. Capture et Traitement d'images
from kivy.core.image import Image as CoreImage
from io import BytesIO

def capture_image(camera_instance):
    # Capturer l'image
    texture = camera_instance.texture

    # Créer une image à partir de texture
    buf = BytesIO()
    texture.save(buf, flipped=True)
    buf.seek(0)

    # Créer une image kivy
    core_img = CoreImage(BytesIO(buf.read()), ext="png")

    return core_img

# intégration avec OpenCV
import cv2
import numpy as np
from kivy.graphics.texture import Texture

def process_with_opencv(camera_instance):
    # Convertir la texture kivy en image OpenCV
    texture = camera_instance.texture
    size = texture.size
    pixels = texture.pixels

    # Créer un array numpy
    image = np.frombuffer(pixels, dtype=np.uint8)
    image = image.reshape((size[1], size[0], 4))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Traitement OpenCV (exemple: traitement en niveau de gris)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Reconversion en texture kivy
    buf = gray.tobytes()
    texture = Texture.create(size=(size[0], size[1]), colorfmt="luminance")
    texture.blit_buffer(buf, colorfmt='luminance', bufferfmt='ubyte')

    return texture

# après avoir rencontrer des problèmes de connexion à la caméra état donner que le desktop n'en possède pas,
# on peut exécuter le code du fichier test_camera.py dans le terminal pour verifier si opnenCV(cv2) est fonctionnel


#                                               TabbedPannel
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelItem

# 2. Configuration avancée :

# Types de positionnement des onglets
# dans le fichier .kv
"""
<TabbedPanel>:
    tab_pos: "top_left" # Options de positionnement
    tab_width: 150
    do_default_tab: False
"""

# Personnalisation de l'apparence
# Personnalisation via le langage KV
"""
<TabbedPanel>:
    background_color: 0.8, 0.8, 0.8, 1
    border: [10, 10, 10, 10]
    tap_height: 40

<TabbedPanelHeader>:
    background_normal: 'tab_normal.png'
    background_down: 'tab_active.png'
    font_size: 16
    color: 0, 0, 0, 1
"""

# 3. Gestion dynamique des onglets
# Ajout/suppression onglets
def add_dynamic_tab(self):
    # Création d'un nouvel onglet
    from kivy.uix.label import Label
    new_tab = TabbedPanelItem(text="Nouvel onglet")
    new_tab.add_widget(Label(text="Contenu du nouvel onglet"))
    self.ids.tab_panel.add_widget(new_tab)

def remove_tab(self, tab):
    self.ids.tab_panel.remove_widget(tab)

# Navigation programatique
# passer à un onglet spécifique
def switch_to_tab(self, index):
    self.ids.tab_panel.switch_to(self.ids.tab_panel.tab_list[index])

# 4. Communication entre onglets
# Partage de données
from kivy.event import EventDispatcher
from kivy.properties import DictProperty
class SharedData(EventDispatcher):
    data = DictProperty({})
    def __init__(self, **kwargs):
        super(SharedData, self).__init__(**kwargs)
        self.register_event_type("on_data_change")

    def update_data(self, key, value):
        self.data[key] = value
        self.dispatch('on_data_change')

    def on_data_change(self):
        pass

# Personnalisation avancée
# Création d'un TabbedPanel personnalisé
class CustomTabbedPanel(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(current_tab=self.on_tab_switch)

    def on_tab_switch(self, instance, value):
        print(f"Onglet changé: {value}")

# Exercice:
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

tp = TabbedPanel(spacing=10)
tp.do_default_tab = False
tp.default_tab_text = "entête"
th = TabbedPanelHeader(text="entête 1")
th.background_color = (1, 0, 1, 0.5)

box = BoxLayout()
box.orientation="vertical"
for i in range(10):
    th = TabbedPanelHeader(text=f"entête {i+1}")
    th.content = box
    box.add_widget(Button(text=f"bouton: {i+1}"))
    tp.add_widget(th)

tp.bar_width = 2
tp.set_def_tab(tp.tab_list[0])# définir un onglet par défault

tp.add_widget(th)
runTouchApp(tp)


#                                           kivy.uix.modalview
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

# 1. Exemple + exercice
#   , 2., 3., 4.
view = ModalView(size_hint=(0.6, 0.6), overlay_color=[0.2, 0.2, 0.2, 0.3])
content = BoxLayout(orientation='vertical', spacing='25dp')
btn= Button(text="bonjour, envoyez")
label = Label(text='Bienvenue', font_size='35sp')

content.add_widget(label)
content.add_widget(btn)
view.add_widget(content)

def on_open(*args):
    print("vue modulaire ouverte")
def on_dismiss(*args):
    print("vue modulaire fermée")

btn.bind(on_press=view.dismiss)
view.bind(on_open=on_open)
view.bind(on_dismiss=on_dismiss)

view.open()
runTouchApp()

