class IntentDetector:
    def __init__(self):
        self.intents = {
            "hello": ["hello", "hi", "hey"],
            "status": ["status"],
            "help": ["help", "commands"],
            "remember": ["remember"],
            "whatis": ["whatis"],
            "calculate": ["calculate"]
        }
        
        self.phrases = {
            "what is": "whatis",
            "what's": "whatis",
            "how to": "whatis",
        }
       

    def detect(self, command):
        command = command.lower()
        parts = command.split()
        result = {
            "command": None,
            "parts": None
        }
        if len(parts) >= 2:
            phrase = " ".join(parts[:2])
            if phrase in self.phrases:
                result["command"] = self.phrases[phrase]
                result["parts"] = [self.phrases[phrase]] + parts[2:]
                return result
          
        for intent, keywords in self.intents.items():
                if not parts:
                    return result
                if parts[0] in keywords:
                    result["command"] = intent
                    result["parts"] = parts
                    return result
    