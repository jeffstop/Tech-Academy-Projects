#
# Python:   3.9.6
#
# Author:   Jeff Stoppel
#
# Purpose:  The Tech Academy - Python Course, Creating our first program together
#           Demonstrating how to pass variables from function to function
#           while producing a functional game
#
#           Remember, function_name(variable) means that we pass in the variable
#           return variable_means that we are returning the variable to
#           back to the calling function.









def start(nice=0,mean=0,name=""):
    # Get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
   

def describe_game(name):
    """

        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """

    # Meaning, if we don not already have this user's name,
    # then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby one lucky/unlucky stranger. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


# First interaction with stranger
def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smilling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean +1)
            stop = False
        score(nice,mean,name) # pass the 3 variables to the score()

# Second interaction with stranger
def nice_mean2(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nYou follow the stranger into town. \nHe's surprised to see you again. \nWill you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger takes you to a nearby pub to \nthank you for being so nice.")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger is visibly upset \nand again storms off...")
            mean = (mean +1)
            stop = False
        score2(nice,mean,name) # pass the 3 variables to the score()

# Third interaction with stranger
def nice_mean3(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nThe stranger takes you back to the \nedge of town. He asks you to leave this place. \nWill you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger thanks you for your kindness, \nbut says you're too nice to stay in an \nevil place like this. You leave knowing \nyoury niceness can change the world.")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger can hardly contain his anger. \nHe commands you to leave, you big jerk.")
            mean = (mean +1)
            stop = False
        score3(nice,mean,name) # pass the 3 variables to the score()



def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({},mean))".format(name,nice,mean))


def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can us them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        # else, call nice_mean2 function passing in the variables so it can use them
        nice_mean2(nice,mean,name)

def score2(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can us them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        # else, call nice_mean function passing in the variables so it can use them
        nice_mean3(nice,mean,name)

def score3(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can us them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    # Substitute the {} with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # Call again function and pass in our variables
    again(nice,mean,name)


def lose(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    # Call again function and pass in our variables
    again(nice,mean,name)




def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")



def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Notice, I do not reset the name variable as that same user has selected to play again
    start(nice,mean,name)
    
















if __name__ == "__main__":
    start()
