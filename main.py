from scoreboard import *
import time
import winsound
from food import *
from Snake import *
from box import *
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("SNAKE-GAME")
border()
screen.tracer(0)
snake=Snake()
food=Food()
score=Scoreboard()
level=screen.numinput("Difficulty","what is the difficulty you want\nenter a number for the difficulty min-high speed max-low speed",0.15,0.01,0.5)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game_is=True
while game_is:
    screen.update()
    time.sleep(level)
    snake.move()
    if snake.head.distance(food)<15:
        winsound.Beep(1000,50)
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor()<-280:
        game_is=False
        score.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is=False
            score.game_over()
screen.exitonclick()
