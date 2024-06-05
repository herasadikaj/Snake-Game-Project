

import turtle
import time
import random

delay = 0.1


score = 0
high_score = 0


screen = turtle.Screen()
screen.title("Snake Game 🐍")
screen.bgpic("Garden.png") 
screen.setup(width=640, height=640)  
screen.tracer(0) 



head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "Stop"


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
segments = []



pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 255)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "normal"))



instruction_pen = turtle.Turtle()
instruction_pen.speed(0)
instruction_pen.color("black")
instruction_pen.penup()
instruction_pen.hideturtle()
instruction_pen.goto(0, -288)
instructions = "Use the W, S, A, D keys to move the snake."
instruction_pen.write(instructions, align="center", font=("Courier", 12, "normal"))


def update_score():
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))


def move_food():
    x = random.randint(-270, 270)
    y = random.randint(-270, 220)  
    food.goto(x, y)


def hits_score_area():
    if head.distance(0, 255) < 20:
        return True
    return False


def food_in_score_area():
    if food.distance(0, 255) < 20:
        return True
    return False



def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
def move():
    movements = {
        "up" : (0, 20),
        "down" : (0, -20),
        "left" : (-20, 0),
        "right" : (20, 0)
    }
    dx , dy = movements.get(head.direction, (0, 0))
    head.setx(head.xcor() + dx)
    head.sety(head.ycor() + dy)



screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")



while True:
    screen.update()
    
   
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

     
        for segment in segments:
            segment.goto(1000, 1000)
    
        
        segments.clear()
    
       
        score = 0
    
    
        delay = 0.1
        update_score()
    

    
    if head.distance(food) < 20:

        
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
    
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
    
    
        delay -= 0.001
       
        score += 1
        if score > high_score:
            high_score = score
        update_score()
    

   
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
   
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    

    
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
    
           
            for segment in segments:
                segment.goto(1000, 1000)

            
            segments.clear()
    
            
            score = 0
    
           
            delay = 0.1
            update_score()
             
    time.sleep(delay)
