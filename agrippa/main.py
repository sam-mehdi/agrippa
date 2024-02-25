import os
from agrippa.agent.agent import call_agrippa
  
def main():
    # Setup complete. Greet the user
    os.system('color') # Enable color in Windows terminal
    from termcolor import colored
    print(colored("Agrippa ", "yellow", attrs=["bold"]) + colored("awaits your command.", "red"))

    while True:
        # Read user input
        print(colored("Princeps: ", "magenta"), end="")
        human_message = input()

        response = call_agrippa(human_message).get("output")
        print(colored(response.replace("\n", "\n"), 'yellow'))

if __name__ == "__main__":
    main()
