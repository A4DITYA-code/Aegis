class Calculator:
  
    def __init__(self):
        self.operations = {
          "+": self.add,
          "-": self.subtract,
          "*": self.multiply,
          "/": self.divide,
          "**": self.power
        }
        
    def add (self, a, b):
        return a + b
      
    def subtract (self, a, b):
        return a - b
      
    def multiply (self,a ,b):
        return a * b
    def divide (self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
    def power (self, a, b):
        return a ** b