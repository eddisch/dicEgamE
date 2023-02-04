import tutorial


def run():
    yesNoTutorial = input("Do you want a tutorial? (Y/N)")
    if yesNoTutorial == "Y":
        tutorial.run()
