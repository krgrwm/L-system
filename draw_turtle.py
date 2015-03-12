import turtle

def apply_rule(l, rule):
    return [rule.get(i, i) for i in l]

def init(pos):
#    turtle.delay(0)
    t = turtle.Turtle()
    t.setheading(90)
    turtle.tracer(0)
    t.penup()
    t.setpos(pos)
    t.pendown()
    return t

def draw(t, model):
    new = list(model.l)
    new = apply_rule(new, model.trule)
    for f, *p in new:
        if isinstance(f, str):
            getattr(t, f)(*p)
        else:
            f(t, *p)
    turtle.update()
    turtle.mainloop()
