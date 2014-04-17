import sys

from random import sample
from collections import deque

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import Rectangle, Ellipse, Color
from kivy.core.window import Window

class PacMan(Widget):
    speed = (0, 0)

class Ghost(Widget):
    pass

class Wall(Widget):
    pass

class Pellet(Widget):
    pass

class Pill(Widget):
    pass

class PacManGame(Widget):
    running = True
    score_label = ObjectProperty(None)
    state_label = ObjectProperty(None)
    pacman = ObjectProperty(None)
    red = ObjectProperty(None)
    orange = ObjectProperty(None)
    teal = ObjectProperty(None)
    pink = ObjectProperty(None)
    p1_2 = ObjectProperty(None)
    p1_3 = ObjectProperty(None)
    p1_4 = ObjectProperty(None)
    p1_5 = ObjectProperty(None)
    p1_6 = ObjectProperty(None)
    p1_7 = ObjectProperty(None)
    p1_8 = ObjectProperty(None)
    p2_1 = ObjectProperty(None)
    p2_5 = ObjectProperty(None)
    p2_9 = ObjectProperty(None)
    p3_1 = ObjectProperty(None)
    p3_3 = ObjectProperty(None)
    p3_4 = ObjectProperty(None)
    p3_5 = ObjectProperty(None)
    p3_6 = ObjectProperty(None)
    p3_7 = ObjectProperty(None)
    p3_9 = ObjectProperty(None)
    p4_1 = ObjectProperty(None)
    p4_2 = ObjectProperty(None)
    p4_3 = ObjectProperty(None)
    p4_5 = ObjectProperty(None)
    p4_7 = ObjectProperty(None)
    p4_8 = ObjectProperty(None)
    p4_9 = ObjectProperty(None)
    p5_3 = ObjectProperty(None)
    p5_5 = ObjectProperty(None)
    p5_7 = ObjectProperty(None)
    p6_1 = ObjectProperty(None)
    p6_2 = ObjectProperty(None)
    p6_3 = ObjectProperty(None)
    p6_4 = ObjectProperty(None)
    p6_5 = ObjectProperty(None)
    p6_6 = ObjectProperty(None)
    p6_7 = ObjectProperty(None)
    p6_8 = ObjectProperty(None)
    p6_9 = ObjectProperty(None)
    p7_1 = ObjectProperty(None)
    p7_3 = ObjectProperty(None)
    p7_7 = ObjectProperty(None)
    p7_9 = ObjectProperty(None)
    p8_1 = ObjectProperty(None)
    p8_3 = ObjectProperty(None)
    p8_7 = ObjectProperty(None)
    p8_9 = ObjectProperty(None)
    p9_1 = ObjectProperty(None)
    p9_3 = ObjectProperty(None)
    p9_7 = ObjectProperty(None)
    p9_9 = ObjectProperty(None)
    p10_1 = ObjectProperty(None)
    p10_3 = ObjectProperty(None)
    p10_7 = ObjectProperty(None)
    p10_9 = ObjectProperty(None)
    p11_1 = ObjectProperty(None)
    p11_3 = ObjectProperty(None)
    p11_7 = ObjectProperty(None)
    p11_9 = ObjectProperty(None)
    p12_1 = ObjectProperty(None)
    p12_3 = ObjectProperty(None)
    p12_7 = ObjectProperty(None)
    p12_9 = ObjectProperty(None)
    p13_1 = ObjectProperty(None)
    p13_2 = ObjectProperty(None)
    p13_3 = ObjectProperty(None)
    p13_4 = ObjectProperty(None)
    p13_5 = ObjectProperty(None)
    p13_6 = ObjectProperty(None)
    p13_7 = ObjectProperty(None)
    p13_8 = ObjectProperty(None)
    p13_9 = ObjectProperty(None)
    p14_3 = ObjectProperty(None)
    p14_5 = ObjectProperty(None)
    p14_7 = ObjectProperty(None)
    p15_1 = ObjectProperty(None)
    p15_2 = ObjectProperty(None)
    p15_3 = ObjectProperty(None)
    p15_5 = ObjectProperty(None)
    p15_7 = ObjectProperty(None)
    p15_8 = ObjectProperty(None)
    p15_9 = ObjectProperty(None)
    p16_1 = ObjectProperty(None)
    p16_3 = ObjectProperty(None)
    p16_4 = ObjectProperty(None)
    p16_5 = ObjectProperty(None)
    p16_6 = ObjectProperty(None)
    p16_7 = ObjectProperty(None)
    p16_9 = ObjectProperty(None)
    p17_1 = ObjectProperty(None)
    p17_5 = ObjectProperty(None)
    p17_9 = ObjectProperty(None)
    p18_2 = ObjectProperty(None)
    p18_3 = ObjectProperty(None)
    p18_4 = ObjectProperty(None)
    p18_5 = ObjectProperty(None)
    p18_6 = ObjectProperty(None)
    p18_7 = ObjectProperty(None)
    p18_8 = ObjectProperty(None)
    pill1_1 = ObjectProperty(None)
    pill1_9 = ObjectProperty(None)
    pill18_1 = ObjectProperty(None)
    pill18_9 = ObjectProperty(None)
    ghosts_scared = False
            
    def __init__(self, *args, **kwargs):
        super(PacManGame, self).__init__(*args, **kwargs)
        self.ghosts = (self.red, self.orange, self.teal, self.pink)
        self.score = 1
        if sys.platform in ('linux2', 'darwin', 'win32'):
            self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
            self._keyboard.bind(on_key_down=self._on_key_down, on_key_up=self._on_key_up)
        self.walls = set()
        #border
        for x in xrange(20):
            self.walls.add((x, 0))
            self.walls.add((x, 10))
        for y in xrange(5):
            self.walls.add((0, y))
            self.walls.add((19, y))
        for y in xrange(6, 11):
            self.walls.add((0, y))
            self.walls.add((19, y))
        self.walls.add((-1, 5))
        self.walls.add((20, 5))
        #attached lines
        for y in xrange(3):
            self.walls.add((5, y))
            self.walls.add((14, y))
        for y in xrange(8, 11):
            self.walls.add((5, y))
            self.walls.add((14, y))
        #L shapes
        for y in xrange(2, 5):
            self.walls.add((2, y))
            self.walls.add((17, y))
        self.walls.add((3, 2))
        self.walls.add((16, 2))
        for y in xrange(6, 9):
            self.walls.add((2, y))
            self.walls.add((17, y))
        self.walls.add((3, 8))
        self.walls.add((16, 8))
        #short lines
        self.walls.add((4, 4))
        self.walls.add((5, 4))
        self.walls.add((4, 6))
        self.walls.add((5, 6))
        self.walls.add((14, 4))
        self.walls.add((15, 4))
        self.walls.add((14, 6))
        self.walls.add((15, 6))
        #long lines
        for x in xrange(7, 13):
            self.walls.add((x, 2))
            self.walls.add((x, 8))
        #box
        for x in xrange(7, 13):
            self.walls.add((x, 4))
        for y in xrange(4, 7):
            self.walls.add((7, y))
            self.walls.add((12, y))
        self.walls.add((8, 6))
        self.walls.add((11, 6))
        self.pellets = {(1, 2): self.p1_2, (1, 3): self.p1_3, (1, 4): self.p1_4, (1, 5): self.p1_5, (1, 6): self.p1_6, (1, 7): self.p1_7, (1, 8): self.p1_8, (2, 1): self.p2_1, (2, 5): self.p2_5, (2, 9): self.p2_9, (3, 1): self.p3_1, (3, 3): self.p3_3, (3, 4): self.p3_4, (3, 5): self.p3_5, (3, 6): self.p3_6, (3, 7): self.p3_7, (3, 9): self.p3_9, (4, 1): self.p4_1, (4, 2): self.p4_2, (4, 3): self.p4_3, (4, 5): self.p4_5, (4, 7): self.p4_7, (4, 8): self.p4_8, (4, 9): self.p4_9, (5, 3): self.p5_3, (5, 5): self.p5_5, (5, 7): self.p5_7, (6, 1): self.p6_1, (6, 2): self.p6_2, (6, 3): self.p6_3, (6, 4): self.p6_4, (6, 5): self.p6_5, (6, 6): self.p6_6, (6, 7): self.p6_7, (6, 8): self.p6_8, (6, 9): self.p6_9, (7, 1): self.p7_1, (7, 3): self.p7_3, (7, 7): self.p7_7, (7, 9): self.p7_9, (8, 1): self.p8_1, (8, 3): self.p8_3, (8, 7): self.p8_7, (8, 9): self.p8_9, (9, 1): self.p9_1, (9, 3): self.p9_3, (9, 7): self.p9_7, (9, 9): self.p9_9, (10, 1): self.p10_1, (10, 3): self.p10_3, (10, 7): self.p10_7, (10, 9): self.p10_9, (11, 1): self.p11_1, (11, 3): self.p11_3, (11, 7): self.p11_7, (11, 9): self.p11_9, (12, 1): self.p12_1, (12, 3): self.p12_3, (12, 7): self.p12_7, (12, 9): self.p12_9, (13, 1): self.p13_1, (13, 2): self.p13_2, (13, 3): self.p13_3, (13, 4): self.p13_4, (13, 5): self.p13_5, (13, 6): self.p13_6, (13, 7): self.p13_7, (13, 8): self.p13_8, (13, 9): self.p13_9, (14, 3): self.p14_3, (14, 5): self.p14_5, (14, 7): self.p14_7, (15, 1): self.p15_1, (15, 2): self.p15_2, (15, 3): self.p15_3, (15, 5): self.p15_5, (15, 7): self.p15_7, (15, 8): self.p15_8, (15, 9): self.p15_9, (16, 1): self.p16_1, (16, 3): self.p16_3, (16, 4): self.p16_4, (16, 5): self.p16_5, (16, 6): self.p16_6, (16, 7): self.p16_7, (16, 9): self.p16_9, (17, 1): self.p17_1, (17, 5): self.p17_5, (17, 9): self.p17_9, (18, 2): self.p18_2, (18, 3): self.p18_3, (18, 4): self.p18_4, (18, 5): self.p18_5, (18, 6): self.p18_6, (18, 7): self.p18_7, (18, 8): self.p18_8}
        self.pills = {(1, 1): self.pill1_1, (1, 9): self.pill1_9, (18, 1): self.pill18_1, (18, 9): self.pill18_9}
        self.pacman.gridpos = (0, 5)
        self.red.gridpos = (8, 5)
        self.orange.gridpos = (9, 5)
        self.teal.gridpos = (10, 5)
        self.pink.gridpos = (11, 5)
        self.ghost_steps = 30.0
        self.ghost_time = 0.75
        self.pacman_steps = 10.0
        self.pacman_time = 0.25
        
        if sys.platform == 'linux3':
            self.provider = None
            import sensor
            try:
                self.provider = sensor.SensorListener('accelerometer', self.on_sensor)
                self.provider.start()
            except sensor.SensorNotFound:
                pass
            self.trigger_sensor_update_values = Clock.create_trigger(self.sensor_update_values, 0)
        Clock.schedule_interval(self.update_ghosts, self.ghost_time)
    
    def on_sensor(self, provider, eventname, *args):
        if provider is not self.provider:
            return
        if eventname == 'accuracy-changed':
            sensor, accuracy = args[:2]
        elif eventname == 'sensor-changed':
            event = args[0]
            self.sensor_values = event.values
            self.trigger_sensor_update_values()
    
    def sensor_update_values(self, *args):
        values = self.sensor_values[:2]
        if abs(values[0]) < 1.5 and abs(values[1]) < 1.5:
            if self.pacman.speed != (0, 0):
                Clock.unschedule(self.update_pacman)
                self.pacman.speed = (0, 0)
        else:
            speed = self.pacman.speed
            if abs(values[0]) > abs(values[1]):
                if values[0] < 0:
                    self.pacman.speed = (0, 1)
                else:
                    self.pacman.speed = (0, -1)
            else:
                if values[1] < 0:
                    self.pacman.speed = (-1, 0)
                else:
                    self.pacman.speed = (1, 0)
            if ((self.pacman.gridpos[0] + self.pacman.speed[0]) % 20, (self.pacman.gridpos[1] + self.pacman.speed[1]) % 11) in self.walls:
                if 1.5 < abs(values[0]) < abs(values[1]):
                    if values[0] < 0:
                        self.pacman.speed = (0, 1)
                    else:
                        self.pacman.speed = (0, -1)
                elif 1.5 < abs(values[1]) <= abs(values[0]):
                    if values[1] < 0:
                        self.pacman.speed = (-1, 0)
                    else:
                        self.pacman.speed = (1, 0)
            if speed == (0, 0) and self.pacman.speed != (0, 0):
                Clock.schedule_interval(self.update_pacman, self.pacman_time)
    
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down, on_key_up=self._on_key_up)
        self._keyboard = None
    
    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'spacebar':
            self.restart()
        speed = self.pacman.speed
        for k, s in ('w', (0, 1)), ('a', (-1, 0)), ('s', (0, -1)), ('d', (1, 0)):
            if keycode[1] == k:
                self.pacman.speed = s
        if speed == (0, 0) and self.pacman.speed != (0, 0):
            Clock.schedule_interval(self.update_pacman, self.pacman_time)

    def _on_key_up(self, keyboard, keycode):
        speed = self.pacman.speed
        for k, s in ('w', (0, 1)), ('a', (-1, 0)), ('s', (0, -1)), ('d', (1, 0)):
            if keycode[1] == k and self.pacman.speed == s:
                self.pacman.speed = (0, 0)
        if speed != (0, 0) and self.pacman.speed == (0, 0):
            Clock.unschedule(self.update_pacman)
    
    def on_touch_down(self, touch):
        #speed = self.pacman.speed
        #x, y = touch.x - self.width / 2, touch.y - self.height / 2
        #if abs(x) > abs(y):
        #    self.pacman.speed = (1, 0) if x > 0 else (-1, 0)
        #else:
        #    self.pacman.speed = (0, 1) if y > 0 else (0, -1)
        #if speed == (0, 0) and self.pacman.speed != (0, 0):
        #    Clock.schedule_interval(self.update_pacman, 0.5)
        if sys.platform == 'linux3':
            self.restart()
    
    def on_touch_move(self, touch):
        #self.on_touch_down(touch)
        pass
    
    def on_touch_up(self, touch):
        #if self.pacman.speed != (0, 0):
        #    Clock.unschedule(self.update_pacman)
        #    self.pacman.speed = (0, 0)
        pass
    
    def serve_ball(self):
        for obj in self.ghosts:
            obj.center = self.center
            obj.velocity = Vector(4, 0).rotate(randint(0, 360))
    
    def restart(self):
        self.score = 0
        self.score_label.text = 'Score: 0'
        self.state_label.text = ''
        for pellet in self.pellets.values():
            if pellet not in self.children:
                self.add_widget(pellet)
        for pill in self.pills.values():
            if pill not in self.children:
                self.add_widget(pill)
        if self.pacman in self.children:
            self.remove_widget(self.pacman)
        self.pacman.gridpos = (0, 5)
        self.pacman.pos = Vector(self.pacman.gridpos[0] * self.width / 20, self.pacman.gridpos[1] * self.height / 11.25)
        self.pacman.source = 'pacman_right.png'
        self.add_widget(self.pacman)
        for ghost in self.ghosts:
            self.remove_widget(ghost)
        self.red.gridpos = (8, 5)
        self.orange.gridpos = (9, 5)
        self.teal.gridpos = (10, 5)
        self.pink.gridpos = (11, 5)
        for ghost in self.ghosts:
            ghost.pos = Vector(ghost.gridpos[0] * self.width / 20, ghost.gridpos[1] * self.height / 11.25)
            ghost.source = '%s_front.png' % ghost.color
            self.add_widget(ghost)
        Clock.unschedule(self.unscare_ghosts)
        self.unscare_ghosts(0)
        self.ghosts_scared = False
        Clock.unschedule(self.move_pacman)
        Clock.unschedule(self.stop_pacman)
        Clock.unschedule(self.move_ghosts)
        Clock.unschedule(self.stop_ghosts)
        Clock.unschedule(self.update_ghosts)
        Clock.schedule_interval(self.update_ghosts, self.ghost_time)
        self.running = True
        
    def move_ghosts(self, dt):
        for ghost in self.ghosts:
            if ghost in self.children:
                if ghost.curspeed != (0, 0):
                    ghost.pos = Vector(ghost.curspeed[0] * self.width / 20 / self.ghost_steps, ghost.curspeed[1] * self.height / 11.25 / self.ghost_steps) + ghost.pos

    def stop_ghosts(self, dt):
        Clock.unschedule(self.move_ghosts)
        for ghost in self.ghosts:
            if ghost in self.children:
                ghost.pos = Vector(ghost.gridpos[0] * self.width / 20, ghost.gridpos[1] * self.height / 11.25)
    
    def move_pacman(self, dt):
        self.pacman.pos = Vector(self.pacman.curspeed[0] * self.width / 20 / self.pacman_steps, self.pacman.curspeed[1] * self.height / 11.25 / self.pacman_steps) + self.pacman.pos
        
    def stop_pacman(self, dt):
        Clock.unschedule(self.move_pacman)
        self.pacman.pos = Vector(self.pacman.gridpos[0] * self.width / 20, self.pacman.gridpos[1] * self.height / 11.25)
    
    def update_pacman(self, dt):
        if not self.running:
            return
        x, y = self.pacman.speed
        gridpos = ((self.pacman.gridpos[0] + x) % 20, (self.pacman.gridpos[1] + y) % 11)
        if gridpos in self.walls:
            return
        if self.pacman.speed == (0, 1):
            self.pacman.source = 'pacman_back.png'
        elif self.pacman.speed == (-1, 0):
            self.pacman.source = 'pacman_left.png'
        elif self.pacman.speed == (0, -1):
            self.pacman.source = 'pacman_front.png'
        elif self.pacman.speed == (1, 0):
            self.pacman.source = 'pacman_right.png'
        if gridpos in self.pellets and self.pellets[gridpos] in self.children:
            self.score += 1
            self.remove_widget(self.pellets[gridpos])
        elif gridpos in self.pills and self.pills[gridpos] in self.children:
            self.score += 6
            self.remove_widget(self.pills[gridpos])
            self.scare_ghosts()
        if all(p not in self.children for p in self.pellets.values() + self.pills.values()):
            self.state_label.text = 'Victory!'
            Clock.unschedule(self.unscare_ghosts)
            self.running = False
        else:
            self.score_label.text = 'Score: %d' % self.score
        self.pacman.gridpos = gridpos
        self.pacman.curspeed = self.pacman.speed
        Clock.unschedule(self.stop_pacman)
        Clock.schedule_interval(self.move_pacman, self.pacman_time / self.pacman_steps)
        Clock.schedule_once(self.stop_pacman, self.pacman_time)
        for ghost in self.ghosts:
            if ghost.gridpos == self.pacman.gridpos:
                if self.ghosts_scared:
                    ghost.gridpos = (-1, -1)
                    self.score += 5
                    self.score_label.text = 'Score: %d' % self.score
                    self.remove_widget(ghost)
                else:
                    self.remove_widget(self.pacman)
                    self.running = False
                    self.state_label.text = 'Defeat!'
    
    def scare_ghosts(self):
        Clock.unschedule(self.unscare_ghosts)
        for ghost in self.ghosts:
            ghost.source = 'white%s' % ghost.source[ghost.source.index('_'):]
        self.ghosts_scared = True
        Clock.schedule_once(self.unscare_ghosts, 7.5)
    
    def unscare_ghosts(self, dt):
        self.ghosts_scared = False
        for ghost in self.ghosts:
            ghost.source = '%s%s' % (ghost.color, ghost.source[ghost.source.index('_'):])
        available_slots = [(8, 5), (9, 5), (10, 5), (11, 5)]
        for ghost in self.ghosts:
            if ghost in self.children and ghost.gridpos in available_slots:
                available_slots.remove(ghost.gridpos)
        for ghost in self.ghosts:
            if ghost not in self.children:
                ghost.gridpos = available_slots.pop(0)
                if self.pacman.gridpos == ghost.gridpos:
                    self.remove_widget(self.pacman)
                    self.running = False
                    self.state_label.text = 'Defeat!'
                ghost.pos = Vector(ghost.gridpos[0] * self.width / 20, ghost.gridpos[1] * self.height / 11.25)
                ghost.source = '%s_front.png' % ghost.color
                self.add_widget(ghost)
    
    def update_ghosts(self, dt):
        if not self.running:
            return
        for ghost in self.ghosts:
            ghost.curspeed = (0, 0)
        if self.ghosts_scared:
            for ghost in self.ghosts:
                if ghost not in self.children:
                    continue
                S = set(self.walls)
                for other_ghost in self.ghosts:
                    if other_ghost in self.children and other_ghost != ghost:
                        S.add(other_ghost.gridpos)
                possible = set()
                for x, y in (0, 0), (0, 1), (-1, 0), (0, -1), (1, 0):
                    if (ghost.gridpos[0] + x, ghost.gridpos[1] + y) not in S:
                        possible.add((x, y))
                ghost.speed = sample(possible, 1)[0]
                gridpos = (ghost.gridpos[0] + ghost.speed[0], ghost.gridpos[1] + ghost.speed[1])
                if ghost.speed != (0, 0) and gridpos not in S:
                    x, y = ghost.speed
                    if ghost.speed == (0, 1):
                        ghost.source = 'white_back.png'
                    elif ghost.speed == (-1, 0):
                        ghost.source = 'white_left.png'
                    elif ghost.speed == (0, -1):
                        ghost.source = 'white_front.png'
                    elif ghost.speed == (1, 0):
                        ghost.source = 'white_right.png'
                    ghost.gridpos = gridpos
                    ghost.curspeed = ghost.speed
                    if ghost.gridpos == self.pacman.gridpos:
                        ghost.gridpos = (-1, -1)
                        ghost.curspeed = (0, 0)
                        self.score += 5
                        self.score_label.text = 'Score: %d' % self.score
                        self.remove_widget(ghost)
        else:
            for ghost in self.ghosts:
                ghost.speed = (0, 0)
                S = set(self.walls)
                for other_ghost in self.ghosts:
                    if other_ghost != ghost:
                        S.add(other_ghost.gridpos)
                Q = deque()
                for x, y in (0, 0), (0, 1), (-1, 0), (0, -1), (1, 0):
                    p = (ghost.gridpos[0] + x, ghost.gridpos[1] + y)
                    if p not in S:
                        S.add(p)
                        Q.append((p, (x, y)))
                while len(Q) > 0:
                    gridpos, d = Q.popleft()
                    if gridpos == self.pacman.gridpos:
                        ghost.speed = d
                        break
                    for x, y in (0, 1), (-1, 0), (0, -1), (1, 0):
                        p = (gridpos[0] + x, gridpos[1] + y)
                        if p not in S:
                            S.add(p)
                            Q.append((p, d))
                x, y = ghost.speed
                if ghost.speed == (0, 0):
                    continue
                elif ghost.speed == (0, 1):
                    ghost.source = '%s_back.png' % ghost.color
                elif ghost.speed == (-1, 0):
                    ghost.source = '%s_left.png' % ghost.color
                elif ghost.speed == (0, -1):
                    ghost.source = '%s_front.png' % ghost.color
                elif ghost.speed == (1, 0):
                    ghost.source = '%s_right.png' % ghost.color
                ghost.gridpos = (ghost.gridpos[0] + x, ghost.gridpos[1] + y)
                ghost.curspeed = ghost.speed
                if ghost.gridpos == self.pacman.gridpos:
                    self.remove_widget(self.pacman)
                    self.running = False
                    self.state_label.text = 'Defeat!'
        Clock.unschedule(self.stop_ghosts)
        Clock.schedule_interval(self.move_ghosts, self.ghost_time / self.ghost_steps)
        Clock.schedule_once(self.stop_ghosts, self.ghost_time)
    
class PacManApp(App):
    def build(self):
        game = PacManGame()
        return game
    
if __name__ == '__main__':
    PacManApp().run()
