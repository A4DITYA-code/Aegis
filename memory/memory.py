class Memory:
    def __init__(self):
        self.memory = {}
    
    def remember(self, key, value):
        if key and value:
            self.memory[key] = value
            return "success"
        else:
            return "failure"
    
    def whatis(self, key):
        if key in self.memory:
            return self.memory[key]
        else:
            return "I don't have any information about that."