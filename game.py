import turtle
import time
import random
import sqlite3

# Database setup
DB_NAME = 'snake_game.db'

def initialize_database():
    """
    Initializes the database and creates the HighScore table if it does not exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS HighScore (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        score INTEGER NOT NULL
    )
    ''')
    cursor.execute('INSERT INTO HighScore (score) SELECT 0 WHERE NOT EXISTS (SELECT 1 FROM HighScore)')
    conn.commit()
    conn.close()

def get_high_score():
    """
    Retrieves the high score from the database.
    
    Returns:
    -------
    int
        The high score.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT score FROM HighScore LIMIT 1')
    high_score = cursor.fetchone()[0]
    conn.close()
    return high_score

def save_high_score(score):
    """
    Saves the high score to the database if it is higher than the current high score.
    
    Parameters:
    ----------
    score : int
        The score to be saved as the high score.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('UPDATE HighScore SET score = ? WHERE score < ?', (score, score))
    conn.commit()
    conn.close()

# Initialize database
initialize_database()

# Game variables
delay = 0.1
score = 0
high_score = get_high_score()

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")  # New background color
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")  # New head color
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("gold")  # New food color
food.penup()
food.goto(0, 100)

segments = []

# Pen for score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")  # Score text color
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Functions to control the snake
def go_up():
    """
    Changes the direction of the snake to up if it is not currently moving down.
    """
    if head.direction != "down":
        head.direction = "up"

def go_down():
    """
    Changes the direction of the snake to down if it is not currently moving up.
    """
    if head.direction != "up":
        head.direction = "down"

def go_left():
    """
    Changes the direction of the snake to left if it is not currently moving right.
    """
    if head.direction != "right":
        head.direction = "left"

def go_right():
    """
    Changes the direction of the snake to right if it is not currently moving left.
    """
    if head.direction != "left":
        head.direction = "right"

def move():
    """
    Moves the snake in the current direction.
    """
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")       # Up arrow key
wn.onkeypress(go_down, "Down")   # Down arrow key
wn.onkeypress(go_left, "Left")   # Left arrow key
wn.onkeypress(go_right, "Right") # Right arrow key

# Main game loop
while True:
    wn.update()

    # Check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset the score
        score = 0
        delay = 0.1

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new segment with alternating red and blue colors
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        # Alternate colors: red for even indices, blue for odd indices
        if len(segments) % 2 == 0:
            new_segment.color("red")
        else:
            new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
            save_high_score(high_score)

        delay -= 0.001

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1

            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
