import turtle
import time

# SETTING OF SCREEN
wn=turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#  SCORE
score_a = 0
score_b = 0

#PADDLE A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()                                #penup=no drawing while moving
paddle_a.goto(-350,0)

#PADDLE B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()                               
paddle_b.goto(350,0)

#BALL
ball=turtle.Turtle()
ball.shape("circle")
ball.speed()
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=1.15
ball.dy=0.5

# PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0 Player B: 0",align="center",font=("Courier",24, "normal"))

#FUNCTION
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#KEYWORD BINDING
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"i")
wn.onkeypress(paddle_b_down,"k")

#GAME LOOP
while True:
    wn.update()
    
    #MOVE TE BALL
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #BORDER CHECKING
    if ball.ycor()>290:                  # setting boundaries for y
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()> 390:                  # setting boundaries for x
        ball.setx(390)
        ball.dx*=-1
        score_a += 1
        pen.clear()
        pen.write("Player A:{} Player B: {}".format(score_a, score_b),align="center",font=("Courier",24, "normal"))

    if ball.xcor()< -390:
        ball.setx(-390)
        ball.dx*=-1
        score_b += 1
        pen.clear()
        pen.write("Player A:{} Player B: {}".format(score_a, score_b),align="center",font=("Courier",24, "normal")) 

       
    # PADDLE AND BALL COLLISIONS
    if ball.xcor()>340 and (ball.ycor()< paddle_b.ycor()+ 50 and ball.ycor()>paddle_b.ycor() -50):
        ball.dx *= -1
    if ball.xcor()< -340 and (ball.ycor()< paddle_a.ycor()+ 50 and ball.ycor()>paddle_a.ycor() -50):
        ball.dx *= -1