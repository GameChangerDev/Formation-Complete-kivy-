#1. Concepts de Base
# # voir dans deepseek et code source

#2. kivy.uix.slider
# Exemple 1 : Slider Basique
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label


class SliderApp(App):
    def build(self):
        slider = Slider(
            min=0,
            max=100,
            value=50,
            step=5,
            orientation='horizontal'
        )
        slider.bind(value=self.on_value_change)
        return slider

    def on_value_change(self, instance, value):
        print(f"Slider value: {value}")


# Exemple 2 : Slider avec Affichage personnalisé

class SliderWithLabel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.label = Label(text="Value: 50")
        self.add_widget(self.label)

        self.slider = Slider(min=0, max=100, value=50)
        self.slider.bind(value=self.update_label)
        self.add_widget(self.slider)

    def update_label(self, instance, value):
        self.label.text = f"Value: {int(value)}"

class CustumApp(App):
    def build(self):
        return SliderWithLabel()

if __name__ == '__main__':
    CustumApp().run()

#3. kivy.uix.progressbar
# Exemple 3: ProgressBar Simple

from kivy.uix.progressbar import ProgressBar
class ProgressBarApp(App):
    def build(self):
        return ProgressBar(value=75, max=100)



#Exemple 4: ProgressBar animée (Simulmation de chargement)

from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

class AnimatedProgressBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.progress = ProgressBar(max=100)
        self.add_widget(self.progress)

        Clock.schedule_interval(self.update_progress, 0.1)

    def update_progress(self, dt):
        if self.progress.value < 100:
            self.progress.value += 2
        else:
            self.progress.value = 0

class LoadingApp(App):
    def build(self):
        return AnimatedProgressBar()

if __name__ == '__main__':
    LoadingApp().run()

# 4. Intégration Slider + ProgressBar
class IntegratedWidgets(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50

        # Création de la ProgressBar
        self.progress_bar = ProgressBar(max=100)
        self.add_widget(self.progress_bar)

        # Création du Slider
        self.slider = Slider(min=0, max=100, cursor_image=r"C:\Users\DELL\PycharmProjects\kivy_apprentissage\Module 1\kivy_core\png_boutons\FERME.png")
        self.slider.bind(value=self.update_progress)
        self.add_widget(self.slider)

    def update_progress(self, instance, value):
        self.progress_bar.value = value

class IntegrationApp(App):
    def build(self):
        return IntegratedWidgets()

if __name__ == '__main__':
    IntegrationApp().run()

# 5. Personnalisation Avancée
# Personnalisatiobn du Slider:
Slider(
    background_horizontal="Slider_bg.png",
    background_vertical='slider_vert_bg.png',
    cursor_image='cursor.png'
)
# Personnalisation de la ProgressBar :
ProgressBar(
    background_color=(0.2, 0.2, 0.2, 1),
    color=(0.8, 0.2, 0.2, 1)
)

#6. Bonnes Pratique
# # voir dans deepseek

# 7. Cas d'usage Courant
