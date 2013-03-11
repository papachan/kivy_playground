from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.config import Config
from kivy.clock import Clock
from kivy.properties import ObjectProperty
import random

cant_lines = 10

class DashboardPositions:
    def __init__(self, dimensiones=None, pox=0, poy=0):
        self.posiciones = []
        self.screenW = dimensiones[0]
        self.screenH = dimensiones[1]

    def __repr__(self):
        cols = self.screenW / 20
        lines = self.screenH / 20
        return "totales posiciones: " + str(cols * lines)

    def populate(self):
        lines = self.screenH / 20
        cols = self.screenW / 20
        for y in range(lines):
            for x in range(cols):
                self.posiciones.append((y,x))


    def getPositions(self):
        return self.posiciones

class DashboardHistory:
    def __init__(self):
        self.history = []
    def __repr__(self):
        return str(self.history)
    def savePosition(self,t):
        self.history.append(t)
    def getHistory(self):
        return self.history
    def haveHistory(self):
        return len(self.history) > 0
    def length(self):
        return len(self.history)
    def clear(self):
        self.history = []

class BoardUI(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.h = DashboardHistory()
        self.p = DashboardPositions(Window.size)
        self.p.populate()
        self.l = self.p.getPositions()

    def update(self, dt):
        if len(self.l) == 0:
            Clock.unschedule(self.update)
            return False
        self.drawSquare()

    def drawSquare(self):
        self.canvas.clear()
        h = self.h.getHistory()
        flag = True
        if len(h) > 0:
            last = h[-1]
            if last < len(self.l):
                x = self.l[last]
                i = last
                t = (x[1]*20,x[0]*20)
                flag = False

        if flag == True:
            x = random.choice(self.l)
            i = self.l.index(x)
            t = (x[1]*20,x[0]*20)

        self.h.savePosition(i)
        with self.canvas:
            color = Color(random.random(), random.random(), random.random(), mode='rgb')
            Rectangle(pos=t, size=(20, 20))
        if len(h) >= cant_lines:
            self.h.clear()

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

