import random
from textx import metamodel_from_file
robot_mm = metamodel_from_file('robot.tx')
robot_model = robot_mm.model_from_file('enderman.rbt')

class Robot:

    def __init__(self):
        # Initial position is (0,0)
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"Robot position is {self.x}, {self.y}."

    def interpret(self, model):

        # model is an instance of Program
        for c in model.commands:

            if c.__class__.__name__ == "InitialCommand":
                if c.x != 0 or c.y != 0:
                    raise Exception(f"Expected 0, 0, recieved {c.x}, {c.y}")
                print(f"Setting position to: {c.x}, {c.y}")
                self.x = c.x
                self.y = c.y
            else:
                if c.direction == "random":
                    print(f"Going to random position in a {c.steps} square \"radius\" from current position")
                elif c.direction == "360":
                    print(f"Taking {360 * (1 if c.steps == 0 else c.steps)} degrees of rotation.")
                else:
                    print(f"Going {c.direction} for {c.steps} step(s).")

                move = {
                    "360": (0, 0),
                    "up": (0, 1),
                    "down": (0, -1),
                    "left": (-1, 0),
                    "right": (1, 0),
                    "upleft": (-1, 1),
                    "upright": (1, 1),
                    "downleft": (-1, -1),
                    "downright": (1, -1),
                    "random": (1, 1)
                }[c.direction]

                # Calculate new robot position
                if c.direction == "random":
                    self.x += random.randint(-c.steps, c.steps)
                    self.y += random.randint(-c.steps, c.steps)
                else:
                    self.x += c.steps * move[0]
                    self.y += c.steps * move[1]

            print(self)

robot = Robot()
robot.interpret(robot_model)