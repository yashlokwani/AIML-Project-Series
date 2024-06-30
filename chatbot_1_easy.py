class ChatBot:
    def __init__(self):
        self.user_name = ""
        self.context = []   

    def greet(self):
        self.user_name = input("Hello! I'm a chatbot.\nWhat's your name? ")
        self.context.append(f"User's name is {self.user_name}")
        print(f"Nice to meet you, {self.user_name}!\n")

    def farewell(self):
        print(f"\nGoodbye, {self.user_name}! It was nice chatting with you.")

    def ask_questions(self):
        questions = ["How are you feeling today? ", "Do you like programming? "]
        for question in questions:
            response = input(question)
            self.context.append(f"{question}{response}")

    def respond(self):
        responses = {
            "what is your name": "I am a chatbot named Loki.",
            "how are you": "I'm just a bunch of code, but I'm here to help you!",
            "what can you do": "I can chat with you and remember the context of our conversation.",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "what is the weather today": "I'm not connected to the internet, but I hope it's sunny!"
        }
        while True:
            user_input = input("\nAsk me a question: ").lower()
            if user_input == "quit":
                break
            elif user_input in responses:
                print(responses[user_input])
            else:
                print("Sorry, I didn't understand that. Can you ask something else?")
                continue

    def recall_context(self):
        print("\nHere's what I remember from our conversation:")
        for memory in self.context:
            print(memory)

chatbot = ChatBot()
chatbot.greet()
chatbot.ask_questions()
chatbot.respond()
chatbot.recall_context()
chatbot.farewell()
