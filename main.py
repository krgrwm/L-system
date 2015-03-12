import lsystem
import draw_turtle
import random

class Koch(object):
    def __init__(self):
        self.l = "-F"
        self.rule = {'F': 'F+F-F-F+F'}
        self.trule = {'F': ['forward', 3.4], '+': ['right', 90], '-': ['left', 90]}

class Tree(object):
    def __init__(self):
        self.stack = []
        d = 0.5
        self.l = "A"
        self.rule = {'B': 'BB', 'A': 'B[A]A'}
        self.trule = {'A': ['forward', d], 'B': ['forward', d], '[': [self.push], ']': [self.pop]}
        random.seed()
        self.deg = [0, 90]

    def push(self, t):
        self.l.append([t.heading(), t.pos()])
        t.left(random.randint(*self.deg))

    def pop(self, t):
        h, pos = self.l.pop()
        t.penup()
        t.setheading(h)
        t.setpos(pos)
        t.right(random.randint(*self.deg))
        t.pendown()

kochisland_init = "F-F-F-F"
kochisland_rule = {'F': 'F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F'}
kochisland_rule2 = {'F': 'FF-F-F-F-F-F+F'}
kochisland_rule3 = {'F': 'FF-F-F-F-FF'}
kochisland_rule4 = {'F': 'F-FF--F-F'}
kochisland_rule5 = {'F': 'F-F+F-F-F'}

levyC_init = "F"
levyC_rule = {'F': '+F--F+'}

dragon_init = "FX"
dragon_rule = {"X": "X+YF", "Y": "FX-Y"}


turtle_rule_levyC = {'F': ['forward', 1.9], '+': ['right', 45], '-': ['left', 45]}
turtle_rule_dragon = {'F': ['forward', 1.9], '+': ['right', 90], '-': ['left', 90], 'X': ['forward', 0], 'Y': ['forward', 0]}

#koch = Koch()
#lsystem.step(koch, 3)
#t = draw_turtle.init((0, -190))
#draw_turtle.draw(t, koch)

tree = Tree()
lsystem.step(tree, 10)
t = draw_turtle.init((0, -190))
draw_turtle.draw(t, tree)
