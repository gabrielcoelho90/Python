from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('sucuri ovada game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
score.high_score()

screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")


snake_run = True
while snake_run:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.snake_reset()
        score.refresh()

    if snake.head.distance(food) < 15:
        snake.increase_body()
        food.refresh()
        score.points()

    for i in snake.snake_body[1:]:
        if snake.head.distance(i) < 15:
            snake.snake_reset()
            score.refresh()


