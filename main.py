""" This is a probability calculator. It has a Hat class that takes a number of arguments that
 specify the number of balls of each color that are in the hat, and a draw method that randomly
 draws a number of balls WITHOUT REPLACEMENT.
There is then an experiment class that returns the probability of drawing balls ofa  specific color
if we repeat the experiment a specified number of times"""

import random
import copy

class Hat:

    """ This clas defines the Hat for whoch balls can be placed in, and a method to draw them """

    def __init__(self, **kwargs):
        self.hat = kwargs
        self.contents = []
        ball_colour_freq = kwargs.values()
        self.total_balls = sum(ball_colour_freq)
        for key in kwargs.keys():
            self.contents.append(key)


    def draw(self, balls_to_be_drawn):

        """ This is function that randomly draws a specified number of balls
        (called balls_to_be_drawn) from the hat."""

        self.balls_to_be_drawn = balls_to_be_drawn
        drawn = dict.fromkeys(self.hat.keys(), 0)
        for i in range(balls_to_be_drawn):
            # drawing a random ball
            ball_drawn = random.choice(list(self.hat))
            self.hat[ball_drawn] = - 1
            drawn[ball_drawn] = + 1
        cat = list(drawn.keys())
        return cat

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    """ a function that returns the probability of drawing certain types of balls over
    n experiments"""

    match = 0
    balls_drawn_in_experiment_set = set(hat.draw(num_balls_drawn))
    expected_balls_set = set(expected_balls.keys())
    for i in range(num_experiments):
        if set(balls_drawn_in_experiment_set).intersection(set(expected_balls_set)) != 0:
            match = + 1
    probability = match / num_experiments
    return probability
