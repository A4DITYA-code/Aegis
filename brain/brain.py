class Brain:
    def __init__(self):
        print("Brain initialized.")

    def think(self, command):
        if command.lower() == "hello":
            print("Aegis > Hello, Aditya!")

        elif command.lower() == "status":
            print("Aegis > All systems operational.")
            
        elif command.lower() == "help":
            print("========== AEGIS COMMANDS ==========")
            print("  hello   - Greets the user")
            print("  status  - Displays the system status")
            print("  help    - Displays this help message")
            print("  exit    - Shutdown Aegis")
            print("====================================")

        else:
            print("Aegis > I don't understand that command yet.")