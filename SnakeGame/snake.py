from turtle import Turtle, Screen


screen = Screen()
STARTED_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_STEPS = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in STARTED_POSITIONS:
            new_snake = Turtle('square')
            new_snake.penup()
            new_snake.color('white')
            new_snake.goto(i)
            self.snake_body.append(new_snake)

    def move(self):
        for pos in range(len(self.snake_body) - 1, 0, -1):
            new_position = self.snake_body[pos - 1].position()
            self.snake_body[pos].goto(new_position)
        self.head.forward(SNAKE_STEPS)

    def increase_body(self):
        new_snake = Turtle('square')
        new_snake.penup()
        new_snake.color('white')
        food_pos = self.snake_body[-1].position()
        new_snake.goto(food_pos)
        self.snake_body.append(new_snake)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_reset(self):
        for i in self.snake_body:
            i.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]








