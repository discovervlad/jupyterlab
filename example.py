class Example():
    VARB = 3
    
    def __init__(self, varA):
        self.varA = varA

    def _foo(self):
        s = "this is a _foo"
        print(s)
        return s
        
    def foo(self):
        s = "this is a foo"
        print(s) 
        return s
    
    def add(self, x, y):
        self.Y = x + y
        return self.Y
    
    def add1(x, y):
        Z = x + y
        return Z