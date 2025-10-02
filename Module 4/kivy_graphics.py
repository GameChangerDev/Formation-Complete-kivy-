# 1. introduction
# voir deepssek pour les détails et twitter/Grok
from kivy.graphics import Canvas, Rectangle, Color
from kivy.uix.widget import Widget
from kivy.app import runTouchApp

class CustumWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0, 1) # RGBA
            Rectangle(pos=(0, 0), size=(100, 100))

#runTouchApp(CustumWidget())

# 2. intructions graphiques Avancées
# a) Mesh : Contrôle pixel-perfect, créez des formes complexes avec des vertices personnalisés.
from kivy.graphics import Mesh

vertices = [
    0, 0, 0, 0, # x, y, u, v
    100, 0, 1, 0,
    100, 100, 1, 1,
    #0, 100, 0, 1
]
indices = [0, 1, 2, 0, 2, 3] # Triangles
class Dessin(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            print("effectué")
            Mesh(vertices=vertices, indices=indices, mode='triangles')

#runTouchApp(Dessin())

# b) Bezier et Ellipse de précision Courbes paramétriques et ellipses avec contrôle des segments.
from kivy.graphics import Bezier, Ellipse
class ExempleBezier(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # Courbe de Bézier
            Bezier(points=[0,100, 50,50, 200,12, 200,600], segments=4160)
            # Ellipse avec 100 segments
            Ellipse(pos=(200, 200), size=(150, 80), segments=100)
#runTouchApp(ExempleBezier())

# c) stencilPop et StencilPush Dessiner des masques complexes

from kivy.graphics import StencilPop, StencilPush, StencilUse
class Masques(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        StencilPush()
        Color(1, 0, 0)
        Rectangle(pos=(0, 0), size=(100, 100))
        StencilUse()
        Color(1, 0, 0, 1)
        Ellipse(pos=(100, 100), size=(200, 200))
        StencilPop()
#runTouchApp(Masques())


# 3. inscructions graphiques principales
# Rectangle, Ellipse, Line, Triangle, Mesh, Bezier
# exemple : Dessiner plusieurs formes
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Ellipse, Line

class ShapesWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # Rectangle rouge
            Color(1, 0, 0, 1)
            Rectangle(pos=(100, 100), size=(200, 150))

            # Cercle bleu
            Color(0, 0, 1, 1)
            Ellipse(pos=(350, 100), size=(100, 100))

            # Ligne verte
            Color(0, 1, 0, 1)
            Line(points=[100,300, 300,400, 400,300], width=2)

class ShapesApp(App):
    def build(self):
        return ShapesWidget()
"""
if __name__ == '__main__':
    ShapesApp().run()
"""
# 3.2. Context instructions
# Color(r, g, b, a), Translate(x, y), Rotate(angle, x, y), Scale(sx, sy), PushMatrix et PopMatrix
# Exemple : Tranformations
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, PushMatrix, PopMatrix, Rotate, Translate, Scale

class TransformationWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            PushMatrix()
            # Déplacer le canevas
            Translate(200, 200)
            # Rotation de 45 degrés
            Rotate(angle=45, origin=(0, 0))
            #Scale(2, 2)
            # Dessiner un Rectangle
            Color(1, 0, 0, 1)
            Rectangle(pos=(-50, -50), size=(100, 100))
            PopMatrix()

class TransformationApp(App):
    def build(self):
        return TransformationWidget()
"""
if __name__ == '__main__':
    TransformationApp().run()
"""

# Exemple : Matrices personnalisées, Utilisez Matrix pour des transformations complexes
from kivy.graphics import MatrixInstruction
from kivy.graphics.transformation import Matrix

mat = Matrix().scale(3, 3, 1).rotate(45, 0, 0, 1)
class CustomMatrix(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            MatrixInstruction(matrix=mat)
            Rectangle(pos=(100, 100), size=(50, 50))

#runTouchApp(CustomMatrix())

# 4. Animation avec kivy.graphics
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.properties import NumericProperty
from kivy.clock import Clock

class AnimatedWidget(Widget):
    rect_x = NumericProperty(100)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rect = None
        with self.canvas:
            Color(1, 0, 0, 1)
            self.rect = Rectangle(pos=(self.rect_x, 100), size=(100, 100))
        Clock.schedule_interval(self.update, 1/60)

    def update(self, dt):
        self.rect_x += 2
        if self.rect_x > self.width -100:
            self.rect_x = 100
        self.rect.pos = (self.rect_x, 100)
    def on_touch_down(self, widget):
        Clock.schedule_interval(self.echelle, 1/60)

    def echelle(self, dt):
        width, height = self.rect.size
        width -= 1
        height -= 1
        if width < 5:
            width = 100
            height = 100
        self.rect.size = (width, height)

#runTouchApp(AnimatedWidget())
class AnimatedApp(App):
    def build(self):
        return AnimatedWidget()
"""
if __name__ == '__main__':
    AnimatedApp().run()
"""

# 5. gestion des textures
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.graphics.texture import Texture  # permet de travailler avec les textures
# a)Exemple : Utilisation d'une texture
class TextureWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Créer une texture 100x100
        texture = Texture.create(size=(100, 100))# Crée une texture vide.
        # Remplir la texture avec des pixels rouges
        pixels = b'\xff\x00\x00\xff' * 100 *100 # RGBA
        texture.blit_buffer(pixels, colorfmt='rgba', bufferfmt='ubyte')# remplir la texture avec des données de pixels

        with self.canvas:
            Color(1, 1, 1, 1)
            Rectangle(texture=texture, pos=(100, 100), size=(100, 100))

class TextureApp(App):
    def build(self):
        return TextureWidget()

#TextureApp().run()

# b) Textures dynamiques, mise à jour en temps réel avec texture.create()
"""
texture = Texture.create(size=(512, 512))
texture.blit_buffer(b'\xff\x00\x00\xff', colorfmt='rgba', bufferfmt='ubyte')

# Mise à jour dynamique
def update_texture(dt):
    new_data = b'\xff\x00\x00\xff'*100
    texture.blit_buffer(new_data, colorfmt='rgba', bufferfmt='ubyte')
Clock.schedule_interval(update_texture, 1/30.)
"""
# 6. Utilisation avancé : FBO (Frame Buffer Object)
#a) Exemple rendu dans un FBO

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Fbo, ClearColor, ClearBuffers

class FboWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Créer un Fbo
        self.fbo = Fbo(size=(200, 200))
        with self.fbo:
            ClearColor(0, 0, 0,1)
            ClearBuffers()
            Color(1, 0, 0, 1)
            Rectangle(pos=(0, 0), size=(100, 100))

        with self.canvas:
            Color(1, 1, 1, 1)
            Rectangle(texture=self.fbo.texture, pos=(100, 100), size=(200, 200))

class FboApp(App):
    def build(self):
        return FboWidget()
#FboApp().run()

#b). Créer des textures de rendu intermédiaires pour les effets complexes
from kivy.graphics import Fbo, Color, Rectangle
"""
# Création d'un FBO
fbo = Fbo(size=(800, 600))

# Dessiner dans le FBO
with fbo:
    Color(0, 0, 1, 1)# Bleu
    Rectangle(size=fbo.size)# Remplir le FBO

# Utilisation du FBO comme texture
class FboExample(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # Afficher le contenu du Fbo
            Rectangle(texture=fbo.texture, size=self.size)

    def on_size(self, *args):
        self.canvas.clear()
        with self.canvas:
            Rectangle(texture=fbo.texture, size=self.size)
class Fbo2App(App):
    def build(self):
        return FboExample()
#if __name__ == '__main__':
    #Fbo2App().run()
"""
# c) Cas d'Usage Avancé : Effets en chaîne avec Multi-FBO
from kivy.graphics import Fbo, Color, Rectangle, ClearColor, ClearBuffers
"""
# Création de 2 FBOs
class WidgetEx(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fbo1 = Fbo(size=(800, 600))
        self.fbo2 = Fbo(size=(800, 600))

        # premier rendu dans fbo1
        with self.fbo1:
            ClearColor(0, 0, 0, 1) # Fond noir
            ClearBuffers()
            Color(1, 0, 0, 1)
            Rectangle(pos=(100, 100), size=(200, 200))


        # Appliquer un effet dans fbo2 en utilisant fbo1 comme source
        with self.fbo2:
            ClearColor(0, 0, 0, 0) # transparent
            ClearBuffers()
            # Ici vous pourrez utiliser un shader personnalisé
            Color(1, 1, 1, 0.5)
            Rectangle(texture=self.fbo1.texture, size=self.fbo1.size)


        # utilisation finale
        with self.canvas:
            Rectangle(texture=self.fbo2.texture, size=self.fbo2.size)

runTouchApp(WidgetEx())

# Fonctionnalités Clés des FBOs:
#1. Mise à jour Dynamique:
def update_fbo(dt):
    with fbo:
        ClearBuffers()
        # Redessiner le contenu
        Color(random(), random(), random(), random())
        Rectangle(pos=(random()*500, random()*500), size=(100, 100))

Clock.schedule_interval(update_fbo, 1/30)
#2. Capture d'Ecran :
fbo = Fbo(size=self.size)
self.export_to_png = fbo.texture.save('screenshot.png')
#3. Optimisation des performances :
# Recycler les FBOs existants au lieu d'en créer de nouveau
if not hasattr(self, "_fbo"):
    self._fbo = Fbo(size=self.size)
else:
    self._fbo.size = self.size
"""
# 6. Shader Personnalisés (GLSL)
class ShaderWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shader_source = """
        $HEADER
        uniform float time;
        void main(void) {
            vec2 shifted_pos = vec2(vPosition.x + sin(time), vPosition.y);
            gl_Position = vec4(shifted_pos, 0.0, 1.0);
        }
        """
        self.fbo = Fbo(size=self.size)
        self.fbo.shader.fs = self.shader_source # Fragment shader
        self.uniforms = {'time': 0.0}

        with self.fbo:
            Color(1, 1, 1)
            Rectangle(size=self.size)

        with self.canvas:
            Rectangle(texture=self.fbo.texture, size=self.size)
runTouchApp(ShaderWidget())


# 7. Optimisation et bonnes pratiques

#+ Utilisation de kvlang
"""
<MyWidget>:
    canvas:
        Color:
            rgba: 1, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
"""

#8.  Projet pratique : Dessin intéractif
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line

class DrawWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_line = None

    def on_touch_down(self, touch):
        with self.canvas:
            color = Color(1, 1, 0, 1) # Jaune
            self.current_line = Line(points=[touch.x, touch.y], width=2)

    def on_touch_move(self, touch):
        self.current_line.points += [touch.x, touch.y]

class DrawApp(App):
    def build(self):
        return DrawWidget()

DrawApp().run()

# 9. Ressources supplementaire

# 10. Exercices




"""
package content:
    boxshadow
    buffer
    cgl
    cgl_backend (package)
    compiler
    context
    context_instructions
    fbo
    gl_instructions
    instructions
    opengl
    opengl_utils
    scissor_instructions
    shader
    stencil_instructions
    svg
    tesselator
    texture
    transformation
    vbo
    vertex
    vertex_instructions
"""