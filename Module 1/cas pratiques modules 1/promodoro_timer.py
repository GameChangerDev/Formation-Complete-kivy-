# Projet : Pomodoro Timer Avancé avec Statistique

from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.properties import (
    NumericProperty,
    StringProperty,
    BooleanProperty,
    ListProperty,
    ObjectProperty
)
from kivy.config import Config
from kivy.graphics import Color, Rectangle
import json
from datetime import datetime


# Configuration initiale
Config.set("kivy", "exit_on_escape", "0")
if not Config.has_section("pomodoro"):
    Config.add_section("pomodoro")

class PomodoroEngine:
    """ Moteur de gestion du temps"""
    def __init__(self):
        self.session_count = 0
        self.history = []
        alert = r"C:\Users\DELL\Music\fally_ipupa\arsenal de belle mélodies\[musique.243stars.com]5e-race-by-Fally-ipupa.mp3"
        self.sound_alert = SoundLoader.load(alert)

    def start_session(self, duration, callback):
        """Démarre une session de travail"""
        self.session_start = datetime.now()
        self.duration = duration * 60 # Convertir en secondes
        self.callback = callback
        self.remaining = self.duration
        return Clock.schedule_interval(self.update, 1)


    def update(self, dt):
        """Met à jour le temps restant"""
        self.remaining -= 1
        if self.remaining <= 0:
            self.complete_session()
            return False
        return True

    def complete_session(self):
        """Termine la session avec succès"""
        self.session_count += 1
        session_end = datetime.now()
        self.history.append({
            "start": self.session_start.strftime("%Y-%m-%d %H:%M:%S"),
            'end': session_end.strftime("%Y-%m-%d %H:%M:%S"),
            'duration': self.duration
        })
        if self.sound_alert:
            self.sound_alert.play()
        self.callback(True)

    def get_stats(self):
        """Calcule les statistiques"""
        total_time = sum(s["duration"] for s in self.history) // 60
        today = datetime.now().strftime("%Y-%m-%d")
        today_sessions = sum(1 for s in self.history if s['start'].startswith(today))
        return total_time, today_sessions, len(self.history)

class PomodoroUI(BoxLayout):
    """Interface utilisateur principale"""
    # Propriétés des observables
    time_display = StringProperty("25:00")
    session_type = StringProperty("TRAVAIL")
    progress_value = NumericProperty(100)
    button_text = StringProperty("Démarrer")
    session_active = BooleanProperty(False)

    # Configurations
    work_duration = NumericProperty(25)
    break_duration = NumericProperty(5)
    long_break_duration = NumericProperty(15)
    sessions_before_long_break = NumericProperty(4)

    # Références
    timer = ObjectProperty(None)
    engine = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine = PomodoroEngine()
        self.load_config()
        self.update_display(self.work_duration * 60)

    def update_display(self, seconds):
        """Met à jour l'affichage du temps"""
        mins, secs = divmod(seconds, 60)
        self.time_display = f"{mins:02d}:{secs:02d}"
        self.progress_value = (seconds / (self.work_duration * 60)) * 100

    def toggle_session(self):
        """Démarre/Arrête une session """
        if self.session_active:
            self.stop_session()
        else:
            self.start_session()
        self.session_active = not self.session_active
        self.button_text = "Arrêter" if self.session_active else "Démarrer"

    def start_session(self):
        """Démarre une session de travail"""
        self.session_type = "TRAVAIL"
        duration = self.work_duration
        self.timer = self.engine.start_session(duration, self.session_completed)

    def start_break(self, long=False):
        """Démarre une pause"""
        self.session_type = "PAUSE LONGUE" if long else "PAUSE"
        duration = self.long_break_duration if long else self.break_duration
        self.timer = self.engine.start_session(duration, self.break_completed)

    def stop_session(self):
        """Arrête la session en cours"""
        if self.timer:
            Clock.unschedule(self.timer)
            self.timer = None

    def session_completed(self, succes):
        """Callback quand le travail est terminé"""
        self.session_active = False
        self.button_text = "Démarrer"

        # Détermine si c'est une longue pause
        total, today, all_sessions = self.engine.get_stats()
        long_break = all_sessions % self.sessions_before_long_break == 0

        self.start_break(long=long_break)


    def break_completed(self, sucesss):
        """Callback quand la pause est terminé"""
        self.session_active = False
        self.button_text = "Démarrer"
        self.update_display(self.work_duration * 60)

    def show_stats(self):
        """Affiche les statistiques"""
        total, today, all_sessions = self.engine.get_stats()

        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=f"Sessions complétées: {all_sessions}"))
        content.add_widget(Label(text=f"Temps total: {total}"))
        content.add_widget(Label(text=f"Sessions aujourd'hui: {today}"))

        popup = Popup(title='statistiques pomodoro', content=content, size_hint=(0.7, 0.4))

        content.add_widget(Button(text='Fermer', on_press=popup.dismiss))

        popup.open()

    def load_config(self):
        """Charge la configuration (kivy.config)"""
        defaults = {
            "work_duration": 20,
            'break_duration': 5,
            'long_break_duration': 15,
            'sessions_before_long_break': 4
        }

        for key, default in defaults.items():
            try:
                value = Config.getint('pomodoro', key)
                setattr(self, key, value)
            except:
                setattr(self, key, default)

    def save_config(self):
        """Sauvegarde la configuration (kivy.config)"""
        for key in ['work_duration', 'break_duration', 'long_break_duration', 'sessions_before_long_break']:
            Config.set('pomodoro', key, str(getattr(self, key)))
        Config.write()

class PomodoroApp(App):
    def build(self):
        """Application principale (kivy.base)"""
        Window.bind(on_request_close=self.on_exit)
        return PomodoroUI()

    def on_exit(self, *arg):
        """Sauvegarde à la fermeture"""
        self.root.save_config()
        self.stop()

if __name__ == '__main__':
    # Créer un son d'alerte
    PomodoroApp().run()