import game

choice = int(input("Welcome to dicE gamE!\nWhat would you like to do?\n1: Play the Game!\n2: About page"))
if choice == 1:
    game.run()
elif choice == 2:
    print(
        """Hi, my name is Eddisch. I'm a student so please don't judge me too hard. 
        For business or other things please contact me at eddisch2010@gmail.com""")
