
def main():
    # Starting message
    print("Welcome to the Video Game Console Expert System!")
    
    # Ask  user's budget
    budget = int(input("What is your budget for a video game console? "))
    
    # Ask  user's preference for console game type
    console = input("Do you like Mario games, Halo games, or Uncharted games? ").lower()
    
    # Ask about user's preferred games
    game = input("What types of games do you prefer to play? (action, sports, RPG, etc.) ")
    

    # Ask about user's need for 4k graphics
    graphics = input("Do you want to play in 4K graphics? (yes or no) ").lower() == "yes"

    # Determine if user should buy a PlayStation, Xbox, or Nintendo Switch
    if budget >= 300 and console == "uncharted" and (game == "RPG" or game == "sports" or game == "action") and graphics:
        print("Based on your responses, we recommend that you buy a PlayStation console.")
    elif budget >= 300 and console == "halo" and (game == "RPG" or game== "sports" or game== "action") and graphics:
        print("Based on your responses, we recommend that you buy a Xbox console.")
    elif budget >= 300 and (console == "uncharted" or console == "Halo") and (game == "RPG" or game == "sports" or game== "action") and graphics:
        print("Based on your responses, we recommend that you buy an Xbox or PlayStation console.")
    elif budget >= 200 and console == "mario" and (game == "RPG" or game == "sports" or game == "action") and not graphics:
        print("Based on your responses, we recommend that you buy a Nintendo Switch console.")
    else:
        print("Based on your responses, we do not have a specific recommendation. Please consider your needs and preferences when making a decision. We cannot meet all requirements for a video game console. Please try again with different needs and we may be able to provide a recommendation.\n ")
        main()
	
if __name__ == "__main__":
    main()

