""" This is a probability calculator. There is a Hat class with an __init__ method that
akes a number of arguments that specify the number of balls of each colour that are in the
hat. There is also a draw method that randomly draws a number of balls out of the hat WITHOUT
REPLACEMENT. There is then an experiment function that returns the probability of drawing balls of
 a specific colour if we repeat the experiment a specified number of times"""

import random
import copy

class Hat:

    """ This class defines the Hat for which balls can be placed in, and a method to draw them """

    def __init__(self, **kwargs):
        self.hat = kwargs
        self.contents = []
        ball_colour_freq = kwargs.values()
        self.total_balls = sum(ball_colour_freq)
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)


    def draw(self, balls_to_be_drawn):

        """ This is a function that randomly draws a specified number of balls
        (called balls_to_be_drawn) out of the hat."""
        drew_balls = list()
        self.balls_to_be_drawn = balls_to_be_drawn
        for i in range(balls_to_be_drawn):
            # drawing a random ball
            ball_drawn = random.choice(list(self.hat))
            self.contents.remove(ball_drawn)
            drew_balls.append(ball_drawn)
            drew_balls.sort()
        return drew_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
#must usee copy hat in here
    """ a function that returns the probability of drawing certain colours of balls out of
    the hat over n experiments"""

    match = 0
    balls_drawn_in_experiment_set = set(hat.draw(num_balls_drawn))
    expected_balls_set = set(expected_balls.keys())
    for i in range(num_experiments):
        if set(balls_drawn_in_experiment_set).intersection(set(expected_balls_set)) != 0:
            match = + 1
    probability = match / num_experiments
    return probability
