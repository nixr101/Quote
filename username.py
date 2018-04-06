while 10 == 10:
    while 10 == 10:
            usernames = ("nixer101", "jjazy")
            user = input("Pick a name ")
            if user == usernames[1]:
                print("""username is taken
        Press Enter To Continue""")
                user = input()
            elif user == usernames[0]:
                print("""username is taken
        Press Enter To Continue""")
                user = input()
            else:
                print("Your username is %r" % (user))

                break
    while 10 == 10:
        while 10 == 10:
            user = user
            login = input("enter your username")

            if login == user:
                print("You are signed in!")

                print ('Hi, %r!' % (user))
                break
            else:
                print('Wrong Username')
        while 10 == 10:
            print('''
            You can: Sign out, Stop the program, or Get an inspirational Quote
                     (Enter 1 to sign out, 2 to stop the program, or 3 to get a quote''')
            action = input("Which option do you prefer?")
            if action == "1":
                break
            elif action == "2":
                print(2)
                import program
            elif action == "3":
                print(3)
                import random
                action = (random.randint(1, 3))
                if action == 1:
                        print("Doing nothing is hard, you never know when you're done.")
                elif action == 2:
                        print("I did not trip and fall. I attacked the floor and I believe I am winning.")
                elif action == 3:
                        print("""A stupid person laughs three times at a joke; once when everyone else is laughing, 
                        a second time when he actually gets the joke, and a third time when he realizes he was 
                        laughing without getting the joke at first.""")