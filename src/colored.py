from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.config import Config
from kivy.clock import Clock
from kivy.utils import get_random_color
from kivy.properties import ObjectProperty
from random import *

'''
obtener todas las posiciones en una grilla
usar un random choice de las posibilidad
'''
class DashboardPositions():
    def __init__(self, dimensiones=None, pox=0, poy=0):
        self.posiciones = []
        self.screenW = dimensiones[0]
        self.screenH = dimensiones[1]

    def populate(self):
        lines = self.screenH / 20
        cols = self.screenW / 20
        for y in range(lines):
            for x in range(cols):
                self.posiciones.append((y,x))

    def transformPosition(self):
        cols = self.screenW / 20
        lines = self.screenH / 20
        totales =  cols * lines
        print "totales posiciones: " + str(cols * lines)

    def getPositions(self):
        return self.posiciones

class DashboardHistory():
    def __init__(self):
        self.history = []
    def __repr__(self):
        return str(self.history)
    def savePosition(self,t):
        self.history.append(t)

class BoardUI(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.h = DashboardHistory()
        self.p = DashboardPositions(Window.size)
        self.p.populate()
        self.l = self.p.getPositions()

    def update(self, dt):
        self.drawSquare()

    def drawSquare(self):
        if len(self.l) == 0:
            Clock.unschedule(self.update)
            return False
        x = choice(self.l)
        self.l.remove(x)
        
        t = (x[1]*20,x[0]*20)
        print t
        self.h.savePosition(t)
        
        with self.canvas:
            color = Color(random(), random(), random(), mode='rgb')
            Rectangle(pos=t, size=(20, 20))


class JuegoApp(App):
    def build(self):
        Config.set('graphics', 'width', '550')
        Config.set('graphics', 'height', '400')
        Config.write()

        board = BoardUI()
        Clock.schedule_interval(board.update, .1)
        return board



if __name__ == '__main__':
    JuegoApp().run()

