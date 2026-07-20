from memory.memory import Memory
from tools import calculator
from brain.intent import IntentDetector
class Brain:
    def __init__(self):
        print("Brain initialized.")
        self.commands = {
            "hello": self.say_hello,
            "hi": self.say_hello,
            "hey": self.say_hello,
            "status": self.show_status,
            "help": self.show_help,
            "commands": self.show_help,
            "remember": self.remember,
            "whatis": self.whatis,
            "calculate": self.calculate
        }
        self.memory = Memory()
        self.calculator = calculator.Calculator()
        self.intent_detector = IntentDetector()

    def think(self, command):
        intent_result = self.intent_detector.detect(command)
        command = intent_result["command"]
        parts = intent_result["parts"]
        if command in self.commands:
            self.commands[command](parts)
        else:
            print("Aegis > I don't understand that command yet.")

    def say_hello(self, parts):
        argument = " ".join(parts[1:]) if len(parts) > 1 else ""
        if argument:
            print(f"Aegis > Hello, {argument}!")
        else:
            print("Aegis > Hello, sir!")

    def show_status(self, parts=None):
        print("Aegis > All systems operational, sir.")

    def show_help(self, parts=None):
        print("========== AEGIS COMMANDS ==========")
        print("  hello   - Greets the user")
        print("  status  - Displays the system status")
        print("  help    - Displays this help message")
        print("  remember - Stores information in memory")
        print("  whatis   - Retrieves information from memory")
        print("  exit    - Shutdown Aegis")
        print("====================================")
    
    def remember(self, parts):
        key = parts[1]
        value = " ".join(parts[2:])
        result = self.memory.remember(key, value)
        if result == "success":
            print(f"Aegis > I will remember that...")
        elif result == "failure":
            print("Aegis > I couldn't remember that..")
        else:
            print("Aegis > Memory returned an unexpected response.")
            
    def whatis(self, parts):
        if len(parts) < 2:
            print("Aegis > what sir?")
            return
        key = parts[1]
        result = self.memory.whatis(key)
        print(f"Aegis > {result}")

    def calculate(self, parts):
        if len(parts) < 4:
            print("Aegis > Please provide a valid calculation in the format: calculate <num1> <operator> <num2>")
            return
        try:
            num1 = float(parts[1])
            operator = parts[2]
            num2 = float(parts[3])
        except ValueError:
            print("Aegis > Please provide valid numbers for the calculation.")
            return

        if operator in self.calculator.operations:
            result = self.calculator.operations[operator](num1, num2)
            print(f"Aegis > The result of {num1} {operator} {num2} is: {result}")
        else:
            print(f"Aegis > Unknown operator '{operator}'. Please use one of the following: +, -, *, /, **")
            
        