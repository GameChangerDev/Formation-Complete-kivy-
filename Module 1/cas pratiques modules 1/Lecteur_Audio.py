"""
    Projet : Métronome personnalisable avec Kivy
"""

#imports
from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.properties import (
    NumericProperty, BooleanProperty, StringProperty, ObjectProperty, ListProperty
)
from kivy.config import Config
from kivy.graphics import Color, Ellipse


# Configuration initiale
Config.set('kivy', 'exit_on_escape', '0')
if not Config.has_section("metronome"):
    Config.add_section('metronome')
    Config.setdefaults('metronome', {"bpm":"", "volume":"", "beats":""})

class MetronomeEngine:
    """Moteur audio du metronome (kivy.core.audio)"""
    def __init__(self):
        self.sound_beat = SoundLoader.load(r"C:\Users\DELL\Music\fally_ipupa\arsenal de belle mélodies\[musique.243stars.com]Orphelin-amoureux-by-Fally-ipupa.mp3")
        self.sound_accent = SoundLoader.load(r"C:\Users\DELL\Music\fally_ipupa\arsenal de belle mélodies\[musique.243stars.com]Orphelin-amoureux-by-Fally-ipupa.mp3")
        self.current_beat = 0

    def play_beat(self, beat_per_bar):
        self.current_beat = (self.current_beat % beat_per_bar) + 1
        sound = self.sound_accent if self.current_beat == 1 else self.sound_beat
        if sound:
            sound.volume = MetronomeApp.get_running_app().volume
            sound.play()

class VisualBeat(BoxLayout):
    """Widget visuel animé (kivy.clock)"""
    active = BooleanProperty(False)
    beat_color = ListProperty([0.1, 0.6, 1, 1])

    def on_active(self, _, value):
        self.beat_color = [1, 0.4, 0.2, 1] if value else [0.2, 0.6, 1, 1]

class MetronomeUI(BoxLayout):
    """Interface utilisateur principale"""
    bpm = NumericProperty(120)
    volume = NumericProperty(0.8)
    beats_per_bar = NumericProperty(4)
    is_playing = BooleanProperty(False)
    timer = ObjectProperty(None, allawnone=True)
    engine = ObjectProperty(None, allownone=True)
    visual_beats = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine = MetronomeEngine()
        self.load_config()
        self.build_visual_beats()

    def build_visual_beats(self):
        """Crée les indicateurs visuels de temps"""
        self.visual_beats = []
        for i in range(self.beats_per_bar):
            beat = VisualBeat()
            self.ids.visual_container.add_widget(beat)
            self.visual_beats.append(beat)

    def update_visual_beats(self):
        """Met à jour l'affichage visuel"""
        for i, visual in enumerate(self.visual_beats):
            visual.active = (i == self.beat_index)

    def on_beat_per_bar(self, _, value):
        """Adapte dynamiquement l'interface"""
        self.ids.visual_container.clear_widgets()
        self.visual_beats = []
        self.build_visual_beats()

    def toggle_play(self):
        """Démarre/ârrete le metronome (kivy.base)"""
        if self.is_playing:
            self.stop()
        else:
            self.start()
        self.is_playing = not self.is_playing

    def start(self):
        """Démarre le timer avec une précision optimale"""
        interval = 60.0 / self.bpm
        self.timer = Clock.schedule_interval(self.beat, interval)

    def stop(self):
        """Arrête le Metronome"""
        if self.timer:
            self.timer.cancel()# Annule les mises à jour répétées
            self.timer = None

        for beat in self.visual_beats:
            beat.active = False

    def beat(self, dt):
        """Gestion de chaque temps (kivy.clock)"""
        #self.engine.play_beat(self.beats_per_bar)
        #current_index = (self.engine.current_beat -1) % self.beats_per_bar
        self.beat_index = self.engine.play_beat(self.beats_per_bar, self.volume)
        self.update_visual_beats(self.beat_index)

    def update_bpm(self, value):
        """Ajuste dynamiquement le BPM"""
        self.bpm = int(value)
        if self.is_playing:
            self.stop()
            self.start()

    def load_config(self):
        """Charge la chofiguration (kivy.config)"""
        self.bpm = Config.getint("metronome", 'bpm')#, 120)
        self.volume = Config.getfloat('metronome', 'volume')#, 0.8)
        self.beats_per_bar = Config.getint("metronome", "beats")#, 4)

    def save_config(self):
        """Sauvegarde les paramètres (kivy.config)"""
        Config.set("metronome", 'bpm', str(self.bpm))
        Config.set("metronome", "volume", str(self.volume))
        Config.set("metronome", "beats", str(self.beats_per_bar))
        Config.write()

class MetronomeApp(App):
    """Application principale (kivy.base)"""
    def build(self):
        Window.bind(on_request_close=self.on_exit)
        return MetronomeUI()

    def on_exit(self, *args):
        """Sauvegarder la config à la fermeture"""
        self.root.save_config()
        self.stop()

if __name__ == '__main__':
    MetronomeApp().run()


