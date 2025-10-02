# 17. kivy.uix.video & kivy.core.video

from kivy.uix.video import Video

# voir grok apk et deepseek pour les descriptions

#1.
#2. Chargement et lecture basique
# Exemple minimal :
from kivy.app import App, runTouchApp
from kivy.uix.video import Video



class VideoApp(App):
    def build(self):
        video = Video(
            source = r"C:\Users\DELL\Videos\neil\.mp4",
            state='play',# 'play' 'pause' 'stop'
            options={'allow_stretch': True}
        )
        return video
#VideoApp().run()

#3. Contrôle Avancé de la lecture
# Manipuler la vidéo Dynamiquement :

class VideoController(Video):
    def toggle_playback(self):
        self.state = "pause" if self.state == 'play' else 'play'

    def seek(self, percent, precise=True):
        """Position en secondes"""
        self.position = percent

    def set_volume(self, volume):
        """Volume entre 0 et 1"""
        self.volume = volume
# Exemple d'utilisation pratique dans ecran kv
controller = VideoController(source=r"C:\Users\DELL\Videos\.mp4")
controller.toggle_playback()
controller.seek(120) # Aller à 2 minutes
controller.set_volume(0.5)
#runTouchApp(controller)

# 4. Gestion des événements : on_eos, on_load, on_position_change
video = Video(source=r"C:\Users\DELL\Videos\.mp4")

def on_video_end(instance):
    print("Fin de la vidéo ! Action personnalisée...")
    instance.state = 'stop'

video.bind(on_eos=on_video_end)
#runTouchApp(video)

# 5. Synchronisation avec interface Slider de Progression :

from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

class AdvancedVideoPlayer(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # widget vidéo
        self.video = Video(
            source=r"C:\Users\DELL\Videos\neil\.mp4",
            state='play',
            options={'fit_mode': 'contain'}
        )

        # Barre de progression
        self.progress = Slider(min=0, max=100, value=0)
        self.progress.bind(value=self.seek_video)

        # Contrôle de volume
        self.volume = Slider(min=0, max=100, value=0.5)
        self.volume.bind(on_press=self.toggle_play_pause)

        # Boutons
        play_pause_btn = Button(text="Play/Pause", size_hint=(1, 0.2))
        play_pause_btn.bind(on_press=self.toggle_play_pause)

        # Mise à jour de la barre de progression
        Clock.schedule_interval(self.update_progress, 0.5)

        layout.add_widget(self.video)
        layout.add_widget(self.progress)
        layout.add_widget(self.volume)
        layout.add_widget(play_pause_btn)
        return layout

    def toggle_play_pause(self, instance):
        if self.video.state == "play":
            self.video.state = "pause"
        else:
            self.video.state = 'play'

    def update_progress(self, dt):
        if self.video.duration > 0:
            # Mettre à jour la barre de progression
            self.progress.max = self.video.duration
            print(self.video.duration)
            self.progress.value = self.video.position
            print(self.video.position)

    def seek_video(self, instance, value):
        if self.video.duration > 0:
            print(value / self.video.duration)
            self.video.seek(value / self.video.duration)

    def set_volume(self, instance, value):
        self.video.volume = value

#AdvancedVideoPlayer().run()

#  5. Utilisation du KvLang pour unr interface propre
# exemple : Lecteur Vidéo avec KvLang
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class VideoPlayer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.ids)

    def toggle_play_pause(self):
        if self.ids.video.state == 'play':
            self.ids.video.state = 'pause'
            self.ids.play_pause_btn.text = 'Play'
        else:
            self.ids.video.state = 'play'
            self.ids.play_pause_btn.text = 'Pause'
    def update_progress(self, dt):
        if self.ids.video.duration > 0:
            self.ids.progress.max = self.ids.video.duration
            self.ids.progress.value = self.ids.video.position

    def seek_video(self,value):
        if self.ids.video.duration > 0:
            self.ids.video.seek(value / self.ids.video.duration)

    def set_volume(self, value):
        self.ids.video.volume = value

class VideoPlayerApp(App):
    def build(self):
        player = VideoPlayer()
        Clock.schedule_interval(player.update_progress, 0.5)
        return player

#VideoPlayerApp().run()

# 6. Gestion des événements
# Exemple : Gestion d'érreur
from kivy.uix.label import Label

class VideoEventsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.percent = 0

        self.video = Video(source=r'C:\Users\DELL\Videos\neil\.mp4', state='play')
        self.status_label = Label(text="Status: Playing")

        # Lier les événements
        self.video.bind(on_eos=self.on_video_end)
        self.video.bind(on_load=self.on_video_load)
        self.video.bind(on_error=self.on_video_error)

        layout.add_widget(self.video)
        layout.add_widget(self.status_label)

        return layout

    def on_video_end(self, insatance):
        self.status_label.text = 'Status: Video End'
        self.video.state = 'stop'
        self.video.seek(0)  # Revenir au debut

    def on_video_load(self, insatance):
        self.status_label.text = 'Status: Video ended'

    def on_video_error(self, insatnce, error):
        self.status_label.text = f"Status: Error - {error}"

#VideoEventsApp().run()

# 7. Lecture de flux vidéo (Streaming)
# Exemple : Lecture d'un flux vidéo

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class VideoStreamApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        # URL de flux vidéo(exemple, utiliser une URL valide)
        self.video = Video(
            source='https:youtube.com/franklin',
            state='play'
        )
        
        play_pause_btn = Button(text='play', size_hint=(1, 0.2))
        play_pause_btn.bind(on_press=self.toggle_play_pause)
        
        layout.add_widget(self.video)
        layout.add_widget(play_pause_btn)
        
        return layout
    
    def toggle_play_pause(self, instance):
        if self.video.state == 'play':
            self.video.state = 'pause'
        else:
            self.video.state = 'play'

#VideoStreamApp().run()

# 8. Technique avancées
# 8.1 Synchronisation avec d'autres widgets

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivy.uix.label import Label
from kivy.clock import Clock

class VideoSubtitlesApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.video = Video(source=r'C:\Users\DELL\Videos\neil\Neil_Cruz_electricien(240p).mp4', state='play')
        self.subtitle_label = Label(text="", size_hint=(1, 0.2))

        # Exemple de sous-titres  (dictionnaire {temps: texte}
        self.subtitles = {
            2.0: "Bonjour, ceci c'est un sous-titre",
            5.0: "La vidéo continue",
            10.0: "Fin des sous-titres"
        }

        Clock.schedule_interval(self.update_subtitles, 0.1)

        layout.add_widget(self.video)
        layout.add_widget(self.subtitle_label)

        return layout

    def update_subtitles(self, dt):
        current_time = self.video.position
        for time, text in self.subtitles.items():
            if abs(current_time - time) < 0.2:
                self.subtitle_label.text = text
                break
            else:
                self.subtitle_label.text = ''

#VideoSubtitlesApp().run()

# 8.2 Effets visuels sur la vidéo
# Exemple: Appliquer un éffet de flou
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivy.uix.effectwidget import EffectWidget, FXAAEffect, VerticalBlurEffect, HorizontalBlurEffect, ChannelMixEffect

class VideoEffectApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Appliquer un effet de flou
        effect_widget = EffectWidget()
        effect_widget.effects = [FXAAEffect(), VerticalBlurEffect(), HorizontalBlurEffect() , ChannelMixEffect()]

        self.video = Video(source=r"C:\Users\DELL\Downloads\L'UNIVERS est-il infini  _.mp4", state='play')
        effect_widget.add_widget(self.video)

        layout.add_widget(effect_widget)

        return layout

#VideoEffectApp().run()

# 9. Bonnes Pratiques et Optimisation
#   --------------  Voir sur grok apk et deepseek   ------------------------------

# 10. projet final : Lecteur vidéo Complet

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.textinput import TextInput

class VideoPlayerExo(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        # Exemple de sous-titres synchronisés (temps en seconde : texte)
        self.subtitles = {
            2.0: "Bienvenue dans le lecteur vidéo !",
            5.0: "Contrôlez la Lecture avec les boutons.",
            10.0: "Fin de la Démonstration."
        }
        self.create_ui()    # Appel pour Contruire l'interface utilisateur

    def create_ui(self):
        # Widget video
        self.video = Video(
            source=r"C:\Users\DELL\Downloads\L'UNIVERS est-il infini  _.mp4",
            state='play',
            options={'fit_mode': 'contain'} # Ajuste la vidéo au contenu
        )
        self.add_widget(self.video)

        # Slider pour la progression
        self.progress = Slider(min=0, max=100, value=0)
        self.progress.bind(value=self.seek_video) # Lier le déplacement dans la vidéo
        self.add_widget(self.progress)

        # Slider pour le volume
        self.volume = Slider(min=0, max=1, value=0.5) # Volume initial à 50%
        self.volume.bind(value=self.set_volume) # Lier au controle du volume
        self.add_widget(self.volume)

        # Label pour les sous-titres
        self.subtitle_label = Label(text='', size_hint=(1, 0.2), font_size=20)
        self.add_widget(self.subtitle_label)

        # Labekl pour le status
        self.status_label = Label(text='Status: Playing', size_hint=(1, 0.1))
        self.add_widget(self.status_label)

        # Le bouton Play/Pause
        self.play_pause_btn = Button(text='Pause', size_hint=(1, 0.2))
        self.play_pause_btn.bind(on_press=self.toggle_play_pause) # Lier le basculement
        self.add_widget(self.play_pause_btn)

        # Lier les événements de la vidéo
        self.video.bind(on_eos=self.on_video_end)   # Fin de la vidéo
        self.video.bind(on_load=self.on_video_load)   # vidéo chargée
        self.video.bind(on_error=self.on_video_error)   # Erreur

        # Mettre à jour la progressionet les sous-titres toutes les 0.1 secondes
        Clock.schedule_interval(self.update_progress, 0.1)

    def toggle_play_pause(self, instance):
        """Bascule entre Play et Pause."""
        if self.video.state == 'play':
            self.video.state = 'pause'
            self.play_pause_btn.text = 'Play'
            self.status_label.text = 'Status: Paused'
        else:
            self.video.state = 'play'
            self.play_pause_btn.text = 'Pause'
            self.status_label.text = 'Status: Playing'

    def update_progress(self, dt):
        """Met à jour la progression et les sous-titres."""
        if self.video.duration > 0: # Vérifie que la vidéo est chargée
            self.progress.max = self.video.duration
            self.progress.value = self.video.position
            self.update_subtitles()

    def update_subtitles(self):
        """Affiche les sous-titres en fonction du temps actuel."""
        current_time = self.video.position
        for time, text in self.subtitles.items():
            if abs(current_time - time) < 0.2: # Tolérance de 0.2s
                self.subtitle_label.text = text
                break
            else:
                self.subtitle_label.text = ''   # efface et aucun sous-titre ne correspond
    def seek_video(self, instance, value):
        """Déplace la vidéo à la position indiqué par le slider."""
        if self.video.duration > 0:
            self.video.seek(value / self.video.duration)

    def set_volume(self, instance, value):
        """Ajuste le volume de la vidéo"""
        self.video.volume = value

    def on_video_end(self, instance):
        """Gère la fin de la vidéo"""
        self.status_label.text = "Status: Vidéo ended"
        self.video.state = 'stop'
        self.video.seek(0)  # Reviens au debut
        self.play_pause_btn.text = 'Play'

    def on_video_load(self, instance):
        """Confirme le chargement de la video"""
        self.status_label.text = 'Status: Vidéo loaded'

    def on_video_error(self, instance, error):
        """Affiche les erreurs éventuelles."""
        self.status_label.text = f"Statut: Error - {error}"

class VideoPlayerExoApp(App):
    def build(self):
        return VideoPlayerExo()

if __name__ == '__main__':
    VideoPlayerExoApp().run()