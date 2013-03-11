from kivy.app import App
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.vector import Vector
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ReferenceListProperty
from kivy.config import Config
from kivy.clock import Clock

Builder.load_string('''
<Square>
    size: 20, 20
    canvas:
        Color:
            rgba: 1, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
<BoardUI>
    ball: pong_ball
    Square:
        id: pong_ball
        center: self.parent.center


    ''')

class Square(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class BoardUI(Widget):
    ball = ObjectProperty(None)

    def __init__(self):
        Widget.__init__(self)
        self.ball.velocity = (2,0)

    def on_touch_down(self, touch):
        print("Touch widget at ({0}, {1})".format(touch.px, touch.py))
        
    def update(self, dt):
        self.ball.move()

        if self.ball.y < 0:
            self.ball.velocity_y *= -1

        if self.ball.x < 0 or self.ball.right > 550:
            self.ball.velocity_x *= -1


    def draw(self, **kwargs):
        pass


class JuegoApp(App):
    def build(self):
        Config.set('graphics', 'width', '550')
        Config.set('graphics', 'height', '400')
        Config.write()

        board = BoardUI()
        Clock.schedule_interval(board.update, 1.0/60.0)
        return board



if __name__ == '__main__':
    JuegoApp().run()

