import EoniaAI
import sys

class GameInterface:
    def __init__(self):
        self.ai = EoniaAI.EoniaAI()

    def sendInput(self, input_string):
        output = self.ai.processInput(input_string)
        if output == "exit":
            sys.exit()
        print(output)

# Example of a game loop
if __name__ == "__main__":
    game_interface = GameInterface()
    print("Welcome to Elyria: Realms of Omnipotence!")
    while True:
        user_input = input("Enter a command: ")
        game_interface.sendInput(user_input)

