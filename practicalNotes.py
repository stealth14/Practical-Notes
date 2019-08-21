import kivy

from kivy.app import App

from kivy.uix.label import Label

from kivy.uix.button import Button

from kivy.core.window import Window

import datetime

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.gridlayout import GridLayout

from kivy.uix.stacklayout import StackLayout

from kivy.uix.textinput import TextInput

from kivy.uix.popup import Popup

from kivy.graphics import Color

from kivy.uix.pagelayout import PageLayout

#builder
from kivy.lang import Builder

#tabed panel
from kivy.uix.tabbedpanel import TabbedPanel

#screen manager
from kivy.uix.screenmanager import ScreenManager, Screen

#transicion
from kivy.uix.screenmanager import SwapTransition

from kivy.uix.screenmanager import FadeTransition
#tabbed panel
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader

#scrollview
from kivy.uix.scrollview import ScrollView

#efectos
from kivy.uix.effectwidget import  EffectWidget
from kivy.uix.effectwidget import HorizontalBlurEffect
from kivy.uix.effectwidget import VerticalBlurEffect

#detector de eventos - se usara para crear efectos personalizados

kivy.require('1.9.1')

Window.clearcolor = (0, 0.2, 0.4,1)

#home 
home = GridLayout(cols=3,spacing=[10,10],padding=[10,10])
home.orientation = 'vertical'

#libreria
libreria = GridLayout(cols=2,spacing=[10,10],padding=[10,10])
libreria.orientation = 'vertical'

#widget contenedor raiz
principal=PageLayout(cols=2,spacing=[10,10],padding=[10,10])
principal.orientation = 'vertical'

#barra lateral
barra_lateral=GridLayout(cols=2)

#estante
class tabbed_panel(TabbedPanel):
    pass

estante=tabbed_panel()
estante.default_tab_text = 'Recientes'
#instancias de materias materias
materias=[]

#cajon 
cajon=GridLayout(cols=1,spacing=[10,10],padding=[10,10])

#screen manager 
sm = ScreenManager(transition=FadeTransition())


class MenuScreen(Screen):
    pass
class LibraryScreen(Screen):
    pass

boton_actual=" "
#encabezado organizador
encabezado=" "

#screens
screen=Screen(name='home')
screen2=Screen(name='libreria')

#propmt para recibir el nombre de materia

materia=TextInput(multiline=False,font_size=25,background_color=(0.125, 0.125, 0.125,1),background_normal= '',foreground_color=(1,1,1,1),border=(4, 4, 4, 4))

popup = Popup(title='Nombre de materia',content=materia,size_hint=(None, None), size=(200, 110))

#propmt para recibir el contenido del snippet

contenido=TextInput(multiline=False,font_size=15,background_color=(0.125, 0.125, 0.125,1),background_normal= '',foreground_color=(1,1,1,1),border=(4, 4, 4, 4))

popup_snippet=Popup(title='Nueva nota',content=contenido,size_hint=(None, None), size=(300, 400))

def crear_label(instance):
    global estante

    fecha_actual =datetime.datetime.now()

    fecha_natural = fecha_actual.strftime("%A")+' '+fecha_actual.strftime("%d")+' '+fecha_actual.strftime("%B")+' '+fecha_actual.strftime("%Y")+'\n'

    linea=encabezado+'\n'+str(fecha_natural)+'\n'+contenido.text

    instance.text=" "

    contenido.focus = False
    
    boton_actual
    #pendiente
    buscar_hijo(boton_actual,linea)

    popup_snippet.dismiss()

    
    
    
def crear_contenido(instance):
    global contenido
    global encabezado,boton_actual

    boton_actual=instance.text
    contenido.focus=True

    encabezado=instance.text+'\n'
    popup_snippet.open()


contenido.bind(on_text_validate=crear_label)

def crear_tab(materia):
    global estante
    global libreria


    th = TabbedPanelHeader(text=materia)

    layout_del_content=GridLayout(cols=1,spacing=[10,10],padding=[10,10],size_hint_y=None)

    layout_del_content.bind(minimum_height=layout_del_content.setter('height'))

    
    #habilitar el scrolliing
    my_scroll_view=ScrollView(size_hint=(1, None), size=(libreria.width,libreria.height-100))

    my_scroll_view.add_widget(layout_del_content)

    th.content=my_scroll_view




    #rescatamos referencia al contenedor de la tabla
    #materias.append()

    estante.add_widget(th)

    
    

def crear_boton(materia):
    boton = Button(text=materia,size_hint=(None,None))
    boton.bind(on_release=crear_contenido)
    #creacion de tabla para cada materia
    crear_tab(materia)
    return boton

def buscar_hijo(texto,linea):
    for hijo in estante.tab_list:
        if hijo.text == texto:
            hijo.content._viewport.add_widget(TextInput(text=linea,size_hint=(1,None),background_color=(0.125, 0.125, 0.125,1), background_normal= '',foreground_color=(1,1,1,1),border=(4, 4, 4, 4)))

def agregar(instance):
    global home 
    global popup

    home.add_widget(crear_boton(materia.text))
    popup.dismiss()
    materia.text=" "

materia.bind(on_text_validate=agregar)

def popup_materia(instance):
    global materia
    popup.open()
    materia.focus=True


def ir_a_libreria(instance):
    global sm
    sm.current='libreria'

def ir_a_home(instance):
    global sm
    sm.current='home'



class PracticalNotes(App):
    global home
    
    global sm

    global screen,screen2

    global barra_lateral,estante

    def build(self):
        #elementos home

        #boton de nueva materia
        BtnNuevaMateria = Button(text="+",size_hint=(None,None),background_color=(1, .3, .4,.50), background_normal= '',font_size=40)
        #llamado popup para agregar materias           
        BtnNuevaMateria.bind(on_release=popup_materia)
        #boton ir a libreria
        BtnAbrirLibreria = Button(text="Libreria",size_hint=(None,None),background_color=(0, .8, .0,.50), background_normal= '',font_size=27)
        #bind a libreria 
        BtnAbrirLibreria.bind(on_release=ir_a_libreria)

        #agregado de elementos a layout home
        #home.add_widget(BtnAbrirLibreria)

        home.add_widget(BtnNuevaMateria)
        
        
        #elementos libreria
        #boton volver a home
        #BtnAbrirHome = Button(text="Home",size_hint=(None,None),background_color=(0, .4, .8,.50), background_normal= '',font_size=27)
        #bind  home
        #BtnAbrirHome.bind(on_release=ir_a_home)

        #agregado elementos alayout libreria
        #barra_lateral.add_widget(BtnAbrirHome)

        #libreria.add_widget(barra_lateral)

        #elementos de barra lateral

        #agregado del estante



        libreria.add_widget(estante)

        #agregamos layouts a los screens
        
        #screen2.add_widget(libreria)
        screen.add_widget(home)
        
        

        #agregamos screns al manager
        sm.add_widget(screen)
        sm.add_widget(screen2)



        w = EffectWidget()
        w.add_widget(sm)

        principal.add_widget(w)
        principal.add_widget(libreria)


        return principal

window = PracticalNotes()
if __name__ == "__main__":
    window.run()