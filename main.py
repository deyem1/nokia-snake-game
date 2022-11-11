from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
# segments = []
# tim1 = Turtle()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        print("nom mon nom")
        food.refresh()
        snake.extend_segments()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()

        #if head collides with tails
        #trigger game oveer sequence
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()





# starting_position = [(0, 0), (-20, 0), (-40, 0)]
# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for seg_num in range(len(segments)-1,0,-1):
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x,new_y)
#     segments[0].forward(20)
# tim2 = Turtle("square")
# tim1.color("white")
# tim2.color("white")
#
# tim1.shape("square")
# tim2.penup()
# tim2.goto(-20, 0)
#
# tim3 = Turtle("square")
# tim3.penup()
# tim3.goto(-40, 0)


screen.exitonclick()
