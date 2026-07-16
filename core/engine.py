from brain.brain import Brain
class Engine:
    def __init__(self):
        print("Initializing Aegis Engine...")
        self.brain = Brain()
    def start(self):
        print("Aegis Engine Started")
        
        while True:
            command = input("You: ")
            if command.lower() == "exit":
                print("Shutting down.....!")
                break
            self.brain.think(command)