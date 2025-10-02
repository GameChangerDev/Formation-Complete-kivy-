"""Voir Grok pour les descriptions des classes ou fonctions || propriétés"""

#classe/Fonctions
"""
Clock
Clock.schedule_once
Clock.schedule_interval
Clock.unschedule
Clock.create_trigger
Clock_base
"""
from kivy import clock
help(clock)

# Classe Clock ||   kivy.clock.Clock
# propriétés principales : time =retourne le temps actuel(via time.time), °frames, °frametime
#from kivy.clock import Clock
#help(Clock)
# méthodes principales:
"""voir grok"""

# Exemple 1 : Planification unique avec schedule_once
# voici un exemple simple qui mets à jour un label après un delai de 2 secondes.
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class ClockApp(App):
    def build(self):
        self.label = Label(text="Attendez 2 secondes")
        Clock.schedule_once(self.update_label, 2) # Exécuté après 2 secondes
        return self.label

    def update_label(self, dt):# dt: qui est le delta time(paramètre obligatoire) la variation du temps
        self.label.text = "Texte mis à jour !"# nouveau text du self.label après le delai

if __name__ == '__main__':
    ClockApp().run()

# Exemple 2 : Mise à jour répétée avec schedule_interval
#cette exemple Crée un compteur qui s'incrémente toute les secondes.
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class CounterApp(App):
    def build(self):
        self.count = 0
        self.label = Label(text="compteur : 0")
        Clock.schedule_interval(self.update_counter, 1)
        return self.label

    def update_counter(self, dt):
        self.count += 1# incrémentation du compteur
        self.label.text = f"compteur : {self.count}"
        if self.count == 5:
            print("limite atteinte, arrêt du compteur !!!")
            return False  #lorsque la fonction qui est mise à jour retourne False la mise à jour répétée s'arrête

if __name__ == '__main__':
    CounterApp().run()

# exemple 3 : utilisation de create_trigger
# cette exemple montre comment utilisé un déclencheur pour synchroniser une action avec le rendu

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class TriggerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='En Attente...')
        btn = Button(text="Déclencher")
        self.trigger = Clock.create_trigger(self.update_label)
        btn.bind(on_press=self.on_button_press)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_button_press(self, instance):
        self.trigger() #Déclencher manuellement

    def update_label(self, dt):
        self.label.text = "Déclenché !" # Déclencher manuellement

if __name__ == '__main__':
    TriggerApp().run()


# Exemple 4 : Annulation de planification avec unschedule
# cette exemple montre comment arrêter une mise à jour répétée.

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class StopLockApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.count  = 0
        self.label = Label(text='compteur : 0')
        self.button = Button(text='Arreter')
        self.button.bind(on_press=self.stop_counter)
        Clock.schedule_interval(self.update_counter, 1)
        layout.add_widget(self.label)
        layout.add_widget(self.button)
        return layout

    def update_counter(self, dt):
        self.count += 1
        self.label.text = f"compteur : {self.count}"

    def stop_counter(self, instance):
        Clock.unschedule(self.update_counter)
        self.label.text = f"compteur arrêté ! \nle compteur est allé jusqu'a : {self.count}"

if __name__ == '__main__':
    StopLockApp().run()