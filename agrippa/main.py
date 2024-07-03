from agrippa.agent.agent import call_agrippa
from termcolor import colored
  
def main():
    # Greet the user
    print(colored("Agrippa ", "yellow", attrs=["bold"]) + colored("awaits your command.", "red"))

    while True:
        # Read user input
        print(colored("Princeps: ", "magenta"), end="")
        human_message = input()

        # Call agent and print response
        response = call_agrippa(human_message).get("output")
        print(colored(response.replace("\n", "\n"), 'yellow'))

if __name__ == "__main__":
    main()
