# Formation kivy.uix.filechooser
# les Desciptions sont dans le code sources, deepseek, ou grok apk

from kivy.uix.filechooser import FileChooser, FileChooserListLayout, FileChooserIconLayout, FileChooserIconView, FileChooserListView
from kivy.app import runTouchApp
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class ChooserApp(App):
    def build(self):
        box = BoxLayout(orientation="vertical")
        btn_choose = Button(text="Explorateur", size_hint_y=0.1)

        self.filechooser = FileChooserListView()
        self.filechooser.path = r"C:\Users\DELL\Music\fally_ipupa"# Mofifier le chemin d'ouverture par defaut
        self.filechooser.multiselect = False
        # Personnalisation avec Filtres personnalisés, les filtres vonts au delà des simples motifs et peuvent utiliser
        # des fonctions de callbacks
        self.filechooser.filters = [self.image_filtrer]
        self.filechooser.bind(on_submit=self.on_submit)
        box_chooser = BoxLayout(orientation="vertical")
        btn_submit = Button(text="Submit", size_hint=(1, 0.1))
        btn_submit.bind(on_press=self.fermer_popup)

        box_chooser.add_widget(self.filechooser)
        box_chooser.add_widget(btn_submit)

        self.popup = Popup(size_hint=(0.3, 0.7))
        self.popup.title = "Selectionner un Fichier"
        self.popup.content = box_chooser
        btn_choose.bind(on_press=self.popup.open)

        box.add_widget(btn_choose)
        return box

    def fermer_popup(self, *args):
        self.popup.dismiss()
        print(f"fichier selectionner : {self.filechooser.selection}")

    def image_filtrer(self, folder, filename):
        # Vérifier par l'extension et le contenue réel si possible
        ext = filename.lower().split('.')[-1]
        return ext in ['png', 'jpg', 'gif', 'bmp', "mp3"]

    def on_submit(self, inst, selected, touch):
        print(f"selection : {selected}")
        self.popup.dismiss()

ChooserApp().run()

