from visual import *


ball = sphere(pos=(5,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=(6,0,0), size=(0.2,12,12), color=color.green)
ball.velocity = vector(25,0,0)
deltat = 0.005
t=0
while t < 300:
    rate(100)
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.x <0:
        ball.velocity.x=-ball.velocity.x
    ball.pos = ball.pos + ball.velocity*deltat
    t = t + deltat