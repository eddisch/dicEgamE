import game
import tutorial

choice = int(input("Welcome to dicE gamE!\nWhat would you like to do?\n1: Play the Game!\n2: About page\n"))
if choice == 1:
    yesNoTutorial = input("Do you want a tutorial? (Y/N)")
    if yesNoTutorial == "Y" or yesNoTutorial == "y":
        tutorial.run()
    elif yesNoTutorial == "N" or yesNoTutorial == "n":
        game.run()
elif choice == 2:
    print(
        """Hi, my name is Eddisch. I'm a student so please don't judge me too hard. 
        For business or other things please contact me at eddisch2010@gmail.com""")
