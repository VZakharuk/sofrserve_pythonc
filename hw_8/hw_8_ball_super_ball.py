"""
Vasyl Zakharuk
Python Core 355
Codewars Kata. Ball Super Ball
"""



class Ball(object):
    def __init__(self, object='regular'):
        self.ball_type = object
    def ball_super(self):
        return self.ball_type

reg_ball = Ball()
print("If no arguments are given, "'ball type'" is: {}.".format(reg_ball.ball_super()))
sup_ball = Ball('super')
print("If argument ade 'super, "'ball type'" is: {}.".format(sup_ball.ball_super()))
