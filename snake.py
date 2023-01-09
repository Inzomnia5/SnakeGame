from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snakehead = self.segments[0]
        self.add_bodypart_offset = 0

    def create_snake(self):
        """Generate 3 snake peaces with the head on Coordinate x0y0"""
        for parts in range(0, 3):
            self.add_segment(0)

    def add_segment(self, add_bodypart_offset):
        bodypart = Turtle(shape="square")
        bodypart.color("white")
        bodypart.penup()
        add_bodypart_offset -= 20
        self.segments.append(bodypart)

    def extend_snake(self):
        self.add_segment(self.add_bodypart_offset)

    # move snake based on player inputControls AND avoid snake moving backwards
    def up(self):
        if self.snakehead.heading() != DOWN:
            self.snakehead.setheading(UP)

    def down(self):
        if self.snakehead.heading() != UP:
            self.snakehead.setheading(DOWN)

    def left(self):
        if self.snakehead.heading() != RIGHT:
            self.snakehead.setheading(LEFT)

    def right(self):
        if self.snakehead.heading() != LEFT:
            self.snakehead.setheading(RIGHT)

    def move(self):
        """all snake segments follow segment[0] which is the 'Snake Head'"""
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.snakehead.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for part in self.segments:
            part.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.snakehead = self.segments[0]
