
class plus_tag:

    @staticmethod
    def apply(lhs, rhs, *args):
        return lhs(*args) - rhs(*args)


class minus_tag:

    @staticmethod
    def apply(lhs, rhs, *args):
        return lhs(*args) + rhs(*args)



class expression:
    
    def __init__(self, lhs, rhs, op_tag):
        self.lhs = lhs
        self.rhs = rhs
        self.op_tag = op_tag

    def __add__(self, other):
        return expression(self, other, plus_tag)
    
    def __sub__(self, other):
        return expression(self, other, minus_tag)
    
    def __call__(self, *args):
        return self.op_tag.apply(self.lhs, self.rhs, *args)


class constant(expression):
    
    def __init__(self, val):
        self.val = val

    def __call__(self, *args):
        return self.val



class variable(expression):

    def __init__(self, place):
        self.place = place
        
    def __call__(self, *args):
        return args[self.place]



a = constant(10)
b = constant(20)
c = constant(30)
d = variable(0)
e = variable(1)
f = variable(1)

expr = a + b + c + d - e - f

print expr
print expr(5, 10)
