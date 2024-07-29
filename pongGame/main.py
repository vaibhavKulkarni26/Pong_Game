import time
from turtle import Screen
from Paddle import Paddle
from ball import Ball
from scorboard import Scorboard

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


r_paddle= Paddle((350,0))
l_paddle= Paddle((-350,0))
ball=Ball()
scorboard = Scorboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>260 or ball.ycor()< -260:
        ball.bounce_y()

    # collision with paddle
    if ball.distance(r_paddle)< 50 and ball.xcor() > 320 or ball.distance(l_paddle)< 50 and ball.xcor() < -320 :
        ball.bounce_x()

    # detect  R paddle misses
    if ball.xcor() > 380:
        ball.restart()
        scorboard.l_point()


    # detect L paddle misses
    if ball.xcor() < -380:
        ball.restart()
        scorboard.r_point()


screen.exitonclick()